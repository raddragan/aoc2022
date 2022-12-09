import utils
import re

def doRun(segments: int, isTest : bool):
    segmentsAt = [[0, 0] for h in range(segments)]
    history = [[0, 0]]

    def ensureHistory():
        tailAt = segmentsAt[-1]
        if(not (tailAt in history)):
            history.append(tailAt.copy())

    def segmentMoved(s: int):
        if(s == (segments - 1)):
            return
        headAt = segmentsAt[s]
        tailAt = segmentsAt[s+1]
        xDelta = headAt[0]-tailAt[0]
        xDeltaAbs = abs(xDelta)
        yDelta = headAt[1]-tailAt[1]
        yDeltaAbs = abs(yDelta)

        if(xDeltaAbs > 1 and yDeltaAbs > 1):
            # it appears that it now moves 1 and 1 towards the head
            tailAt[0] = tailAt[0]+(1 if xDelta > 0 else -1)
            tailAt[1] = tailAt[1]+(1 if yDelta > 0 else -1)
            segmentMoved(s+1)
        else:
            a = 0 if (xDeltaAbs > 1) else 1
            aDelta = xDelta if (a == 0) else yDelta
            b = abs(1-a)

            if(abs(aDelta) < 2):
                return

            tailAt[a] = tailAt[a]+(1 if aDelta > 0 else -1)
            if(headAt[a] != tailAt[a] and headAt[b] != tailAt[b]):
                tailAt[b] = headAt[b]
            segmentMoved(s+1)
    
    def printSegments():
        for i in range(len(segmentsAt)):
            char = 'H' if i == 0 else i
            print(f'  {char}:{segmentsAt[i]}')
        print('')
    
    def printGrid():
        xRange = [0,0]
        yRange = [0,0]
        for segmentAt in segmentsAt:
            if(xRange[0] > segmentAt[0]):
                xRange[0] = segmentAt[0]
            elif(xRange[1] < segmentAt[0]):
                xRange[1] = segmentAt[0]
            if(yRange[0] > segmentAt[1]):
                yRange[0] = segmentAt[1]
            elif(yRange[1] < segmentAt[1]):
                yRange[1] = segmentAt[1]
        for y in range(yRange[1],yRange[0]-1,-1):
            line = [f'{y}:']
            for x in range(xRange[0],xRange[1]+1):
                here = [x,y]
                found = False
                for iSegment in range(segments):
                    if(segmentsAt[iSegment] == here):
                        line.append('H' if iSegment == 0 else f'{iSegment}')
                        found = True
                        break
                if(not found):
                    line.append('.')
            print(''.join(line))
        print('')


    for dirs in [re.match('(\w) (\d*)', line) for line in utils.readInput('9', isTest)]:
        dir = dirs.group(1)
        move = 1 if (dir in ['R', 'U']) else -1
        print(f'== {dir} {dirs.group(2)} ==')
        for i in range(int(dirs.group(2))):
            a = 0 if(dir in ['L', 'R']) else 1
            segmentsAt[0][a] = segmentsAt[0][a] + move
            segmentMoved(0)
            ensureHistory()
            #printSegments()
            #printGrid()
    print(f'{segments} segments; {len(history)} positions')

def run():
    doRun(10,False)