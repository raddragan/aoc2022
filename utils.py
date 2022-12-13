def intersection(lst1, lst2):
    return unique([value for value in lst1 if value in lst2])

def arrIntersection(lst:list):
    return unique(intersection(intersection(lst[0], lst[1]),lst[2]))

def plankDistance(a:list[int], b:list[int]):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
    
def readInput(day, test):
    fileName = f'input/{day}{".t" if test else ".p"}'
    lines = open(fileName).read().split('\n')
    return lines

def strToNum(s:str):
    num = ord(s)
    if(num > 90):
        return num-96
    return num-38

def unique(lst):
    return (list(set(lst)))