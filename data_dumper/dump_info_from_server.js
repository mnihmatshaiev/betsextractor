const fetcher = require('./fetcher')
const fs = require('fs');
const { start } = require('repl');

function createDate(day, month, year){
    return new Date(year, month-1, day);
}

async function dumpInfoToFile(filename, startDate, endDate, sport){
    let file = fs.createWriteStream(filename, {flags: 'a'});
    file.on('error', (err => console.log(err)));
    let now = new Date()
    for(var d = startDate; d<=now && d<= endDate; d.setDate(d.getDate()+1)){
        await fetcher.dumpToStreamByDate(d.getDate(), d.getMonth()+1, d.getFullYear(), sport, file);
    }
    file.end()
}

let args = process.argv.slice(2)
var startDate=0;
var endDate=0;
var sport=0;
var file = "";

function getSportID(sport_str){
    switch(sport_str){
        case 'football':
            return 1
        case 'hockey':
            return 2
    }
}
function processArgs(){
    file = args[0]
    sport = getSportID(args[1])
    let arg3 = parseInt(args[3], 10);
    let arg4 = parseInt(args[4], 10);
    let arg5 = parseInt(args[5], 10);
    let arg7 = parseInt(args[7], 10);
    let arg8 = parseInt(args[8], 10);
    let arg9 = parseInt(args[9], 10);

    if(arg3==NaN || arg4==NaN || arg5==NaN || arg7==NaN || arg8==NaN || arg9==NaN) return;
    if(! ((args[2]=="--since" && args[6]=="--until") || (args[6]=="--since" && args[2]=="--until"))) return;
    if (args[2]=="--since") startDate=createDate(args[3],args[4],args[5])
    else endDate=createDate(args[3],args[4],args[5])
    if (args[6]=="--since") startDate=createDate(args[7],args[8],args[9])
    else endDate=createDate(args[7],args[8],args[9])
    return true;
}

if(processArgs()){
dumpInfoToFile(file, startDate, endDate, sport)} else {
    console.log("BAD ARGS")
}