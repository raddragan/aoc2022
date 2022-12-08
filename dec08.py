import utils

def getScore(myHeight: int, directions: list[list[int]]):
    score = 1
    for dir in directions:
        dirScore = 0
        for t in dir:
            dirScore += 1
            if(t >= myHeight):
                break
        score = score * dirScore
        if(score == 0):
            break
    return score

def run():
    isTest = False
    treesByRow = []
    for line in utils.readInput(8,isTest):
        treesByRow.append([int(tree) for tree in line])
    
    width = len(treesByRow[0])
    height = len(treesByRow)

    treesByCol = []
    for x in range(width):
        col = []
        for y in range(height):
            col.append(treesByRow[y][x])
        treesByCol.append(col)

    totalVisible = 0
    maxScore = 0
    for x in range(width):
        for y in range(height):
            myHeight = treesByRow[y][x]
            toLeft = list(reversed(treesByRow[y][0:x]))
            toRight = treesByRow[y][x+1:]
            toUp = list(reversed(treesByCol[x][0:y]))
            toDown = treesByCol[x][y+1:]
            directions = [toLeft, toRight, toUp, toDown]
            if len([d for d in directions if len([t for t in d if t >= myHeight]) == 0]) > 0:
                totalVisible += 1
            myScore = getScore(myHeight, directions)
            if(myScore > maxScore):
                maxScore = myScore
            
    print(f'totalVisible: {totalVisible}')
    print(f'maxScore: {maxScore}')

