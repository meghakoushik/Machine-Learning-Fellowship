#program to find the maximum and minimum numbers from a sequence of numbers.


#For maximum number
def maxNumber(l):
    Max = l[0]
    for num in l:
        if Max < num:
            Max = num
    return Max


print(maxNumber([17, 4, 15, 1, 2, 9]))


#for minimum number
def minNumber(l):
    Min = l[0]
    for num in l:
        if Min > num:
            Min = num
    return Min


print(minNumber([17, 4, 15, 1, 2, 9]))

