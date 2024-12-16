import re

def mul():
    n = 0
    f = open("input.txt", "r")
    for line in f.readlines():
        pat="mul\(\d+,\d+\)"
        muls = re.findall(pat, line)
        for mul in muls:
            nums = re.findall(r"\d+", mul)
            n += int(nums[0])*int(nums[1])
        print(muls)
    return n

print(mul())