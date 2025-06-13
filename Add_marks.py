import csv

file=open('marks.csv','r')
csvreader=csv.reader(file)
header=next(csvreader)

totalMarks={}
for row in csvreader:
  x=row[0]
  if x in totalMarks:
    totalMarks[x]=totalMarks[x]+int(row[1])
  else:
    totalMarks[x]=int(row[1])

print(totalMarks)      
