import utils

def instructionsToArr(str: str):
    return [int(x) for x in str.replace("A","1").replace("B","2").replace("C","3").replace("X","1").replace("Y","2").replace("Z","3").split(" ")]

def calcWlt(arr:list[int]):
    if(arr[0] == arr[1]):
        return 3
    match(arr[0]):
        case 3:
            match(arr[1]):
                case 1:
                    return 6
                case 2:
                    return 0
        case _:
            if(arr[1] == (arr[0] + 1)):
                return 6
            else:
                return 0

def calcScore(arr:list[int]):
    return calcWlt(arr) + arr[1]

def playToWin(opp:int):
    match(opp):
        case 3:
            return 1
        case _:
            return opp+1

def playToLose(opp:int):
    match(opp):
        case 1:
            return 3
        case _:
            return opp-1

def calcStrategyScore(arr:list[int]):
    match(arr[1]):
        case 1:
            return playToLose(arr[0])
        case 2:
            return arr[0] + 3
        case 3:
            return playToWin(arr[0]) + 6

def dec02():
    instructions = [instructionsToArr(s) for s in utils.readInput(2,False)]
    scores = [calcScore(i) for i in instructions]
    print(sum(scores))

    strategies = [calcStrategyScore(i) for i in instructions]
    print(sum(strategies))