with open("6Dec-data.txt", "r") as f:
  rows = f.readlines()

rows = [x.strip() for x in rows]

groups = []
entryrows = 0
index = 0
sum = 0

for r in rows:
  if r!="":
    if entryrows == 0:
      groups.append(r)
    if entryrows > 0:
      groups[index] = groups[index] + r
    entryrows += 1

  else:
    index +=1
    entryrows=0


for g in groups:
  sum = sum + len(set(g))

print sum
#6351
