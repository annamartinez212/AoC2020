import ast

with open("4Dec-data.txt", "r") as f:
  rows = f.readlines()

rows = [x.strip() for x in rows]

passports = []
index = 0
prows = 0


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

def validateYr(yr, min, max):
  if int(yr) >=min and int(yr)<=max:
    return True

def validateHgt(hgt):
  if hgt.endswith("in"):
    if int(hgt.strip("in")) >= 59 and  int(hgt.strip("in")) <=76:
      return True
  if hgt.endswith("cm"):
    if int(hgt.strip("cm")) >= 150 and int(hgt.strip("cm"))  <= 193:
      return True
  return False

def validateHair(hcl):
  if hcl.startswith("#") and len(hcl) == 7:
    hcl = hcl.strip("#")
    for h in hcl:
      if ord(h) in range(48,58) or ord(h) in range(97,103):
        return True
    return False
  return False

def validateEye(ecl):
  colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
  if ecl in colours:
    return True
  return False

def validatePid(pid):
  if len(pid) ==9 and pid.isdigit():
    return True
  return False

def validator(passports):
  valid = 0
  for p in passports:
    if (len(p.keys()) == 7 and not p.has_key('cid')) or len(p.keys()) ==8:
      if validateYr(p["byr"], 1920, 2002) and validateYr(p["iyr"], 2010, 2020) and validateYr(p["eyr"], 2020, 2030) and validateHgt(p["hgt"]) and validateHair(p["hcl"]) and validateEye(p["ecl"]) and validatePid(p["pid"]):
        valid +=1
  return valid

print(validator(passports))
# 116
