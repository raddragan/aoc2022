import utils

def compartmentalize(s:str):
    return [s[0:int(len(s)/2)],s[int(len(s)/2):]]

def run():
    ruksaks = [s for s in utils.readInput(3,False)]
    compartmentalized = [compartmentalize(s) for s in ruksaks]
    common = [utils.unique(utils.intersection(s[0],s[1]))[0] for s in compartmentalized]
    print(common)
    points = [utils.strToNum(s) for s in common]
    print(points)
    print(f'Part 1: {sum(points)}')

    groups = [ruksaks[r:r+3] for r in range(0,len(ruksaks)-1,3)]
    groupInter = [utils.arrIntersection(g)[0] for g in groups]
    print(groupInter)
    points2 = [utils.strToNum(s) for s in groupInter]
    print(points2)
    print(f'Part 2: {sum(points2)}')