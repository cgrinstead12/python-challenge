import os 
import csv

#declare file variable and use the module to open the budget_data.csv file
file = os.path.join("..","Resources","budget_data.csv")

#declare list variables and declare variables with 0s to count with
months = []
revenue = []
totalRevenueChange = []
prevNet = 0
totalRevenue = 0
greatestNetChange = 0
lowestNetChange = 0

#open the budget_data file and declare a reader variable, skip the headers
with open(file, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	next(csvreader, None)

#iterate through the file and append the two columns to the month and revenue lists
	for row in csvreader:
		months.append(row[0])
		revenue.append(int(row[1]))

#iterate through the revenue list and add the iterated revenue to the totalRevenue variable.
#the prevNet variable will take the difference in the iterated row and the previous row
#then prevNet will be appended to the totalRevenueChange list and then prevNet will be set to the iterated value to be calculated in the next iteration
for row in range(len(revenue)):
	totalRevenue = totalRevenue + revenue[row]
	prevNet = revenue[row] - prevNet
	totalRevenueChange.append(prevNet)
	prevNet = revenue[row]

#delete the first value in the totalRevenueChange list because it was the first value subtracting a 0 value
del(totalRevenueChange[0])

#iterate through the totalRevenueChange list and use ifs to find the highest and lowest revenue values
for i in range(len(totalRevenueChange)):
	if totalRevenueChange[i] >= greatestNetChange:
		greatestNetChange = totalRevenueChange[i]
		greatestMonth = months[i + 1]
	elif totalRevenueChange[i] <= lowestNetChange:
		lowestNetChange = totalRevenueChange[i]
		lowestMonth = months[i + 1]

#open a new text file and set it to write and then write the variables to the analysis
with open("Financial Analysis.txt", 'w') as writeFile:
	writeFile.write("Financial Analysis")
	writeFile.write("\n----------------------------\n")
	writeFile.write("Total Months: " + str(len(months)) + '\n')
	writeFile.write("Total: $" + str(totalRevenue) + '\n')
	writeFile.write("Average Change: $" + str(round(sum(totalRevenueChange) / int(len(totalRevenueChange)),2)) + '\n')
	writeFile.write("Greatest Increase in Profits: " + str(greatestMonth) + " ($" + str(round(greatestNetChange, 2)) + ")" +'\n')
	writeFile.write("Greatest Decrease in Profits: " + str(lowestMonth) + " ($" + str(round(lowestNetChange, 2)) + ")" +'\n')


#open the Analysis file and print to terminal
with open("Financial Analysis.txt", 'r', newline="") as readFile:
	print(readFile.read())