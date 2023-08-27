
##Created on Sun Jul 16 15:58:32 2023

##author: Susan Espinosa
##Ptyhon HW Module 3 challenge

##imports
import os
import csv

## STEP#1  - read file 

mycvs_budget = os.path.join("/Users/espos/Documents/DS-BootCamp/3-Module-3-Challenge/Starter_Code/PyBank/Resources","budget_data.csv")
fin_out = open("/Users/espos/Documents/DS-BootCamp/3-Module-3-Challenge/PyBank/analysis/Financial_Analysis.csv","w")


##Declartion

##Varibles

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
    print_avg_chg = round(avg_chg,2)

    ## print required data  - fix formatting
    print("Financial Analysis:")
    print("------------------------------------------------------")
    print("Total Months: ", counter)
    print("Total: $", ttl_netprofit_budget_file)  
    print("Averge Change $",  print_avg_chg )
    print("Greatest Increase in Profits:", current_greatest_increase_date, "(",current_greatest_increase,")")
    print("Greatest Decrease in Profits:", current_greatest_decrease_date,"(",current_greatest_decrease,")")
    
    
    str_counter = str(counter)
    str_ttl_netprofit_budget_file = str(ttl_netprofit_budget_file)
    str_avg_chg = str(print_avg_chg)
    str_current_greatest_increase_date = str(current_greatest_increase_date)
    str_current_greatest_increase = str(current_greatest_increase)
    str_current_greatest_decrease_date = str(current_greatest_decrease_date)
    str_current_greatest_decrease = str(current_greatest_decrease)
    
    ## print required data  - fix formatting
    fin_out.write("Financial Analysis:")
    fin_out.write("\n-------------------------------------------\n")
    fin_out.write("Total Months: ")
    fin_out.write(str_counter)
    fin_out.write("\nTotal: $")
    fin_out.write(str_ttl_netprofit_budget_file)  
    fin_out.write("\nAverge Change $")
    fin_out.write(str_avg_chg )
    
    fin_out.write("\nGreatest Increase in Profits:  " )
    fin_out.write(str_current_greatest_increase_date)
    fin_out.write(" " )
    fin_out.write(str_current_greatest_increase)
    
    #fin_out.write("Greatest Decrease in Profits:", current_greatest_decrease_date,"(",current_greatest_decrease,")")
   
    fin_out.write("\nGreatest Increase in Profits:  " )
    fin_out.write(str_current_greatest_decrease_date)
    fin_out.write(" " )
    fin_out.write(str_current_greatest_decrease)
 
    fin_out.write("\n--------------------------------------------\n")


    fin_out.close()

     