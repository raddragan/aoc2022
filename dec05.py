import utils

def parseInstruction(st:str):
    n = st.split();
    return[int(i) for i in [n[1],n[3],n[5]]]

def run1():
    isTest = False
    stacks = [list(line) for line in utils.readInput('5_1',isTest)]
    instructions = [parseInstruction(line) for line in utils.readInput('5_2',isTest)]

    for move in instructions:
        for c in range(move[0]):
            stacks[move[2]-1].insert(0,stacks[move[1]-1].pop(0))
    
    topOfStacks = [s[0] for s in stacks]
    print("".join(topOfStacks))

def run2():
    isTest = False
    stacks = [list(line) for line in utils.readInput('5_1',isTest)]
    instructions = [parseInstruction(line) for line in utils.readInput('5_2',isTest)]

    for move in instructions:
        a = move[1]-1
        b = move[2]-1
        c = move[0]
        take = stacks[a][0:c]
        stacks[a] = stacks[a][c:]
        stacks[b] = take + stacks[b]
    
    topOfStacks = [s[0] for s in stacks]
    print("".join(topOfStacks))

def run():
    run2()