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
      groups.append([r])
    if entryrows > 0:
      groups[index] = groups[index] + [r]
    entryrows += 1

  else:
    index +=1
    entryrows=0

for group in groups:
  groupset = {}
  for idx, person in enumerate(group):
    if idx == 0:
      groupset = set(person)
    else:
      groupset = groupset.intersection(set(person))
  sum = sum + len(groupset)

print sum
#3143 correct
