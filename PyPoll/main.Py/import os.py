import os
import csv
# Joining paths
election_data = os.path.join("Resources","election_data.csv")
# Assigning variables
totalvotes = []
candidate = []
candidatelist = []
votes = {}
# Read the csv file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    csvheader = next(csvreader)
    data = list(csvreader)
    for row in data:
        totalvotes.append(row[0])
# Print(len(totalvotes)) - counts total votes


# Printing statements in the terminal
print("Election Results")
print("--------------------")
print("Total Votes:" + str(len(totalvotes)))

# Printing statements in a TXT file
f = open("output.txt","w")
f.write("Election Results" + "\n")
f.write("-------------------------------" + "\n")
f.write("Total Votes:" + str(len(totalvotes)) + "\n")
f.close()

