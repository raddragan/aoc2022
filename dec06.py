import utils

def parseInstruction(st:str):
    n = st.split();
    return[int(i) for i in [n[1],n[3],n[5]]]

def process(chars: list[str], target: int):
    for i in range(target-1,len(chars)):
        section = chars[i-target:i]
        if(len(utils.unique(section)) == target):
            print(f'Target {target}: {"".join(section)} starts at {i}')
            break

def run():
    isTest = False
    chars = list(utils.readInput(6,isTest)[0])

    process(chars,4)
    process(chars,14)