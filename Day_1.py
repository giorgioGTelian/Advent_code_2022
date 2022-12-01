AoC-22 - Day 1: Calorie Counting
#
s$ = input
while s$ <> ""
   sum = 0
   while s$ <> ""
      sum += number s$
      s$ = input
   
   ar[] &= sum
   s$ = input

sum = 0
for k = 1 to 3
   max = 0
   for i = 1 to len ar[]
      if ar[i] > max
         max = ar[i]
         maxi = i
      
   
   if k = 1
      print max
   
   sum += max
   ar[maxi] = 0

print(sum)

// second part

with open("C:/Users/elian/pythonProject4/venv/Scripts/data.txt", "r") as f:
    data = [row.strip() for row in f.readlines()]

calories = [sum(map(int, row.split(" "))) for row in " ".join(data).split("  ")]
print(max(calories))
print(sum(sorted(calories, reverse=True)[:3]))
