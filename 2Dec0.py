with open("2Dec-data.txt", "r") as f:
  policies = f.readlines()

policies = [x.replace(":", "").replace("-", " ").strip().split(" ") for x in policies]


def passwords(policies):
  validCounter = 0
  for p in policies:
    if (p[3][int(p[0])-1] == p[2] or p[3][int(p[1])-1] == p[2]) and p[3][int(p[0])-1] != p[3][int(p[1])-1]:

        validCounter += 1
  return validCounter

print passwords(policies)
#688
