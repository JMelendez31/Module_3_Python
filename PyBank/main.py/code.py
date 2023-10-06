import os
import csv
budget_data = os.path.join ("Resources","budget_data.csv")
#Assigning variables
totalmonths = []
totalprofits = []
profitchanges = []
# Reading the CSV file
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)

    for row in csvreader:
    #print(row)
        totalmonths.append(row [0])
        totalprofits.append(int(row[1]))
    #print(len(totalmonths)) - Shows the total months 
    for x in range(1,len(totalprofits)):
        profitchanges.append((int(totalprofits[x]) - int(totalprofits[x-1]))) 
    #print(sum(totalprofits)) - Shows the total profits
    averagechange = ((sum(profitchanges)/len(profitchanges)))
    #print(averagechange) - Shows the Average change
    greatestincrease = max(profitchanges)
    #print(greatestincrease) - shows the greatest increase
    greatestdecrease = min(profitchanges)
    #print(greatestdecrease) - shows the greatest decrease
    
    #Shows data in the terminal
    print("Financial Analysis")
    print("--------------------")
    print("Total Months: " + str(len(totalmonths)))
    print("Total: $" + str(sum(totalprofits)))
    print("Average Change: $" + str(round(averagechange,2)))
    print("Greatest Increase in Profits:$" + str((greatestincrease)))
    print("Greatest Decrease in Profits:$" + str((greatestdecrease)))
    #Shows data in a Text File 
    f = open("output.txt","w")
    f.write("Financial Analysis" + "\n")
    f.write("-------------------------------" + "\n")
    f.write("Total Months: " + str(len(totalmonths)) + "\n")
    f.write("Total: $" + str(sum(totalprofits)) + "\n")
    f.write("Average Change: $" + str(round(averagechange,2)) + "\n")
    f.write("Greatest Increase in Profits:$" + str((greatestincrease)) + "\n")
    f.write("Greatest Decrease in Profits:$" + str((greatestdecrease)) + "\n")
    f.close()