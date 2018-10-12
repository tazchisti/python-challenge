import csv
import os
import numpy as np
#Import Data
PollCSV = os.path.join("Resources", "election_data.csv")

#Set Variables
TotalVoters = 0
#An array to hold candidate names
Candidate = []
#A Tracker to find the place in the candidate array
CandidateTracker = 0
# An Array to hold the number of votes per candiate
CandidateVotes = []
# A tracker to hold the number of votes each candidate received
CandidateVoteTracker = 0
#an array to hold the percentages of the vote each candidate received
CandidatePercentages = []



#open CSV File
with open(PollCSV, newline='') as csvfile:
    #create reader# 
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        #calculates total voters
        TotalVoters += 1
        #creating array holding the candidates from unique names in row[2] of the csv file
        if row [2] not in Candidate:
            Candidate.append(row[2])

for i in range(0, len(Candidate)):

    with open(PollCSV, newline='') as csvfile:
        #create reader# 
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        
        for row in csvreader:
            #I want to see if row[2] of the CSV equals the first candidate in the array (CandidateTracker = 0 to begin)
            if  row [2] == Candidate[i]:
                
                # if this is true, then add 1 to the vote tracker
                CandidateVoteTracker +=1
                #insert this at the first part of the candidate votes array
                # CandidateVotes[i] = CandidateVoteTracker
            
                #move to next candidate
        CandidateVotes.append(CandidateVoteTracker)
        CandidateVoteTracker = 0

for i in range(0, len(Candidate)):
    CandidatePercentages.append(0)
    CandidatePercentages[i] = (CandidateVotes[i]/TotalVoters)*100

ElectionWinnerVotes =  max(CandidateVotes)
ind = np.argmax(CandidateVotes)

winner = Candidate[ind]

print("Election Results")
print("--------------------")
print (f"Total votes counted: {TotalVoters}")
print (f"The Winner is {winner} with {CandidatePercentages[ind]}% of the vote")
print("Election Results per Candidate")

for i in range(0,len(Candidate)):
    print(f"{Candidate[i]}  {CandidatePercentages[i]}")





