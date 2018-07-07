import csv 
import os

file = os.path.join("..", "election_data.csv")

test = []
rawdata = []
vote = {}
total_votes = 0

#if you want to iterate more than once you need to open the file again so that the cursor may find its way to the top of the file.
with open(file, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter =',')
	next(csvreader, None)
	#rawdata = list(csvreader)

	for k,v,i in csvreader:
		vote[i] = 1
		

print(vote)

#print(test)
#print(total_votes)
#print(type(csvreader))