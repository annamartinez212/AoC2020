with open("8Dec-data.txt", "r") as f:
  rows = f.readlines()

rows = [x.strip() for x in rows]
ACC = 0
INDEX = 0
INDICES = {0}


def iterate(rows):
  global ACC
  global INDEX
  while INDEX < len(rows):
    if rows[INDEX].startswith("acc"):
      if INDEX !=0 and INDEX+1 in INDICES:
        return ACC
      ACC = ACC + int(rows[INDEX].strip("acc "))
      INDEX += 1
      INDICES.add(INDEX)
      continue
    if rows[INDEX].startswith("jmp"):
      INDEX = INDEX + int(rows[INDEX].strip("jmp "))
      INDICES.add(INDEX)
      continue
    if rows[INDEX].startswith("nop"):
      INDEX += 1
      INDICES.add(INDEX)
      continue

print(iterate(rows))

# 1394 right
# index =622 means terminated
