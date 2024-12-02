#https://adventofcode.com/2024/day/1
def loadInput(path):
    listA = []
    listB = []
    f = open(path, "r")
    for line in f.readlines():
        numbers = line.split()
        listA.append(int(numbers[0]))
        listB.append(int(numbers[1]))
    return listA, listB

def distanceBetweenLists(listA, listB):
    totalDistance = 0
    for i in range(len(listA)):
        minA = min(listA)
        minB = min(listB)
        totalDistance += abs(minA - minB)
        listA.remove(minA)
        listB.remove(minB)
    return totalDistance

listA, listB = loadInput("input01.txt")
print(distanceBetweenLists(listA, listB))