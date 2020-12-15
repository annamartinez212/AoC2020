with open("11Dec-data.txt", "r") as f:
  layout = f.readlines()

layout = [x.strip() for x in layout]

endOfRow = len(layout[0]) -1

seats = []

for r in layout:
  for s in r:
    seats.append(s)

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
    neighbours = []
    # top left
    if i == 0:
      neighbours = [i+1, i+endOfRow+1, i+endOfRow+2]
    # 1st row
    elif i < endOfRow:
      neighbours = [i-1, i+1, i+endOfRow+1, i+endOfRow, i+endOfRow+2]
    # top right
    elif i == endOfRow:
      neighbours = [i-1, i+endOfRow+1, i+endOfRow]
    # bottom left
    elif i ==len(layout[0])*len(layout) - len(layout[0]):
      neighbours = [i+1, i-endOfRow+1, i-endOfRow+2]
    # bottom right
    elif i == (endOfRow+1)*(len(layout))-1:
      neighbours = [i-1, i-endOfRow+1, i-endOfRow]
    # if eoR
    elif (i+1) % (endOfRow+1) == 0:
      neighbours = [i-1, i-(endOfRow+1), i+endOfRow+1, i-(endOfRow+2), i+endOfRow]
    # if left side
    elif i % (endOfRow+1) == 0:
      neighbours = [i+1, i-(endOfRow+1), i-endOfRow, i+endOfRow+1, i+endOfRow+2]
    # last row
    elif i >= len(seats)-1 - endOfRow:
      neighbours = [i-1, i+1, i-(endOfRow+1), i-endOfRow, i-(endOfRow+2)]
    else:
      neighbours = [i-1, i+1, i-(endOfRow+1), i+endOfRow+1, i-endOfRow, i-(endOfRow+2), i+endOfRow, i+endOfRow+2]
    if s == "L" and adjacentFree(neighbours):
      seatsAfter[i] = "#"
      changesThisRound +=1
    if s == "#" and occupiedNeighbours(neighbours) >=4:
      seatsAfter[i] = "L"
      changesThisRound +=1
  rounds +=1
  changesLastRound = changesThisRound
  seats = seatsAfter[:]


print seatsAfter.count("#"), "rounds", rounds
#2316 correct
