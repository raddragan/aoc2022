import utils

def dec01(test = False):
    lines = utils.readLines('dec01',test)
    elves = [[]]
    for line in lines:
        match line:
            case '':
                elves.append([])
            case _:
                elves[-1].append(int(line))

    sums = []
    for elf in elves:
        sums.append(sum(elf))
    sums.sort()
    print(f'Top: {sums[-1]}')

    topThree = sums[-3:]
    print(f'Top 3: {sum(topThree)}')