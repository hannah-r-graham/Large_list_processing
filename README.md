# Large_list_processing


Two files in this project. Goal is to get the data in a readable, and funtional format to count amounts and create a relationship between the two differently formatted tables. The parse script simply parses the information needed from a field with key value pairs. It pulls the info we are needing, getting rid of the extra, and assigns it back to a list in the column. 

Count skill takes the data from parse script (column 1 = id, column2= parsed info) then takes the parsed info, strips the extra characters, lowercases it, etc. Then takes the info, counts the occurence of it, then takes the user ids that all share the same info and assign them to it. Example: Column 1 = machine learning, Column 2= user  1, user2, user3. Column 3 (count) = 3. Meaning, 3 users have machine learning in their info.
