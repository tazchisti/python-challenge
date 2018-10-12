import os
import csv
#import csv file
BankCSV = os.path.join('..', 'Resources', 'budget_data.csv')

#Set Counters for revenue and numbers of rows
MonthCounter = 0
TotalRevenue = 0
GreatestIncrease = 0
GreatestDecrease = 0
IncMonth = 0
DecMonth = 0
lastMonth = 0

#open CSV File
with open(BankCSV, newline='') as csvfile:
    #create reader# 
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:  
        MonthCounter += 1
        Revenue = float(row[1])
        TotalRevenue += Revenue

        revenue_change = (int(row[1]) - lastMonth)

        if revenue_change > GreatestIncrease:
            GreatestIncrease = revenue_change
            IncMonth = row[0]
        if revenue_change < GreatestDecrease:
            GreatestDecrease = revenue_change
            DecMonth = row[0]

        row[1] = lastMonth
    
print ("")
print("Financial Analysis")
print("-------------------------------")

print(f"Total Months: {str(MonthCounter)}")
print(f"Total Revenue: {str(TotalRevenue)}")
print(f"Greatest Increase: ${GreatestIncrease} - {IncMonth}")
print(f"Greatest Decrease: ${GreatestDecrease} - {DecMonth}")
print ("")

