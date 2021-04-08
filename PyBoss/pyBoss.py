import os
import csv
import datetime

# Reference - https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5#file-us_state_abbrev-py
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# set up some list to hold emp ID, First Name, Last Name, DOB, SSN, State
emp_id = []
first_name = []
new_first_name = []
new_last_name = []
date_of_birth = []
ssn = []
state = []

# Read the employee csv file
employee_csv = os.path.join("employee_data.csv")

with open(employee_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header
    next(csvreader)

    for row in csvreader:

        #start filling up the lists
        emp_id.append(row[0])
        first_name.append(row[1])
        date_of_birth.append(row[2])
        ssn.append(row[3])
        state.append(row[4])

# split the list first name into 2 new list
for name in first_name:
        new_first_name.append(name.split()[0])
        new_last_name.append(name.split()[-1])

# Re-writing the date_of_birth list to show mm/dd/yy
# Reference site - https://stackoverflow.com/questions/32258915/reformatting-a-list-of-date-strings-to-day-month-year-in-python
date_of_birth = (datetime.datetime.strptime(i, "%Y-%m-%d") for i in date_of_birth)
date_of_birth = (datetime.datetime.strftime(i, "%Y-%m-%d") for i in date_of_birth)

## Re-write the ssn with the first 5 digits hidden
new_ssn = []
for x in range(len(ssn)):
    ssn_string = ssn[x]
    ssn_string = ssn_string[:0] + "***-**-" + ssn_string[7:]
    new_ssn.append(ssn_string)
new_ssn

# Re-write the states with two-letter abbreviations
new_state = []

for x in state:
    new_state.append(us_state_abbrev[x])
new_state

# zip together all the list
new_employee_data = zip(emp_id, new_first_name, new_last_name, date_of_birth, new_ssn, new_state)

# write to new output file
# Adding newline='' gets rid of the empty cells
new_employee_csv = os.path.join("new_employee_data.csv")

with open(new_employee_csv, 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)

    # write heading to new file
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # write in zipped new_csv
    writer.writerows(new_employee_data)