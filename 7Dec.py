with open("7Dec-data.txt", "r") as f:
  rows = f.readlines()

rows = [x.strip() for x in rows]

mycolour = " shiny gold"


def bags(mycolour):
  colours = []
  for r in rows:
    if mycolour in r:
      idx = r.rindex(mycolour)
      r = r[:idx:]
      splitted = r.split()
      for idx, word in enumerate(splitted):
        if word == "bag" or word == "bags":
          colours.append(splitted[idx-2]+" "+splitted[idx-1])
  for c in colours:
    colours = colours+bags(c)

  return colours


print(len(set(bags(mycolour))))
#142 is correct
