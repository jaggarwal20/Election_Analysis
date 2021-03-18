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

#Open the election results and read the file
with open(file_to_load) as election_data: 
    #To do:read and analyze the data here
    file_reader = csv.reader(election_data)
    
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)