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

for k in vote_percent.items():
        candidates.append(k)

for v in vote.values():
	greatesValue.append(v)

for w in vote.keys():
	winningCandidate.append(w)

for v in vote_percent.values():
	percents.append(v)

index = greatesValue.index(max(greatesValue))

with open("Election Results.txt", 'w') as writeFile:
	writeFile.write("Election Results")
	writeFile.write("\n------------------\n")
	writeFile.write("Total Votes: " + str(votes))
	writeFile.write("\n------------------\n")
	for i in range(len(candidates)):
		writeFile.write(winningCandidate[i]  + ": " + str(percents[i]) + " (" + str(greatesValue[i]) + ")\n")
	writeFile.write("------------------\n")
	
	#The optional key argument describes how to compare elements to get maximum among them:
	#lambda <item>: return <a result of operation with item> 
	writeFile.write("Winner: " + winningCandidate[index])
	writeFile.write("\n------------------\n")

#open the Analysis file and print to terminal
with open("Election Results.txt", 'r', newline="") as readFile:
	print(readFile.read())
