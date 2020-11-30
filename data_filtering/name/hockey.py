import re


def filter_special_leagues(line):
    if re.match(r'.*альтернатив.*', line, re.IGNORECASE):
        return False
    if re.match(r'.*товарищ.*', line, re.IGNORECASE):
        return False
    if re.match(r'[a-zA-Z0-9].*', line, re.IGNORECASE):
        return False
    if re.match(r'.*кибер.*', line, re.IGNORECASE):
        return False
    if re.match(r'.*юнош.*', line, re.IGNORECASE):
        return False
    if re.match(r'.*жен.*', line, re.IGNORECASE):
        return False
    if re.match(r'.*дуэль игроков.*', line, re.IGNORECASE):
        return False
    if re.match(r'.*\(\d\d\).*', line, re.IGNORECASE):
        return False
    return True


def filter_special_events(line):
    if not isinstance(line, str):
        return False
    if line == "none":
        return True
    return False


def filter_special_names(line):
    if not isinstance(line, str):
        return False
    if re.match(r'.*/.*', line, re.IGNORECASE):
        return False
    if re.match(r'.*\(\d\d\).*', line, re.IGNORECASE):
        return False
    if re.match(r'.*\(жен\).*', line, re.IGNORECASE):
        return False
    if re.match(r'.*\(Экстра-тайм\).*', line, re.IGNORECASE):
        return False
    if re.match(r'Хозяева.*', line, re.IGNORECASE):
        return False
    if re.match(r'.*1-е команды.*', line, re.IGNORECASE):
        return False
    if re.match(r'.*\(мол\).*', line, re.IGNORECASE):
        return False
    if re.match(r'.*\(с ОТ и буллитами\).*', line, re.IGNORECASE):
        return False
    if re.match(r'.*[a-zA-Z].*', line, re.IGNORECASE):
        return False
    if re.match(r'.*/.*', line):
        return False
    return True
