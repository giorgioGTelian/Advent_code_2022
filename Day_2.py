# from typing import Dict
# from unittest import case
# from toolz.dicttoolz import valmap
#
from Tools.scripts.make_ctype import values
#
with open("C:/Users/elian/pythonProject4/venv/Scripts/data.txt", "r") as f:
  data = [line.strip() for line in f.readlines()]
#
# # rules: dict[int, str] = {
# #     1: "A X",
# #     2: "A Y",
# #     3: "A Z",
# #     4: "B X",
# #     5: "B Y",
# #     6: "B Z",
# #     7: "C X",
# #     8: "C Y",
# #     9: "C Z"
# # }
# # print(rules.values())
# #
#
rules = "A X,A Y,A Z,B X,B Y,B Z,C X,C Y,C Z"
player_one_score=[]
player_two_score=[]
for line in data:

     index = rules.split(",")
    
    print(index)

     for index[0] in "A X":
         player_one_score.append(3)
         player_two_score.append(1)
         break
     for index[1] in "A Y":
         player_one_score.append(6)
         player_two_score.append(2)
         break
     for index[2] in "A Z":
         player_one_score.append(0)
         player_two_score.append(3)
        break
         # : 0 + 1
     for index[3] in "B X":
         player_one_score.append(0)
         player_two_score.append(1)
         break
         # : 3 + 2
     for index[4] in "B Y":
         player_one_score.append(3)
         player_two_score.append(2)
         break
         # : 6 + 3
     for index[5] in "B Z":
         player_one_score.append(6)
         player_two_score.append(3)
         break
#         # : 6 + 1
     for index[6] in "C X":
         player_one_score.append(6)
         player_two_score.append(1)
         break
        # : 0 + 2
     for index[7] in "C Y":
         player_one_score.append(0)
         player_two_score.append(2)
         break
         # : 3 + 3
     for index[8] in "C Z":
         player_one_score.append(3)
#         player_two_score.append(3)
        break

print(player_one_score)
print(player_two_score)
print(sum(player_one_score))
print(sum(player_two_score))
sum(player_two_score.values())

#
#

with open("C:/Users/elian/pythonProject4/venv/Scripts/data.txt") as f:
    guide = f.read().splitlines()
scores = {
    "A X" : 3 + 1,
    "A Y" : 6 + 2,
    "A Z" : 0 + 3,
    "B X" : 0 + 1,
    "B Y" : 3 + 2,
    "B Z" : 6 + 3,
    "C X" : 6 + 1,
    "C Y" : 0 + 2,
    "C Z" : 3 + 3
}

score = 0
for line in guide:
    score += scores[line]

print("Day 2 Part 1 = " + str(score))

scores = {
    "A X" : 0 + 3,
    "A Y" : 3 + 1,
    "A Z" : 6 + 2,
    "B X" : 0 + 1,
    "B Y" : 3 + 2,
    "B Z" : 6 + 3,
    "C X" : 0 + 2,
    "C Y" : 3 + 3,
    "C Z" : 6 + 1
}

score = 0
for line in guide:
    score += scores[line]

print("Day 2 Part 2 = " + str(score))
