def reportSafetyCheck(path):
    f = open(path, "r")
    total = 0
    for line in f.readlines():
        numbers = line.split()
        increase = True
        safe = True
        n0 = int(numbers[0])
        n1 = int(numbers[1])
        if n0 > n1:
            increase = False
        for i in range(len(numbers)-1):
            n0 = int(numbers[i])
            n1 = int(numbers[i+1])
            if (increase and n0 > n1) or (not increase and n0 < n1) or (abs(n0-n1) > 3) or (n0-n1 == 0):
                safe = False
                break
        if safe:
            total += 1
    return total


def tolerateASingleBadLevel(path):
    f = open(path, "r")
    total = 0
    for line in f.readlines():
        numbers = line.split()
        if checkNumbers(numbers, False):
            total += 1
    return total


def checkNumbers(numbers, tolerated):
    increase = True
    n0 = int(numbers[0])
    n1 = int(numbers[1])
    if n0 > n1:
        increase = False
    for i in range(len(numbers)-1):
        n0 = int(numbers[i])
        n1 = int(numbers[i+1])
        if (increase and n0 > n1) or (not increase and n0 < n1) or (abs(n0-n1) > 3) or (n0-n1 == 0):
            if not tolerated:
                for j in range(len(numbers)):
                    numbersPoped = numbers.copy()
                    numbersPoped.pop(j)
                    if checkNumbers(numbersPoped, True):
                        return True
                return False
            return False
    return True
    

print(reportSafetyCheck("input02.txt"))
print(tolerateASingleBadLevel("input02.txt"))