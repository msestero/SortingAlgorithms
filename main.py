import random

def getRandomList(numElements):
    randList = []
    for i in range(0, numElements):
        randList.append(random.randint(0, 100))
    return randList

def quick(list):
    if len(list) <= 1:
        return list
    pivot = list[0]
    left = []
    right = []
    for element in list[1:]:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)
    return quick(left) + [pivot] + quick(right)

def bubble(list):
    noSwaps = True
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]
            noSwaps = False
    if noSwaps:
        return list
    return bubble(list)

def merge(list):
    if len(list) <= 1:
        return list
    midPoint = len(list) // 2
    left = merge(list[:midPoint])
    right = merge(list[midPoint:])
    sorted = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            sorted.append(left.pop(0))
        else:
            sorted.append(right.pop(0))
    if len(left) != 0:
        sorted += left
    else:
        sorted += right
    return sorted

def insertion(list):
    if len(list) <= 1:
        return list
    sorted = []
    if list[0] < list[1]:
        sorted.append(list[0])
        return insertion(sorted) + insertion(list[1:])
    sorted.append(list[1])
    return insertion(sorted) + insertion([list[0]] + list[2:])


def selection(list):
    if list is None or len(list) <= 1:
        return list
    lowest = list[0]
    for ele in list[1:]:
        if ele < lowest:
            lowest = ele
    list.remove(lowest)
    return [lowest] + selection(list)

if __name__ == "__main__":
    numElements = int(input("how many elements: "))
    randList = getRandomList(numElements)
    print("Random List: " + str(randList))
    print("Quick Sort: " + str(quick(randList)))
    print("Bubble Sort: " + str(bubble(randList)))
    print("Merge Sort: " + str(merge(randList)))
    print("Insertion Sort: " + str(insertion(randList)))
    print("Selection Sort: " + str(selection(randList)))
