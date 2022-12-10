# from typing import Dict
# from unittest import case
# from toolz.dicttoolz import valmap
#
# from Tools.scripts.make_ctype import values
#
assignments = []
with open("C:/Users/elian/pythonProject4/venv/Scripts/data.txt", "r")  as input:
    for line in input:
        line = line.strip()
        assignments.append(line.split(','))

contains = 0
for pair in assignments:
    elf1, elf2 = pair[0], pair[-1]
    start1, end1 = elf1.split('-')
    start2, end2 = elf2.split('-')

    # cast to integer
    start1 = int(start1)
    start2 = int(start2)
    end1 = int(end1)
    end2 = int(end2)

    # check if elf 1's range contains elf 2's range
    if (start1 <= start2 and end1 >= start2):
        contains = contains + 1
    # check if elf 2's range contains elf 1's range
    elif (start2 <= start1 and end2 >= start1):
        contains = contains + 1


print(contains)

#failed attempt #1
# t = 0
# for line in open(0):
#     a, b = line.split(",")
#     ar = [i for i in range(int(a.split('-')[0]), int(a.split('-')[1])+1)]
#     br = [i for i in range(int(b.split('-')[0]), int(b.split('-')[1])+1)]
#     if all(item in ar for item in br) or all(item in br for item in ar):
#         t += 1
#failed attempt #2
# print(t)
# for line in open(0):
#     a, b = line.split(",")
#     ar = [i for i in range(int(a.split('-')[0]), int(a.split('-')[1])+1)]
#     br = [i for i in range(int(b.split('-')[0]), int(b.split('-')[1])+1)]
#     if set(ar) & set(br):
#         t += 1
#
# print(t)

