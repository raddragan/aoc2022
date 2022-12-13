import utils
import collections.abc
import math

#1 == left; -1 = right
def compareInts(l,r):
    if l < r:
        return 1
    if l > r:
        return -1
    return 0

#1 == left; -1 = right
def compareArrays(larr, rarr):
    for i in range(len(larr)):
        l = larr[i]
        lIsArray = isinstance(l, collections.abc.Sequence)
        if(len(rarr) <= i):
            return -1
        r = rarr[i]
        rIsArray = isinstance(r, collections.abc.Sequence)

        if(lIsArray):
            if(rIsArray):
                result = compareArrays(l, r)
                if(result != 0):
                    return result
            elif(not rIsArray):
                result = compareArrays(l, [r])
                if(result != 0):
                    return result
        elif(rIsArray):
            result = compareArrays([l], r)
            if(result != 0):
                return result
        else:
            result = compareInts(l,r)
            if(result != 0):
                return result

    if(len(rarr) > len(larr)):
        return 1
    return 0

def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if compareArrays(arr[j],arr[j+1]) == -1:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return

def run():
    isTest = False

    packets = []
    for line in utils.readInput('13', isTest):
        if(len(line) > 0):
            packets.append(eval(line))
    
    step1Sum = 0
    for i in range(math.floor((len(packets)-1)/2)):
        result = compareArrays(packets[i*2],packets[(i*2)+1])
        if(result == 1):
            step1Sum += (i+1)
    print(f'step1Sum: {step1Sum}')
    
    packets.append([[2]])
    packets.append([[6]])
    bubbleSort(packets)

    indexOfTwo = -1
    indexOfSix = -1
    for i in range(len(packets)):
        packet = packets[i]
        if(indexOfTwo == -1 and len(packet) == 1 and packet[0] == [2]):
            indexOfTwo = i+1
        elif(indexOfSix == -1 and len(packet) == 1 and packet[0] == [6]):
            indexOfSix = i+1
    
    print(f'decoderKey = {indexOfTwo}*{indexOfSix}={indexOfTwo*indexOfSix}')