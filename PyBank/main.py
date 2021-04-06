import os
import csv

# Path to collect data from the Resources folder and write a file to analysis directory
budget_csv = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join("analysis", "financial_analysis.txt")

# create empty list to store data
month_changes = []
date = []

# Need to initialize some variables
month_count = 0
total_amount = 0
last_month_pl = 0
#total_changes_pl = 0

# Read in the csv file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header
    next(csvreader)

    for row in csvreader:
        
        # Count number of rows(months)
        month_count += 1

        # Store the Date in the date list, to stay in synce with the month_changes list
        date.append(row[0])

        # Calculate the net total amount
        total_amount = total_amount + int(row[1])

        # Calculate the changes in Profit/losses from month to month
        current_month_pl = int(row[1])
        monthly_change = current_month_pl - last_month_pl
        
        # Record monthly_change in the month_changes list to use to figure out, average change, greatest increase, and greatest decrease
        month_changes.append(monthly_change)

        # Keep track of last months profit/losses
        last_month_pl = current_month_pl

# Calculate the average of the changes in Profit/losses
# Need to remove the first item in the list because there is no change for profit/loss because it was the first month
month_changes.pop(0)
total_changes_pl = int(sum(month_changes))
average_change = int(round((total_changes_pl / (month_count - 1)), 2))

# Get the greatest increase and greatest decrease, along with date.
# Need to add 1 to the date index because the date list is storing the previous month before the greatest increase or greatest decrease
greatest_increase = max(month_changes)
increase_date = date[month_changes.index(greatest_increase) + 1]
greatest_decrease = min(month_changes)
decrease_date = date[month_changes.index(greatest_decrease) + 1]

# Print out results and write to file
with open(output_path, 'w') as textfile:

    print("Financial Analysis")
    textfile.write("Financial Analysis \n")
    print("-----------------------------")
    textfile.write("----------------------------- \n")
    print(f"Total Months: {month_count}")
    textfile.write(f"Total Months: {month_count} \n")
    print(f"Total: ${total_amount}")
    textfile.write(f"Total: ${total_amount} \n")
    print(f"Average Change: ${average_change}")
    textfile.write(f"Average Change: ${average_change} \n")
    print(f"Greatest Increase in Profits: {increase_date} $({greatest_increase})")
    textfile.write(f"Greatest Increase in Profits: {increase_date} $({greatest_increase}) \n")
    print(f"Greatest Decrease in Profits: {decrease_date} $({greatest_decrease})")
    textfile.write(f"Greatest Decrease in Profits: {decrease_date} $({greatest_decrease}) \n")
    textfile.close()

#End of script