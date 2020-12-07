with open("2Dec-data.txt", "r") as f:
  policies = f.readlines()

policies = [x.replace(":", "").replace("-", " ").strip().split(" ") for x in policies]

# print (len(policies))

validCounter = 0
for p in policies:
  if p[3].count(p[2]) < int(p[0]) or p[3].count(p[2]) > int(p[1]):
    validCounter += 1
    print p, p[3].count(p[2]), int(p[0])

print (1000-validCounter)
