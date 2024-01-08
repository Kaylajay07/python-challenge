import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("analysis", "election_analysis.txt")

#Open and Read csv
with open(election_csv) as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
#Set variables
    total = 0 
    namelist = []
    votedict= {}
    winning_votes = 0 

#Loop through each row of data
    
    #count total votes
    for line in csv_reader:
        total += 1 
        name = line[2]

        if name not in namelist:
            namelist.append(name)
            votedict[name] = 0
        votedict[name]+= 1     

with open(output_path, "w") as file:
    vote_data = (f"""Election Results
-------------------------
Total Votes: {total}
-------------------------     
""") 
    
    print(vote_data)
    file.write(vote_data)
# Loop through each row of data    
    #calculate vote percentage and vote count per canidate 
    for canidate in votedict:
        vote = votedict.get(canidate)
        percent = float(vote)/ total * 100 
        vote_data = f'{canidate}: {percent:.3f}% ({vote})\n'
        print(vote_data)
        file.write(vote_data)
    
    #Find canidate with most votes 
        winner =max(votedict, key= votedict.get)
        winning_votes = votedict[winner]
    print("-----------------------")       
    winning_cadidate = (f"""---------------------
Winner: {winner}
-----------------------""")

#print and write winner
    file.write(winning_cadidate)
               
print("Winner: ", winner)
print("------------------------")
        