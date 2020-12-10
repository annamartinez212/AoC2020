numbers = open("10Dec-data.txt", "r")
numbers = [int(x) for x in numbers]

numbers.sort(reverse = True)

deviceJlt = max(numbers) + 3
diffs = [min(numbers)]
acc = deviceJlt

for n in numbers:
  diff = acc - n
  diffs.append(diff)
  acc = n

print diffs.count(1)*diffs.count(3)
 #2432
