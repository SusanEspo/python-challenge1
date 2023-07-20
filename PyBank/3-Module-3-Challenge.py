
##Created on Sun Jul 16 15:58:32 2023

##author: Susan Espinosa espo.susan@gmail.com

##Ptyhon HW Module 3 challenge

## STEP#1  - read file 
##"C:\Users\espos\Documents\DS-BootCamp\3-Module-3-Challenge\Starter_Code\PyBank\Resources"\budget_data.csv"

##"C:\Users\espos\Documents\DS-BootCamp\3-Module-3-Challenge\Starter_Code\PyBank\Resources"



##imports
import os
import csv

 
##Declartion

##Varibles
mycvs_budget = os.path.join("/Users/espos/Documents/DS-BootCamp/3-Module-3-Challenge/Starter_Code/PyBank/Resources","budget_data.csv")
ttl_mths_budget_file = 0 ## deliverable total number of months
ttl_netprofit_budget_file =0
##ttl_mths_budget_file  holds count of months in file
total_num_rows = 0

rows_in_file = []  ## here i'm making a list of the rows

fields_in_file = []  ## here i'm making a list of the field names

counter = 0

total_profit_change = 0 

avg_chg = 0

current_greatest_increase = 0
current_greatest_increase_date = ""

current_greatest_decrease = 0 
current_greatest_decrease_date = ""


## STEP#1  - read file 
with open(mycvs_budget, 'r') as csvfile:   # opens file
     #lines = file_handler.read()
    # print(lines)
    # print(type(lines))
    csvreader = csv.reader(csvfile)  ##reader object 
    
    header_names = next(csvreader)  ##read one line at a time 
    for row in csvreader:   ## all the lines 1 at a time
      ##rows_in_file.append(row)   # at line 2 
      
      date = row[0] 
      current_profitloss = int(row[1]) 

      counter = counter + 1 ##passed the header 2nd row
      ttl_netprofit_budget_file = ttl_netprofit_budget_file + current_profitloss
     
      if counter > 1: ## checking for jan 1st instance  and skips since we don't have a profit loss
        monthly_profitloss = current_profitloss - previous_profitloss   ##calculation of the monthly profit  
        total_profit_change = total_profit_change + monthly_profitloss  ##increaments TPC 
        if monthly_profitloss > current_greatest_increase:
              current_greatest_increase =  monthly_profitloss
              current_greatest_increase_date = date
        if monthly_profitloss < current_greatest_decrease:
              current_greatest_decrease =  monthly_profitloss
              current_greatest_decrease_date = date

      previous_profitloss = current_profitloss
      
    
     ## print (row)
  
  ##after the forLoop
    avg_chg =  total_profit_change / (counter -1)   ##minus 1 if for the skip of january


    ## print required data  - fix formatting
    print("Financial Analysis")
    print("------------------------------------------------------")
    print("Total Months ", counter)
    print("Total: $", ttl_netprofit_budget_file)  
    print("Averge Change $",  avg_chg )
    print("Greatest Increase in Profits:", current_greatest_increase_date, current_greatest_increase )
    print("Greatest Decrease in Profits", current_greatest_decrease_date, current_greatest_decrease  )
   
  
   ## ttl_netprofit_budget_file = sum(rows_in_file )
   ## print("Buget Data has ", counter, "number of months.")
   ## print("Buget Data has net value of ", ttl_netprofit_budget_file) ##worng total
   ## print("Avg chang over time",  avg_chg )
   ## print("current_greatest_increase", current_greatest_increase_date, current_greatest_increase )
   ## print("current_greatest_decrease", current_greatest_decrease_date, current_greatest_decrease  )
    ##i tried some """
   
    
    ##print(header_names)
    ##print(rows_in_file)
    ##print(total_profit_change)
    ##print(fields_in_file)    
     

# for row in  csv_read_it:
    
#     if (row[1]) != " ":
#         ttl_mths_budget_file = ttl_mths_budget_file + (row[2])
#         print(row)
         
 
 
     
     