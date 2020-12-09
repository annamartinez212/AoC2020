from itertools import combinations

numbers = open("9Dec-data.txt", "r")
numbers = [int(x) for x in numbers]

pIdx = 25

def invalid(numbers, pIdx):
  for i, n in enumerate(numbers[pIdx:]):
    preamble = set(numbers[:pIdx+i])
    sums = map(lambda tup: (tup[0]+tup[1]), list(combinations(preamble,2)))
    if n not in sums:
      return n

# print(invalid(numbers, pIdx))
#1398413738 correct

invalid = invalid(numbers, pIdx)

for i, n in enumerate(numbers):
  for j in range(len(numbers)):
    if sum(numbers[i:j+1]) == invalid and len(numbers[i:j+1])>=2:
      print  min(numbers[i:j+1])+max(numbers[i:j+1])

# 169521051 correct
