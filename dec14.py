import utils

def parseCoords(str: str):
    return [int(s) for s in str.split(',')]

def run():
    isTest = False
    isPartTwo = True

    xSteps: list[list[int]] = [] #[x,fromY,toY]
    ySteps: list[list[int]] = [] #[y,fromX,toX]
    for line in utils.readInput('14', isTest):
        steps = line.split(' -> ')
        for i in range(len(steps)-1):
            a = parseCoords(steps[i])
            b = parseCoords(steps[i+1])
            if(a[0] == b[0]):
                if(b[1] > a[1]):
                    xSteps.append([a[0],a[1],b[1]])
                else:
                    xSteps.append([a[0],b[1],a[1]])
            else:
                if(b[0] > a[0]):
                    ySteps.append([a[1], a[0], b[0]])
                else:
                    ySteps.append([a[1], b[0], a[0]])
    xSteps.sort(key=lambda s: s[1])
    xSteps.sort(key=lambda s: s[0])
    ySteps.sort(key=lambda s: s[1])
    ySteps.sort(key=lambda s: s[0])
    
    xRanges: list[list[int]] = [] #[x,minY,maxY]
    for xStep in xSteps:
        x,minY,maxY = xStep
        found = False
        for xRange in xRanges:
            if(xRange[0] == x):
                found = True
                if(xRange[1] > minY):
                    xRange[1] = minY
                if(xRange[2] < maxY):
                    xRange[2] = maxY
                break
        if(not found):
            xRanges.append(xStep.copy())
    for yStep in ySteps:
        y,minX,maxX = yStep
        for x in range(minX, maxX+1):
            found = False
            for xRange in xRanges:
                if(xRange[0] == x):
                    found = True
                    if(xRange[1] > y):
                        xRange[1] = y
                    if(xRange[2] < y):
                        xRange[2] = y
                    break
            if(not found):
                xRanges.append([x,y,y])
    xRanges.sort(key=lambda r: r[0])
    minX = xRanges[0][0]
    maxX = xRanges[-1][0]
    minY = min([r[1] for r in xRanges])
    maxY = max([r[2] for r in xRanges])
    floor = maxY + 2
    
    def findYStepsAlongX(x:int):
        results: list[list[int]] = []
        for xStep in xSteps:
            if(xStep[0] > x):
                break
            if(xStep[0] == x):
                results.append(xStep[1:])
        return results
    
    def findXStepsAlongY(y:int):
        results: list[int] = []
        for yStep in ySteps:
            if(yStep[0] > y):
                break
            if(yStep[0] == y):
                results.append(yStep[1:])
        return results

    def findXRange(x: int):
        for xRange in xRanges:
            if(xRange[0] > x):
                return None
            if(xRange[0] == x):
                return xRange[1:]

    def isOutOfBounds(xy: list[int]):
        if(isPartTwo):
            return False
        x,y = xy
        if(x<minX or x>maxX):
            return True
        xRange = findXRange(x)
        return xRange == None or y > xRange[1]
    
    sandsAt: list[list[int]] = [] #[x,y][]

    def isOccupied(xy:list[int]):
        if(isOutOfBounds(xy)):
            return False
        
        if(xy in sandsAt):
            return True

        x,y = xy
        for ys in findYStepsAlongX(x):
            minY,maxY = ys
            if(minY<=y<=maxY):
                return True

        for xs in findXStepsAlongY(y):
            minX,maxX = xs
            if(minX<=x<=maxX):
                return True
        
        if(isPartTwo and y==floor):
            return True

        return False

    def dropTo(xy: list[int]):
        x,y = xy
        if(isOutOfBounds(xy)):
            return None # Disappeared into the abyss

        down = [x,y+1]
        if(isOccupied(down)): #Hit something
            toTheLeft = [x-1,y+1]
            toTheRight = [x+1,y+1]
            if(not isOccupied(toTheLeft)):
                return dropTo(toTheLeft)
            elif(not isOccupied(toTheRight)):
                return dropTo(toTheRight)
            return xy #comes to rest
        
        return dropTo(down)
    
    while(True):
        restingPlace = dropTo([500,0])
        if(restingPlace != None):
            sandsAt.append(restingPlace)
            if(restingPlace == [500,0]):
                break
        else:
            break
    print(f'units of sand come to rest: {len(sandsAt)}')

    # sandsAt.sort(key=lambda s: s[1])
    # sandsAt.sort(key=lambda s: s[0])
    # for sandAt in sandsAt:
    #     print(sandAt)

    for y in range(maxY+1):
        line = []
        for x in range(minX, maxX+1):
            if([x,y] == [500,1]):
                line.append('*')
            elif([x,y] in sandsAt):
                line.append('o')
            elif(isOccupied([x,y])):
                line.append('#')
            else:
                line.append('.')
        print(''.join(line))
            