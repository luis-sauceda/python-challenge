import os
import csv

file_path = os.path.join("Resources_election_data.csv")
total_votes = 0
candidates = []
votes = {}

with open(file_path, newline = '') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    for row in csv_reader:
        total_votes += 1
        if row["Candidate"] not in candidates:
          candidates.append(row["Candidate"])
          votes.update({row["Candidate"]: 1})
            #candidates.update(new_val)
        else:
            vote = votes[row["Candidate"]]
            vote += 1
            
            votes.update({row["Candidate"]: vote})

def percentage(votes_count, total):
    return round((votes_count / total) * 100, 2)


winner = ""
winner_votes = 0

csv_path = os.path.join("Output.txt")

with open(csv_path, "w") as writer:
    
    writer.write("Election Results\n")
    print("Election Results")
    writer.write("--------------------\n")
    print("--------------------")
    writer.write(str(total_votes) +"\n")
    print(str(total_votes))
    writer.write("--------------------\n")
    print("--------------------")

    for candidate, val in votes.items():
        print (candidate + ": " + str(percentage(val, total_votes)) + "%" + f' ({val})')
        writer.write(candidate + ": " + str(percentage(val, total_votes)) + "%" + f' ({val})\n')
        if val > winner_votes:
            winner_votes = val
            winner = candidate
    writer.write("--------------------\n")
    print("--------------------")
    writer.write("Winner: " + winner + "\n")
    print("Winner: " + winner)
    writer.write("--------------------")
    print("--------------------")



    
