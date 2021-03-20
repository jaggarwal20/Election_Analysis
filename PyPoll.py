# The data we need to revtrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The perfectage og votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote. 

#Import the datatime class from the datetime module.

import csv
import os

# assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", 'election_results.csv')

#Assign a variable to save the file to a path. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter. 
total_votes = 0

# Candidate opetions
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

#Open the election results and read the file
with open(file_to_load) as election_data:
    
    #Read the file object with the reader function. 
    file_reader = csv.reader(election_data)

    #read the header row.
    headers = next(file_reader)
    print(headers)
    
    #print each row in the csv file. 
    for row in file_reader:
        #2. add to the total vote count. 
        total_votes += 1

        # print the candidatename from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # add the candidate name to the list
            candidate_options.append(candidate_name)

            #2. Begin tracking the cadidate's vote count
            candidate_votes[candidate_name] = 0

        # add a vote to the cadidates count
        candidate_votes[candidate_name] += 1

        # Save the results to text file.
        with open(file_to_save,"w") as txt_file:
            # print the final vote count to the terminal.
            election_results = (
                f"\nElectionResults\n"
                f"------------------------\n"
                f"Total Votes: {total_votes:,}\n"
                f"------------------------\n")
            print(election_results, end="")
            #Save the final vote count to the text file.
            txt_file.write(election_results)
            # print each candidate to the text file
            for candidate_name in candidate_votes:
                #Retrieve vote count and pecerntage.
                votes = candidate_votes[candidate_name]
                vote_percentage = float(votes)/float(total_votes)*100
                candidate_results = (
                    f"{candidate_name}: {vote_percentage:.1f}% ({votes:,}\n")
                
                #Print each candidate's voter count and percentage to terminal
                print(candidate_results)

                #Save the candidate reuslts to text file.
                txt_file.write(candidate_results)

# Determine the percentage of votes for each candidate by looping through
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    #2. retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. calculate the percentage of votes.
    vote_percentage = float(votes)/float(total_votes)* 100
    # 4. print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage}% of the vote.")

    #Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #2. If true then set winning_count  = votes 
        # and winning_percent = vote_percentage
        # and winning_candidate = candidate_name
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage

    # print winning candidate
    winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}"
        f"Winning Vote Count {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------\n")

    print(winning_candidate_summary)
    # save the winning candidate results to text file
    txt_file.write(winning_candidate_summary)

#Close the file.


