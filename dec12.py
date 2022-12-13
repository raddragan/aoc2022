import utils
import math


def getNumValue(char: str):
    match(char):
        case 'S':
            return 1
        case 'E':
            return 26
    return utils.strToNum(char)


def run():
    isTest = False

    points = []  # [x][y] = [value,stepsFromStart]
    startAt = []
    endAt = []
    lines = utils.readInput('12', isTest)
    height = len(lines)
    width = len(lines[0])
    for x in range(width):
        row = []
        for y in range(height):
            char = lines[height-(y+1)][x]
            value = getNumValue(char)
            match(char):
                case 'S':
                    startAt = [x,y]
                case 'E':
                    endAt = [x,y]
            row.append(value)
        points.append(row)
    numerOfPoints = height*width
    print(f'loaded {numerOfPoints} points')
    print(f'startAt {startAt}')
    print(f'endAt {endAt}')

    crawledTo = [] #[x][y] = steps
    def initCrawledTo(beginning):
        crawledTo.clear()
        for x in range(width):
            col = [-1 for y in range(height)]
            crawledTo.append(col)
        crawledTo[beginning[0]][beginning[1]] = 0
                
    def getCrawledToAt(coord):
        return crawledTo[coord[0]][coord[1]]

    def advanceCrawler(previousStepsPoints):
        movedToPoints = [] #[[x,y]]
        for previousStep in previousStepsPoints:
            x = previousStep[0]
            y = previousStep[1]
            fromStep = getCrawledToAt(previousStep)
            fromValue = points[x][y]
            neighbors = []
            if (x > 0):
                neighbors.append([x-1, y])
            if (x < (width-1)):
                neighbors.append([x+1, y])
            if (y > 0):
                neighbors.append([x, y-1])
            if (y < (height-1)):
                neighbors.append([x, y+1])
            for neighbor in neighbors:
                if(getCrawledToAt(neighbor) > -1):
                    continue
                toX = neighbor[0]
                toY = neighbor[1]
                toValue = points[toX][toY]
                if (toValue <= (fromValue+1)):
                    crawledTo[toX][toY] = fromStep+1
                    movedToPoints.append(neighbor)
        if(len(movedToPoints)>0):
            advanceCrawler(movedToPoints)

    initCrawledTo(startAt)
    advanceCrawler([startAt])
    crawledToEndAt = getCrawledToAt(endAt)
    print(f'E reached after {crawledToEndAt}')

    shortestStepsFromA = None
    for x in range(width):
        for y in range(height):
            if(points[x][y] != 1):
                continue
            initCrawledTo([x,y])
            advanceCrawler([[x,y]])
            crawledToEndAt = getCrawledToAt(endAt)
            if(crawledToEndAt > 0 and (shortestStepsFromA == None or shortestStepsFromA > crawledToEndAt)):
                shortestStepsFromA = crawledToEndAt
    print(f'from nearest a, E reached after {shortestStepsFromA}')
