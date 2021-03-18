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
file_to_load = os.path.join("Resources", '/Users/juhiaggarwal/Desktop/UT_Data_Analytics_Class/Election_Analysis/Resources/election_results.csv')

#create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#total vote counter
total_votes = 0

#Candidate List
candidate_options = []

#Declare empty Dictionary
candidate_votes = {}

# Empty string value Winning Candidate
winning_candidate= ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data: 
    #To do:read and analyze the data here
    file_reader = csv.reader(election_data)
    
    # Read and print the header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader:
        # Add the total vote count.
        total_votes += 1

        #Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match and existing candidate...
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list,
            candidate_options.append(candidate_name)

            #Begin tracking the candidates vote count
            candidate_votes[candidate_name]= 0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] +=1

for candidate_name in candidate_votes:
    #Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #calculate the percentage of votes
    vote_percentage = float(votes)/float(total_votes)*100
    #Print the candidate name and percentage of votes
    #print(f'{candidate_name}: recieved {vote_percentage}% of the vote.')

    #to do: print out each candidates name, vote count, and percentage of votes to the terminal
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        #set winning_candidate equal to the candidate's name
        winning_candidate = candidate_name
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

for candidate in candidate_votes:
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage: .1f}%\n"
        f"----------------------------\n"
    )
    print(winning_candidate_summary)
#Print total Votes
# print(total_votes)

# #Print list of candidates
# print(candidate_options)

# print(candidate_votes)
# print(winning_candidate)
# print(winning_count)
# print(winning_percentage)