import utils
import re

def run():
    isTest = False

    sensors = [] #[[x,y],[bx,by],range]
    for line in utils.readInput('15', isTest):
        coords = re.findall('[-\d]+',line)
        sensor = [int(coords[0]),int(coords[1])]
        beacon = [int(coords[2]),int(coords[3])]
        sensors.append([sensor,beacon,abs(sensor[0]-beacon[0])+abs(sensor[1]-beacon[1])])

    def checkRow(checkRowAt: int, isPartTwo: bool):
        beaconsAt = [] #x[]
        notInRanges = [] #[[minX,maxX]]

        def removeBeacons():
            for b in beaconsAt:
                i = -1
                for r in notInRanges:
                    i+=1
                    if(r[0]<=b<=r[1]):
                        if(r[0] == r[1]):
                            notInRanges.pop(i)
                        elif(r[0] == b):
                            r[0]=r[0]+1
                        elif(r[1] == b):
                            r[1]=r[1]-1
                        else:
                            endsAt = r[1]
                            r[1]=b-1
                            notInRanges.append([b+1,endsAt])
                        notInRanges.sort(key=lambda r: r[1])
                        notInRanges.sort(key=lambda r: r[0])
                        break

        def combineRanges():
            for i in range(len(notInRanges)-1):
                rangeA = notInRanges[i]
                rangeB = notInRanges[i+1]
                if(rangeA[1]>=rangeB[0]):
                    if(rangeB[1] > rangeA[1]):
                        rangeA[1] = rangeB[1]
                    notInRanges.pop(i+1)
                    combineRanges()
                    break

        for sensor in sensors:
            if(sensor[1][1] == checkRowAt):
                beaconsAt.append(sensor[1][0])
            yDelta = abs(checkRowAt - sensor[0][1])
            xRange = sensor[2] - yDelta
            if(xRange >= 0):
                notInRanges.append([sensor[0][0]-xRange,sensor[0][0]+xRange])
        
        notInRanges.sort(key=lambda r: r[1])
        notInRanges.sort(key=lambda r: r[0])

        combineRanges()
        
        if(isPartTwo):        
            if(len(notInRanges)>1):
                return [notInRanges[0][1]+1,checkRowAt]
            return None

        removeBeacons()
        sum = 0
        for r in notInRanges:
            sum+=((r[1]+1)-r[0])
        print(f'part1 sum: {sum}')
    
    checkRow(10 if isTest else 2000000, False)

    for i in range(4000000,-1,-1):
        result = checkRow(i, True)
        if(result != None):
            print(f'part2: {result[0]} * 4000000 + {result[1]} = {(result[0]*4000000)+result[1]}')
            break