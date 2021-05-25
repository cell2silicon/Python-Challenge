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

