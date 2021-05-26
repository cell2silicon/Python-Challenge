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


# opening data file
with open("/Users/jsb/GitHub/Python-Challenge/PyBank/Resources/budget_data.csv") as budget_data:

#   headerline = budget_data.next()
    csv_file = csv.reader(budget_data, delimiter = ',')
    headings = next(csv_file)
    first_row = next(csv_file)
    

    for row in csv_file:
        total_months += 1
        total_amount += int(row[1])

        if greatest_increase["value"] < int(row[1]):
            greatest_increase["month"] = row[0]
            greatest_increase["value"] = int(row[1])
        if greatest_decrease["value"] > int(row[1]):
            greatest_decrease["month"] = row[0]
            greatest_decrease["value"] = int(row[1])

    # calculate the chnages in the data

        change_profit_loss = int(row[1]) - change_previous
        change_monthly.append(change_profit_loss)
        change_previous = int(row[1])

    # calculate average change
    average_change = sum(change_monthly) / total_months

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

with open("/Users/jsb/GitHub/Python-Challenge/PyBank/Analysis/output.txt", "w") as txt_file:
    txt_file.write(output)
