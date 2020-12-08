with open("8Dec-data.txt", "r") as f:
  rows = f.readlines()

rows = [x.strip() for x in rows]
ACC = 0
INDEX = 0
INDICES = {0}


def iterate(rows):
  global ACC
  global INDEX
  while INDEX <= len(rows):
    if rows[INDEX].startswith("acc"):
      if INDEX == len(rows)-1:
        return ACC + int(rows[INDEX].strip("acc "))
      if INDEX !=0 and INDEX+1 in INDICES:
        return False
      ACC = ACC + int(rows[INDEX].strip("acc "))
      INDEX += 1
      if INDEX == len(rows):
        return ACC
      INDICES.add(INDEX)
      continue
    if rows[INDEX].startswith("jmp"):
      if INDEX == len(rows)-1:
        return ACC
      INDEX = INDEX + int(rows[INDEX].strip("jmp "))
      if INDEX == len(rows):
        return ACC
      if INDEX in INDICES:
        return False
      INDICES.add(INDEX)
      continue
    if rows[INDEX].startswith("nop"):
      if INDEX == len(rows)-1:
        return ACC
      INDEX += 1
      if INDEX == len(rows):
        return ACC
      if INDEX in INDICES:
        return False
      INDICES.add(INDEX)
      continue


# 1626, but if I turn the 2 loops around I also get 782 - probably wrong
for idx, r in enumerate(rows):
  if r.startswith("nop"):
    INDEX = 0
    ACC = 0
    INDICES = {0}
    rows[idx] = r.replace("nop", "jmp")
    result = iterate(rows)

    if result:
      print result #, idx
      break
    else:
      rows[idx] = r.replace("jmp", "nop")

for idx, r in enumerate(rows):
  if r.startswith("jmp"):
    rows[idx] = r.replace("jmp", "nop")
    INDEX = 0
    ACC = 0
    INDICES = {0}
    result = iterate(rows)

    if result:
      print result #, idx
      break
    else:
      rows[idx] = r.replace("nop", "jmp")
