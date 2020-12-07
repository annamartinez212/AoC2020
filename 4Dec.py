import ast

with open("4Dec-data.txt", "r") as f:
  rows = f.readlines()

rows = [x.strip() for x in rows]

passports = []
index = 0
prows = 0
valid = 0

for r in rows:
  if r!="":
    if prows ==0:
      passports.append(r)

    if prows > 0:
      passports[index] = passports[index]+" "+r
    prows +=1
  else:
    index +=1
    prows=0


for idx, p in enumerate(passports):
  p = p.replace(" ", "', '").replace(":", "': '")
  passports[idx] = "{'"+p+"'}"
  passports[idx] = ast.literal_eval(passports[idx])

for p in passports:
  if len(p.keys()) == 7 and not p.has_key('cid'):
    valid +=1
  if len(p.keys()) ==8:
    valid +=1

print valid
#200 correct
