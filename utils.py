def readLines(day, test):
    fileName = f'{day}{".t" if test else ""}.txt'
    f = open(fileName)
    lines = []
    for line in f:
        sanitized = line.removesuffix('\n')
        lines.append(sanitized)
    return lines