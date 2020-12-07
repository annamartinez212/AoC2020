with open("3Dec-data.txt", "r") as f:
  rows = f.readlines()

rows = [x.strip() for x in rows]

#params
right = 3
down = 1


trees = 0
position = 0
downcounter = 0

for r in rows:
  if r[position] == "#":
    trees +=1
    r = r+ "X" + str(position)

  # print position, r[position]
  if position + right > len(r) -1:
    position = position - (len(r) - right)
  else:
    position = position + right

print trees
# 75, 76, 84, 179, 85, 94 correct is 218
