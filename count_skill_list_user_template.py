import json
import pandas as pd

# takes original file that listed  user in column 1 and their info listed in 
# column two. then the output is: combines info and lists the users
# so common info is first column then there is a list of users is in the second 
# column. Example: Column 1: Machine Learning, Column2: user1, user2, user3,...

input_file= pd.read_csv('file_name.csv')
# Define vars
original = pd.DataFrame(input_file)
output_json = {}

# clean up data - get rid of upper case letters, strip  
# and make the data cleaner. 

def formatSkills(skillsStr):
    if not isinstance(skillsStr, str):
        return []
    skillsList = skillsStr.lower().split(',')
    iterator = map(lambda skill: skill.strip(), skillsList)
    return list(iterator)

# Loop row by row to see if skill is in list, if not stored, 
# then it adds it to the list and adds 1 to the count for that
# skill. if skill is stored or has to be added, then the email 
# is also added into a seperate list. 

output_json = {}
for index, row in original.iterrows():
    user = row['user']
    
    skills = formatSkills(row['Skills'])
    if isinstance(user, str): 
        for skill in skills:
            if skill not in output_json:
                output_json[skill] = {
                    'users': [],
                    'count': 0
                }
            output_json[skill]['users'].append(user)
            output_json[skill]['count'] = len(output_json[skill]['users'])
output_json

with open('file_name.json', 'w') as f:
    f.write(json.dumps(output_json))