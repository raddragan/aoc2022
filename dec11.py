import utils
import math

def canDivideXByY(x:int, y:int):
    return 1 if (x % y) == 0 else 0

def getLcm(nums: list[int]):
    result = 1
    for x in nums:
        result *= x
    return result

def run():
    isTest = False
    isPartOne = False
    
    operations = [[1,19],[0,6],[2,0],[0,3]] if isTest else [[1,7],[0,4],[1,5],[2,0],[0,1],[0,8],[0,2],[0,5]]
    redirectors = [[2,3],[2,0],[1,3],[0,1]] if isTest else [[6,4],[7,5],[5,1],[0,4],[6,2],[7,3],[2,1],[3,0]]
    divisors = [23,19,13,17] if isTest else [19,3,13,17,2,11,5,7]
    lcm = getLcm(divisors)
    queued = []
    tallies = []
    monkeys = len(operations)

    def calculate(m: int, value: int):
        operation = operations[m]
        match(operation[0]):
            case 0:
                value += operation[1]
            case 1:
                value *= operation[1]
                if(not isPartOne):
                    value = value % lcm
            case 2:
                value = value*value
                if(not isPartOne):
                    value = value % lcm
        return math.floor(value/3) if isPartOne else value
    
    def getNextMonkey(m: int, value: int):
        return redirectors[m][0] if((value % divisors[m]) == 0) else redirectors[m][1]

    for line in utils.readInput('11', isTest):
        queued.append([])
        tallies.append(0)
        for worry in [int(worry) for worry in line.split(',')]:
            queued[-1].append(worry)
    
    for round in range(20 if isPartOne else 10000):
        for m in range(monkeys):
            while(len(queued[m])> 0):
                itemValue = queued[m].pop(0)
                tallies[m]+=1
                endValue = calculate(m, itemValue)
                t = getNextMonkey(m, endValue)
                queued[t].append(endValue)

    print(tallies)
    sortedTallies = sorted(tallies)
    print(f'{sortedTallies[-1]} * {sortedTallies[-2]} = {sortedTallies[-1]*sortedTallies[-2]}')