import re


month_name_to_number = {'янв': 1,
                        'февр': 2,
                        'март': 3,
                        'апр': 4,
                        'май': 5,
                        'июнь': 6,
                        'июль': 7,
                        'авг': 8,
                        'сент': 9,
                        'окт': 10,
                        'нояб': 11,
                        'дек': 12}


def time_matcher_default(time):
    if not isinstance(time, str):
        return False
    res = re.match(r'(\d+) (.*) (\d+):(\d+) (\d+)', time)
    if not res:
        return False
    day = res.group(1)
    month = res.group(2)
    hours = res.group(3)
    minutes = res.group(4)
    year = res.group(5)
    return f"{hours}:{minutes} {day}.{month_name_to_number[month]}.{year}"