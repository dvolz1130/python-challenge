import os
import csv

# Path to collect data from the Resources folder and write a file to analysis directory
election_csv = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join("analysis", "vote_analysis.txt")

# creating empty lists
candidate_list = []

# create dictionary to hold unique candidate and number of votes
candidate_dict = {}

# set up variables
total_votes = 0

# Read in the csv file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header
    next(csvreader)

    for row in csvreader:
        
        # Count number of rows(total votes)
        total_votes += 1

        # Create the candidate list
        candidate_list.append(row[2])

# Getting count of votes per candidate and sorting by highest votes
# Reference website - https://towardsdatascience.com/sorting-a-dictionary-in-python-4280451e1637
for i in set(candidate_list):
    candidate_dict[i] = candidate_list.count(i)
sorted_by_votes = sorted(candidate_dict.items(), key = lambda kv:kv[1], reverse=True)
sorted_candidate_dict = dict(sorted_by_votes)
#print(sorted_candidate_dict)

# Since this dictionary is sorted highest to lowest on vote count, the first key(candidate) in the dictionary is the winner
temp_list = list(sorted_candidate_dict)
winner = temp_list[0]

# create a unique candidate list
#unique_candidate_list = list(set(candidate_list))

print("")
print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")
for key, value in sorted_candidate_dict.items():
    vote_percentage = round(float((value / total_votes) * 100), 2)
    print(f"{key}: {vote_percentage}% ({value})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

# Open path and write to file
with open(output_path, 'w') as textfile:
    textfile.write(" \n")
    textfile.write("Election Results \n")
    textfile.write("--------------------------- \n")
    textfile.write(f"Total Votes: {total_votes} \n")
    textfile.write("--------------------------- \n")
    for key, value in sorted_candidate_dict.items():
        vote_percentage = round(float((value / total_votes) * 100), 2)
        textfile.write(f"{key}: {vote_percentage}% ({value}) \n")
    textfile.write("--------------------------- \n")
    textfile.write(f"Winner: {winner} \n")
    textfile.write("--------------------------- \n")