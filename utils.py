def readInput(day, test):
    fileName = f'input/{day}{".t" if test else ""}'
    lines = open(fileName).read().split('\n')
    return lines