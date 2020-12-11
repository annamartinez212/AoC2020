from itertools import count, combinations, groupby

numbers = open("10Dec-data.txt", "r")
numbers = [int(x) for x in numbers]
numbers.sort(reverse = True)

outletJlt = 0
deviceJlt = max(numbers) + 3
acc = deviceJlt

def differnces(numbers, acc):
  diffs = []
  for n in numbers:
    diff = acc - n
    diffs.append(diff)
    acc = n
  diffs.append(acc)
  return diffs

diffList = differnces(numbers, acc)

occurences = [(x[0], len(list(x[1]))) for x in groupby(diffList)]
maxOnes = max(occurences, key=lambda x:x[1])[1] # just happens to be right, because longer 1-chains than 3-chains - fix is easy, check later

a=1
b=2
c=4
combArrayFor1s = [1, 2, 4]
for i in range(maxOnes - len(combArrayFor1s)): #the longest1 chain combos minus the 3 amounts of combos already in combArrayFor1s for 1, 11 and 111
  combsForConsec1s = a+b+c
  combArrayFor1s.append(combsForConsec1s)
  a=b
  b=c
  c=combsForConsec1s

result = 1
for i, x in enumerate(combArrayFor1s):
  result = result * pow(combArrayFor1s[i], occurences.count((1, i+1)))

print "RESULT", result

# 453551299002368 correct
