import csv 
import os

file = os.path.join("..", "Resources", "election_data.csv")

votes = 0
vote_percent = {}
vote = {}
candidates = []
greatesValue = []
winningCandidate = []
percents = []

#if you want to iterate more than once you need to open the file again so that the cursor may find its way to the top of the file.
with open(file, 'r') as csvfile:
	csvreader = csv.reader(csvfile)

	next(csvreader, None)
	for row in csvreader:
		if row[2] in vote:
			vote[row[2]] = vote[row[2]] + 1
		else:
			vote[row[2]] = 1
		votes += 1

	for k,v in vote.items():
		vote_percent[k] = str(round(((v/votes)*100),3)) + "%"
    
print(vote_percent)

for v in vote_percent.values():
	percents.append(v)
print(percents)
