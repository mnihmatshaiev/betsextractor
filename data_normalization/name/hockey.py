import re


def name_matcher_spec(name):
    res = re.match(
        r'(ШВ|БР|СП|ВВ|ГвБ|БЛТ|ШB|ББ|2МинУд|СтатИг) (.*)\s+-\s+(ШВ|БР|СП|ВВ|ГвБ|БЛТ|ШB|ББ|2МинУд|СтатИг) (.*)',
        name)
    if not res:
        return False
    spec1 = res.group(1)
    command1 = res.group(2)
    spec2 = res.group(3)
    command2 = res.group(4)
    if not spec1 == spec2:
        return False
    return f"{spec1},{command1},{command2}"


def name_matcher_default(name):
    res = re.match(r'(.*)\s+-\s+(.*)', name)
    if not res:
        return False
    command1 = res.group(1)
    command2 = res.group(2)
    return f"none,{command1},{command2}"


def name_matcher(name):
    res = name_matcher_spec(name)
    if res:
        return res
    res = name_matcher_default(name)
    if res:
        return res
    return False
