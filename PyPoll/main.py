##Created on Sun Aug 18 

##author: SE

##Ptyhon HW Module 3 challenge PYPOLL

##IMPORTS
import os
import csv


## Declarations


total_votes = 0
percentage_vote = 0
candidate_list=[]
winner = ""
current_percentage_vote = 0

#create empty dictionary

votes_by_candidate ={}


#read the file 
## STEP#1  - read file 
mycvs_pypoll= os.path.join("/Users/espos/Documents/DS-BootCamp/3-Module-3-Challenge/PyPoll/resources","election_data.csv")
OutPrint = open("/Users/espos/Documents/DS-BootCamp/3-Module-3-Challenge//PyPoll/analysis/election_outout.csv", "w")

with open(mycvs_pypoll, 'r') as csvfile:   # opens file

    csvreader = csv.reader(csvfile)  ##reader object list of dictionary 



    header_names = next(csvreader)  ##read one line at a time 


##for loop thru each row
    for row  in csvreader:
        candidate_name = row[2]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            votes_by_candidate.update({candidate_name:0 }) 
        votes_by_candidate[candidate_name] = votes_by_candidate[candidate_name] + 1 
        total_votes = total_votes + 1 ##passed the header 2nd row
print("Election Results")

OutPrint.write("Election Results\n")

print("--------------------------------------------\n")

OutPrint.write("--------------------------------------------\n")

print(f"Total Votes: {total_votes:,}\n")        
print("--------------------------------------------\n")
#percent =  1 person vote / total 

OutPrint.write(f"Total Votes: {total_votes:,}\n")  
 
OutPrint.write("--------------------------------------------\n")
            
#unpack 
for k, v in (votes_by_candidate.items()):
    
     percentage_vote = round( (v / total_votes) * 100,3)
     str_percentage_vote = str(percentage_vote)
     str_v = str(v)
     print(k, percentage_vote,"% (", v ,")")
     OutPrint.write("\n")
     OutPrint.write(k)
     OutPrint.write(" ")
     OutPrint.write(str_percentage_vote)
     OutPrint.write("% (")
     OutPrint.write(str_v)
     OutPrint.write(")")
     OutPrint.write("\n")
     
     if percentage_vote  > current_percentage_vote :
             current_percentage_vote  =  percentage_vote
             winner = k
             
print("\n--------------------------------------------")
   
print("Winner: ", winner)
print("--------------------------------------------")

OutPrint.write("--------------------------------------------\n")
OutPrint.write("Winner: ")
OutPrint.write(winner)
OutPrint.write("\n--------------------------------------------\n")


OutPrint.close()



