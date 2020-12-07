import math

with open("5Dec-data.txt", "r") as f:
  binary = f.readlines()

binary = [x.strip() for x in binary]


def rowcount(bin):
  for idx, bi in enumerate(binary[0]):
    if bi not in ["F", "B"]:
      return pow(2, idx)

def findseat(ids):
  ids.sort()
  for idx, id in enumerate(ids):
    if idx+1 < len(ids):
      if id+1 not in ids and ids[idx+1]==id+2:
        return id+1


def seats():
  rows = rowcount(binary[0])
  log2 = int(math.log(rows, 2))
  cols = pow(2, len(binary[0]) - log2)
  ids = []

  for b in binary:
    lowerR = 0
    upperR = rows
    lowerC = 0
    upperC = cols
    for idx, r in enumerate(b):
      if idx < log2: # 7 = log2 (128)
        if r == "F":
          upperR = lowerR + rows/pow(2, idx+1)
        if r == "B":
          lowerR = lowerR + rows/pow(2, idx+1)
      row = lowerR

      if idx >= log2: # or just else:
        if r == "L":
          upperC = lowerC + cols/pow(2, idx+1-log2)
        if r == "R":
          lowerC = lowerC + cols/pow(2, idx+1-log2)
      col = lowerC
    ids.append(row*8 + col)
  return max(ids), findseat(ids)

# 888 correct
# 522 correct

print(seats())
