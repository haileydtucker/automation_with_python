#!/usr/bin/env python
# coding: utf-8

# # This program updates .sas file to configure table
# ## Code by Hailey Tucker
# ### June 01, 2020
# #### Last updated June 10, 2020


# Importing Libraries 
import string 

# file_location = "C:/Users/hatuck/Documents/PythonScripts/run_option.sas" # hard-coded location

# Using system line if calling python script in Perl testing pipeline
# import sys
# sys_string = sys.argv
# file_location = ''
# print ("This is the system string passed:", sys_string)
# file_location = str(sys_string[1])

# to_check = sys_string[2] # This is the dictionary of element checks to change lines 
# print ("This is the dictionary that was passed in:", to_check)
# #to_check = to_check.replace('//', '')
# #to_check = to_check.replace('\\', '') #
# #print ("This is the dictionary post strip of // and \\", to_check)
# to_check = eval(to_check) #checking if it is a dictionary format
# #print ("This is the eval of dict", to_check)
# import ast
# to_check = ast.literal_eval(to_check)
# #print ("This is the ast dictionary", to_check)

# hard - coded
file_location = 'manual_entries_temp.xlsx' 

# Reading in a file. 
with open (file_location) as f: 
    lines = f.readlines()
lines = [x.strip() for x in lines] 

#lines

# make to_check able to be passed in 

# Creating list for things to check for: (hard-coded)
 to_check = {"CURRENCY_DECIMAL_ROUNDING_FLG" : "Y","ALIGNMENT_LOGIC_FLG": "Y","ALIGNMENT_THRESHOLD_NO" : 100,"DERECOGNITION_LOGIC_FLG" : "Y"}

# Python program to convert a list to string 
    
# Function to convert   
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    return (str1.join(s))  



# Check each element in lines. If l in lines starts with any k element in keys of to_check, change the contents between the , , following
# the first element to be value for k
new_lines = []
for l in lines: # goes through each line 
    temp_line = l 
    temp_split = temp_line.split(',') # splits the line by the commas
    search_key = temp_split[0] # pulls out the key (first element in the line)
    temp_value = [val for key, val in to_check.items() if search_key in key] # pulls out the value from dict if search key is found in dict
    if not temp_value: # if the first value in the line is not found then just write out the new line
        new_line = temp_line
        new_lines.append(new_line)
    else:
        print("Previous line:", temp_line) # line hasn't changed yet
        temp_split[1] = temp_value[0]
        new_line = temp_split
        new_l = ','.join(str(v) for v in new_line) 
        print ("Updated line", new_l)
        new_lines.append(new_l)

new_lines


file = open(file_location,"w") # Overwriting previous run_option.sas file 
for line_var in new_lines:
    file.write(line_var)
    file.write("\n") # New line
file.close() # Closing out file 




