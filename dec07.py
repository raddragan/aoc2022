import utils
import os
import re

def getTotalSize(dirName: str, dirs: list[list[str,int]]):
    size = 0
    for d in [d for d in dirs if d[0].startswith(dirName)]:
        size += d[1]
    return size

def run():
    isTest = False
    dirs = []

    ignoreLs = False
    currentDir = ''
    currentDirIndex = -1
    for line in utils.readInput(7,isTest):
        matchCd = re.match('^\$ cd (.*)', line)
        matchLs = re.match('^\$ ls', line)
        if(matchCd):
            dirName = matchCd.group(1).replace('/','\\')
            currentDir = ''.join(os.path.normpath(os.path.join(currentDir, dirName)))
            print(currentDir)
        elif(matchLs):
            ignoreLs = len([d for d in dirs if d[0] == currentDir]) > 0
            if(not ignoreLs):
                currentDirIndex = len(dirs)
                dirs.append([currentDir, 0])
        elif(not ignoreLs):
            matchFile = re.match('^(\d*) .*', line)
            if(matchFile):
                dirs[currentDirIndex][1] = dirs[currentDirIndex][1] + int(matchFile.group(1))

    dirsWithSubs = [[dir[0], getTotalSize(dir[0],dirs)] for dir in dirs]

    partOneTotal = 0
    for dir in [dir for dir in dirsWithSubs if dir[1] <= 100000]:
        partOneTotal += dir[1]
    
    print(f'partOneTotal: {partOneTotal}')

    usedSpace = dirsWithSubs[0][1]
    freeSpace = 70000000 - usedSpace
    freeUp = 30000000 - freeSpace
    print(freeUp)

    partTwoDirs = [dir for dir in dirsWithSubs if dir[1] >= freeUp]
    smallestDirToDelete = sorted(partTwoDirs, key=lambda d: d[1])[0]
    print(f'smallestDirToDelete {smallestDirToDelete}')