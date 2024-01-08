import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("analysis", "budget_analysis.txt")

#Lists to store data 
changelist = []
greatestinc = ["", 0]
greatestdec = ["", 0]

#open and read csv
with open(budget_csv) as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
 #Set variables   
    month_count = 0 
    month_count += 1 
    total = 0
    firstline = next(csv_reader)
    total += int(firstline[1])
    previousvalue = int(firstline[1])

#Loop through each row of data
    for row in csv_reader:
        month_count+= 1
        total += int(row[1])
        change = int(row[1])- previousvalue 
        previousvalue = int(row[1]) 
        changelist.append(change)

        if change > greatestinc[1]: 
            greatestinc[1] = change
            greatestinc[0] = row[0]
        
        if change < greatestdec[1]: 
            greatestdec[1] = change
            greatestdec[0] = row[0]


monthlyaverage = sum(changelist)/ len(changelist)

#Print and Write results
result = (f''' Financial Analysis
----------------------------
Total Months: {month_count}
Total: ${total}
Average Change: ${monthlyaverage:.2f}
Greatest Increase in Profits: {greatestinc[0]} (${greatestinc[1]})
Greatest Decrease in Profits: {greatestdec[0]} (${greatestdec[1]})


''')

print(result)

with open(output_path, "w") as file:
    file.write(result)


