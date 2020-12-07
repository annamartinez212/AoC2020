report_file = open("1Dec-data.txt", "r")


with open("1Dec-data.txt", "r") as f:
  expense_report = f.readlines()
expense_report = [x.strip() for x in expense_report]


for i in range(len(expense_report)):
  rg = len(expense_report) - i -1
  for j in range(rg):
    if int(expense_report[i]) + int(expense_report[j+1+i]) == 2020:
      print expense_report[i], expense_report[j+1+i]
