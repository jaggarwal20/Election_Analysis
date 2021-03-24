# Election_Analysis

## Table of Contents
- [1.0 Project Overview](#Project-Overview)
  * 1.1 Purpose
  * 1.2 Resources
- [2.0 Election Audit Results](#Election-Audit-Results)

- [3.0 Election Audit Summary](#Election-Audit-Summary)

<a name="Project-Overview"></a>
## Project Overview
### 1.1 Purpose
Seth and Tom need help conducting an election audit for the Colorado Board of Elections. The board requests that the candidate winner is confirmed but also require the following:
 1. The voter turnout for each city
 2. The percentage of votes from each county out of the total votes
 3. The county with the highest turnout

### 1.2 Resouces
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

<a name="Election-Audit-Results"></a>
## Election Audit Results
* Calculate the total number of votes cast.
  
  The total number of votes cast is 369,711. This total was calculated by creating a for loop. 
  
* Number and percentage of votes for each county. 
  
  - Jefferson County recieved 38855 votes, which is 10.5% of the total votes. 
  - Denver County received 306055 votes, which is 82.8% of the total votes.
  - Arapahoe County received 24801 votes, which is 6.7% of the total votes. 
  
* Which county had the largest number of votes?
  - Denver
 
* Number and percentage of votes each candidate received. 
  - Charles Casper received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
  
* Determine the winner of the election based on popular vote.

  The winner of the election is Diana DeGette who received 73.8% of the votes and 272,892 number of votes. 

![alt text](Resources/election_analysis.png)

<a name="Election-Audit-Summary"></a>
## Election Audit Summary

This script can be used for any election by adjusting the load file and save file paths. 
![alt text](Resources/Load_Save_File.png)

The variables can also be adjusted to represent the data more accurately. For instance if the votes is on a state level rather than a county level. 

