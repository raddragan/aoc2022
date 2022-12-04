import utils

def toRange(s:list[str]):
    return [int(r) for r in s]

def getRange(line:list[str]):
    return [toRange(p.split('-')) for p in line]

def isFullOverlap(ranges:list[list[int]]):
    s = sorted(ranges, key=lambda r: r[0])
    if(s[0][0] == s[1][0]):
        return True
    if(s[0][1] >= s[1][1]):
        return True;
    return False;

def isPartialOverlap(ranges:list[list[int]]):
    s = sorted(ranges, key=lambda r: r[0])
    if(s[0][0] == s[1][0]):
        return True
    if(s[0][1] >= s[1][0]):
        return True;
    return False;

def run():
    lines = [getRange(line.split(',')) for line in utils.readInput(4,False)]
    print(lines)
    fullOverlaps = [r for r in lines if isFullOverlap(r)]
    print(f'Step 1: {len(fullOverlaps)} pairs')
    partialOverlaps = [r for r in lines if isPartialOverlap(r)]
    print(f'Step 2: {len(partialOverlaps)} pairs')
