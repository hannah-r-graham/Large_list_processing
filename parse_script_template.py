import json
import pandas as pd

# take file, first column has user id, second column has user info in a list 
# that needs to be parsed. Current info in list is like key = number, name = "info we want"


x = pd.read_csv('file_name.csv')

# take column to be parsed, loads in json and assign to variable
column_2 = x['skill'].apply(json.loads)
# create list for formatted columns
formatted_column = []
# loop through each row, and parse the info into a list (parsed column2)
for row in column_2:
    parsed_column2 = []
    for skills in row:
        for key, value in skills.items():
            # find the skill by looking for key "name"
            if key == 'name':
                # assign parsed skills to a list
                parsed_column2.append(value)
    # for the parsed skills list, assign it to the formatted column
    formatted_column.append(", ".join(parsed_column2))
# create new column and insert parsed skills inside the formatted column
x['column3'] = formatted_column


x.to_csv("file_name.csv", index=False)

# All of this below is for doing the above python script in POWER BI


# # 'dataset' holds the input data for this script
# import pandas as pd
# import matplotlib
# import json
# #take column to be parsed, loads in json and assign to variable
# column2 = dataset['column2_name'].apply(json.loads)
# #create list for formatted columns
# formatted_column = []
# #loop through each row, and parse column2 into a list (parsed column2)
# for row in column2:
#     parsed_column2 = []
#     for skills in row:
#         for key, value in skills.items():
#             #find the skill by looking for key "name"
#             if key == 'name':
#                 #assign parsed skills to a list
#                 parsed_column2 append(value)
#     #for the parsed skills list, assign it to the formatted column
#     formatted_column.append(", ".join(parsed_column2)
# #create new column and insert parsed column2 inside the formatted column
# dataset['processedcolumn2'] = formatted_column