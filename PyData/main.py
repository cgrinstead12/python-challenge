import csv 
import os

#set file path
file = os.path.join("..", "Resources", "election_data.csv")

#create empty dictionaries, lists, and variables set to 0
votes = 0
vote_percent = {}
vote = {}
greatestValue = []
winningCandidate = []
percents = []

#open the csvfile and loop through the rows
#set the values to a dictionary and add one each time a key is found
with open(file, 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	#skip the headers
	next(csvreader, None)
	#iterate for each row in the file and add unique keys to the dictionary
	for row in csvreader:
		if row[2] in vote:
			vote[row[2]] = vote[row[2]] + 1
		else:
			vote[row[2]] = 1
		#for every iteration add one to votes
		votes += 1

#creates a dictionary of the candidates and their percentages
for k,v in vote.items():
	vote_percent[k] = str(round(((v/votes)*100),3)) + "%"    

#creates a list of the votecount
for v in vote_percent.values():
	percents.append(v)
#creates a list of the total votes for each candidate
for v in vote.values():
	greatestValue.append(v)
#creates a list of the candidates
for w in vote.keys():
	winningCandidate.append(w)
#index to the candidate with the most votes
index = greatestValue.index(max(greatestValue))

#open a new text file and write the results to it
with open("Election Results.txt", 'w') as writeFile:
	writeFile.write("Election Results")
	writeFile.write("\n------------------\n")
	writeFile.write("Total Votes: " + str(votes))
	writeFile.write("\n------------------\n")
	for i in range(len(winningCandidate)):
		writeFile.write(winningCandidate[i]  + ": " + str(percents[i]) + " (" + str(greatestValue[i]) + ")\n")
	writeFile.write("------------------\n")
	writeFile.write("Winner: " + winningCandidate[index])
	writeFile.write("\n------------------\n")

#open the Analysis file and print to terminal
with open("Election Results.txt", 'r', newline="") as readFile:
	print(readFile.read())
