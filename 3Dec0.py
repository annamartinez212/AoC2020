with open("3Dec-data.txt", "r") as f:
  rows = f.readlines()

rows = [x.strip() for x in rows]


def trees(right, down):
  trees = 0
  position = 0
  downcounter = down
  for r in rows:
    if downcounter == down:
      if r[position] == "#":
        trees +=1
      if position + right > len(r) -1:
        position = position - (len(r) - right)
      else:
        position = position + right
      downcounter = 1
    else:
      downcounter +=1
      continue
  return trees
# 75, 76, 84, 179, 85, 94 correct is 218
# 43 is last

print trees(1,1)*trees(3,1)* trees(5,1)* trees(7,1)* trees(1,2)
