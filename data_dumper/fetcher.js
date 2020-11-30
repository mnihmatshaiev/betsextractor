const fetch = require('node-fetch')
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const newLinesRegexp = new RegExp("\n", 'g')

function rowToCSV(row, year){
    let date = row.querySelector('.date').textContent.trim();
    let name = row.querySelector('.nameEvent').textContent.trim();
    let score = row.querySelector('.score').textContent.trim();
    return `${date} ${year};${name};${score}`
}

function tableToCSVList(table,year){
    var lst = []
    let rows = table.rows;
    let ligaName = rows[0].textContent.trim();
    for (var i = 1; i < rows.length; i++){
        let rowCSV = rowToCSV(rows[i], year)
        rowCSV = `${ligaName};${rowCSV}`.replace(newLinesRegexp, ", ");
        lst.push(rowCSV)
    }
    return lst;
}

async function fetchByDate(date, sport){
    console.log(`${date} - fetching data`);
    return fetch(`https://melbet.com/results/get_results_table.php?sport=${sport}&data1=${date}&s=1&typeResult=result`)
}

function writeListToStream(lst, stream){
    lst.forEach(v => {stream.write(v+'\n')})
}

module.exports.dumpToStreamByDate = async function getInfoByDate(day,month,year,sport,stream){
    let date_formated = `${day.toString().padStart(2, "0")}-${month.toString().padStart(2,"0")}-${year}`
    await fetchByDate(date_formated,sport)
    .then(res => {
        console.log(`${date_formated} - data fetched`)
        return res.text()
    }).then(body => new JSDOM(body))
    .then(dom => dom.window.document.querySelectorAll('.tableTxt'))
    .then(tables => {
        var lst = []
        console.log(`${date_formated} - formating data`)
        for(var i = 0; i<tables.length; i++){
            lst = lst.concat(tableToCSVList(tables[i], year))
        }
        console.log(`${date_formated} - data formated`)
        return lst
    }).then(lst => {
        console.log(`${date_formated} - dumping to file`)
        writeListToStream(lst, stream)
        console.log(`${date_formated} - dumped to file`)
    })
}