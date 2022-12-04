def intersection(lst1, lst2):
    return unique([value for value in lst1 if value in lst2])

def arrIntersection(lst:list):
    return unique(intersection(intersection(lst[0], lst[1]),lst[2]))

def readInput(day, test):
    fileName = f'input/{day}{".t" if test else ""}'
    lines = open(fileName).read().split('\n')
    return lines

def unique(lst):
    return (list(set(lst)))