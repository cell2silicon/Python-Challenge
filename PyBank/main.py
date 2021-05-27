# import modules

import csv
import os

# setting variables for  the number of months and total value of profit and loss
total_months = 0
total_amount = 0
change_monthly = []
greatest_increase = {"month":"","value": 0}
greatest_decrease = {"month":"","value": 0}
change_profit_loss = 0
change_previous = 0

# set path for the file
csvpath = os.path.join("/Users/jsb/GitHub/Python-Challenge/PyBank/Resources/budget_data.csv")

# opening and reading csv file

with open(csvpath, newline='') as budget_data:

#   reading file by skipping header
    csv_file = csv.reader(budget_data, delimiter = ',')
    next(csv_file)

    # to calculate the number of months
    for row in csv_file:
        total_months += 1
        total_amount += int(row[1])

        # finding the values for greatest increase and greatest decrease
        if greatest_increase["value"] < int(row[1]):
            greatest_increase["month"] = row[0]
            greatest_increase["value"] = int(row[1]) - change_previous
        if greatest_decrease["value"] > int(row[1]):
            greatest_decrease["month"] = row[0]
            greatest_decrease["value"] = int(row[1]) -change_previous

    # calculate the chnages in the data

        change_profit_loss = int(row[1]) - change_previous
        change_monthly.append(change_profit_loss)
        change_previous = int(row[1])

    # calculate average change
    # since the first element subtracts only 0, so remove the first element from following calculation
    average_change = sum(change_monthly[1:]) / len(change_monthly[1:])

# declaring output values
output = (
    f"Financial Analysis\n"
    f"-------------------------------------------\n"
    f"Total Months : {total_months}\n"
    f"Total Amount : {total_amount}\n"
    f"Average Change : {average_change}\n "
    f"Greatest Increase in Profits : {greatest_increase['month']} (${greatest_increase['value']})\n "
    f"Greatest Decrease in Profits : {greatest_decrease['month']} (${greatest_decrease['value']})\n"
)
#print output to terminal
print(output)

# printing output value in .txt format to analysis folder
with open("/Users/jsb/GitHub/Python-Challenge/PyBank/Analysis/output.txt", "w") as txt_file:
    txt_file.write(output)
