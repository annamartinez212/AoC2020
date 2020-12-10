numbers = open("10Dec-data.txt", "r")
numbers = [int(x) for x in numbers]

numbers.sort(reverse = True)

deviceJlt = max(numbers) + 3
diffs = [min(numbers)]
acc = deviceJlt
# Any given adapter can take an input 1, 2, or 3 jolts lower than its rating and still produce its rated output joltage.

for n in numbers:
  diff = acc - n

  diffs.append(diff)
  acc = n

print diffs.count(1)*diffs.count(3)
 #2432
