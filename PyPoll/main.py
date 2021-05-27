#import modules
import os
import csv
import operator

#setting veriables
total_votes = 0
candidate_names = []
candidate_votes = {}
candidate_votes_summary = ""
winner_name = []

# opening the data file 
with open("/Users/jsb/GitHub/Python-Challenge/PyPoll/Resources/election_data.csv") as poll_data:
    # reading csv file
    csv_file = csv.reader(poll_data, delimiter=",")
    #skipping the header row
    header = next(csv_file)
    # calulating the total number of votes
    for candidate in csv_file:
        total_votes += 1
        #going through the list of candidates in row 2
        #appending the new name of the candidate to the list and setting candidate votes to 0 for loop
        if candidate[2] not in candidate_names:
            candidate_names.append(candidate[2])
            candidate_votes[candidate[2]] = 0

        candidate_votes[candidate[2]] += 1    

# calling values from dictionary to calculate vote percent
for key, value in candidate_votes.items():
    vote_percent = ((value / total_votes) * 100)
    candidate_votes_summary += f"{key} : {vote_percent: .3f}% ({value})\n"

    
    
# find the winner by using the max function in candidate value and assigning it to key
winner_name = max(candidate_votes.items(), key = operator.itemgetter(1))[0]

# declaring output 
output = (
    f"Election Results\n"
    f"----------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------------\n"
    f"{candidate_votes_summary}"
    f"----------------------------------\n"
    f"Winner: {winner_name}\n"
    f"----------------------------------\n")

print(output)

# exporting the output in .txt file to analysis folder. 
with open("/Users/jsb/GitHub/Python-Challenge/PyPoll/Analysis/output.txt", "w") as txt_file:
    txt_file.write(output)



