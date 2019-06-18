# import os and csv
import os
import csv

#establish csv file route
csv_path = os.path.join("Resources_budget_data.csv")

total_months = 0
total = 0.0
average_change = 0.0
greatest_decrease = {"Date": "01/01/01" , "Amount": 0.0}
greatest_increase = {"Date": "01/01/01" , "Amount": 0.0}

#Open CSV file
with open(csv_path, newline = '') as csvfile:
    csv_reader = csv.DictReader(csvfile)#, delimiter = ",") # create a reader object

    #skip headers
    #next(csv_reader, None)

    for row in csv_reader:
        total_months += 1
        total = total + float(row["Profit/Losses"])
        if float(row["Profit/Losses"]) < greatest_decrease["Amount"]:
            greatest_decrease["Amount"] = float(row["Profit/Losses"])
            greatest_decrease["Date"] = str(row["Date"])
        if float(row["Profit/Losses"]) > greatest_increase["Amount"]:
            greatest_increase["Amount"] = float(row["Profit/Losses"])
            greatest_increase["Date"] = str(row["Date"])
    
    average_change = total / float(total_months)

print("Financial Analizis")
print("--------------------")
print(f'Total Months: {total_months}')
print(f'Total: {total}')
print(f'Average Change: {average_change}')
print(f'Greatest Decrease in Profits: {greatest_decrease["Date"]} ({greatest_decrease["Amount"]})')
print(f'Greatest Increase in Profits: {greatest_increase["Date"]} ({greatest_increase["Amount"]})')


csv_path = os.path.join("Output.txt")

with open(csv_path, "w") as writer:
    
    #writer.write("Financial Analizis")
    #writer.write("--------------------")
    #writer.write(f'Total Months: {total_months}')
    #writer.write(f'Total: {total}')
    #writer.write(f'Average Change: {average_change}')
    #writer.write(f'Greatest Decrease in Profits: {greatest_decrease["Date"]} ({greatest_decrease["Amount"]})')
    #writer.write(f'Greatest Increase in Profits: {greatest_increase["Date"]} ({greatest_increase["Amount"]})')


