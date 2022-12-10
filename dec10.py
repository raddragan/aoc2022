import utils
import re

def run():
    adds = [[0,1]]
    cycle = 0
    for add in [re.match('addx ([-\d]*)', line) for line in utils.readInput('10', False)]:
        if not add:
            cycle += 1
        else:
            cycle += 2
            adds.append([cycle, int(add.group(1))])
    
    total = 0
    for snap in [20,60,100,140,180,220]:
        value = sum([a[1] for a in filter(lambda a: a[0] < snap, adds)])
        total+=value*snap
        print(f'{snap} {value} * {snap} = {value*snap}')
    print(f'total: {total}')
    print('')

    spriteAt = 1
    pixels = []
    for cycle in range (240):
        spriteAt = sum([a[1] for a in filter(lambda a: a[0] <= cycle, adds)])
        position = cycle % 40
        pixel = '#' if(abs(spriteAt-position)<2) else '.'
        pixels.append(pixel)
    for y in range(6):
        pixelsInRow = pixels[y*40:(y+1)*40]
        print(''.join(pixelsInRow))