import os
import csv

# Define variables used throughout the script
total_months = 0
total_profit = 0.0
total_profit_change = 0.0
previous_month_profit = 0.
average_profit_change = 0.0
profit_changes = []
greatest_profit_increase = 0.0
greatest_profit_increase_row = []
greatest_profit_decrease = 0.0
greatest_profit_decrease_row = []

# Path to acquire data from the Resources folder
budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')

# Define funtion to format as currency to two decimal places
def as_currency(amount):
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    

    # Loop through the data
    for row in csvreader:
        total_months += 1

        # Current month profit variable
        current_month_profit = float(row[1])

        # Check if on the first month
        if total_months > 1:
            change = current_month_profit - previous_month_profit
            profit_changes.append(change)

            # Check for greatest increase in profits
            if change > greatest_profit_increase:
                greatest_profit_increase = change
                greatest_profit_increase_row = [row[0], change]

            # Check for greatest decrease in profits
            if change < greatest_profit_decrease:
                greatest_profit_decrease = change
                greatest_profit_decrease_row = [row[0], change]   



        total_profit += current_month_profit
        previous_month_profit = current_month_profit


# Sum the total profit change from the 'profit_changes' list

for change in profit_changes:
    total_profit_change += change

average_profit_change = total_profit_change / len(profit_changes)
print("\nFinancial Analysis\n----------------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total: {as_currency(total_profit)}\n")
print(f"Average Change: {as_currency(average_profit_change)}\n")
print(f"Greatest Increase in Profits: {greatest_profit_increase_row[0]} ({as_currency(greatest_profit_increase_row[1])})\n")
print(f"Greatest Decrease in Profits: {greatest_profit_decrease_row[0]} ({as_currency(greatest_profit_decrease_row[1])})")

# Output the anaylsis to a text file in the 'analysis' folder

analysis_results = os.path.join('.', 'analysis', 'analysis_results.txt')
with open(analysis_results, 'w') as f:
    f.write("Financial Analysis\n----------------------------\n")
    f.write(f"\nTotal Months: {total_months}\n")
    f.write(f"\nTotal: {as_currency(total_profit)}\n")
    f.write(f"\nAverage Change: {as_currency(average_profit_change)}\n")
    f.write(f"\nGreatest Increase in Profits: {greatest_profit_increase_row[0]} ({as_currency(greatest_profit_increase_row[1])})\n")
    f.write(f"\nGreatest Decrease in Profits: {greatest_profit_decrease_row[0]} ({as_currency(greatest_profit_decrease_row[1])})")
