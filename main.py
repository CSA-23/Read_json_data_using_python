# Python program to read json file

import json
  
# To Open JSON file
f = open('data.json')
  
# It returns JSON object as dictionary
data = json.load(f)
  
# Iterating through the json list
for i in data['emp_details']:
    print(i)
  
# Closing file
f.close()
