# Large_list_processing


Two files in this project. Goal is to get the data in a readable and functional format to count amounts and create a relationship between the two differently formatted tables. 

The parse script simply parses the information needed from a field with key value pairs. It pulls the info we are needing, getting rid of the extra, and assigns it back to a list in the column. 

Sample data that this script parses: 
Column 1:       Column 2: 
user ID         [[{"key":"0","name":"value_we_want"}], {}....

Desired output of parsing function:
Column1:        Column 2:
User ID         value 1, value 2, value 3



Count skill takes the data from parse script, strips the extra characters, lowercases it, etc. Then takes the list, counts the occurence of it, then takes the unique list elements, and gives the users that listed that unique value from column 2, and the count of users.

Starting format of data:
Column1:        Column 2:
User ID1         value 1, value 2, value 3
User ID2        value 2, value 4

Output:
Column 1:             Column 2:             Count:
Unique value  1       User ID 1             1
Unique Value 2      User ID1, User ID2      2
