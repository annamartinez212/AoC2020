with open("11Dec-data.txt", "r") as f:
  layout = f.readlines()

layout = [x.strip() for x in layout]

endOfRow = len(layout[0]) -1

seats = []

for r in layout:
  for s in r:
    seats.append(s)
dirs = {}
dirs['north'] = -len(layout[0])
dirs['south'] = len(layout[0])
dirs['east'] = 1
dirs['west'] = -1
dirs['ne'] = dirs['north'] + dirs['east']
dirs['se'] = dirs['south'] + dirs['east']
dirs['sw'] = dirs['south'] + dirs['west']
dirs['nw'] =  dirs['north'] + dirs['west']

def getNeighbours(i, seats):
  neighbours = []
  for key in dirs:
    pos = i
    while pos in range (len(seats)):
      if pos == 0:
          if key in ["north", "ne", "nw", "w", "sw"]:
            break
          if i!= pos:
            neighbours.append(pos)
            break
      elif pos < len(layout[0])-1 and key in ["north", "ne", "nw"]: # 1st row
        if i!= pos:
          neighbours.append(pos)
        break
      elif pos == len(layout[0])-1 and key in ["north", "ne", "nw", "e", "se"]: # top right
        if i!= pos:
          neighbours.append(pos)
        break
      elif pos % (len(layout[0])) == 0 and key in ["west", "sw", "nw"]: #left edge
        if i!= pos:
          neighbours.append(pos)
        break
      elif (pos+1) % (len(layout[0])) == 0 and key in ["east", "se", "ne"]:# right edge
        if i!= pos:
          neighbours.append(pos)
        break
      elif pos ==len(layout[0])*len(layout) - len(layout[0]) and key in ["south", "sw", "se", "w", "nw"]: #bottom left
        if i!= pos:
          neighbours.append(pos)
        break
      elif pos == (len(layout[0]))*(len(layout))-1 and key in ["south", "sw", "se", "east", "ne"]: # bottom right
        if i!= pos:
          neighbours.append(pos)
        break
      elif pos >= len(seats) - len(layout[0]) and key in ["south", "sw", "se"]: #last row
        if i!= pos:
          neighbours.append(pos)
        break
      if seats[pos] == "." and pos != i:
        pos = pos + dirs[key]

        continue
      if seats[pos] != "." and pos != i:
        neighbours.append(pos)
        break
      pos = pos + dirs[key]
  return neighbours


def adjacentFree(neighbours):
  for n in neighbours:
    if seats[n] == "#":
      return False
  return True

def occupiedNeighbours(neighbours):
  occupied = 0
  for n in neighbours:
    if seats[n] == "#":
      occupied +=1
  return occupied

changesThisRound = 0
changesLastRound = 1
rounds = 0

while changesLastRound > 0:
  seatsAfter = seats[:]
  changesThisRound = 0
  for i, s in enumerate(seatsAfter):
    neighbours = getNeighbours(i, seats)
    if s == "L" and adjacentFree(neighbours):
      seatsAfter[i] = "#"
      changesThisRound +=1
    if s == "#" and occupiedNeighbours(neighbours) >=5:
      seatsAfter[i] = "L"
      changesThisRound +=1
  rounds +=1
  changesLastRound = changesThisRound
  seats = seatsAfter[:]

print seatsAfter.count("#"), "rounds", rounds
# 2098 too low, 2092 too low, 2103 too low, 2109 too low
# 2124 wrong - after 86 rounds
