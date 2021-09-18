'''
Quetion 13
Write a function that removes empty strings from the list of strings.
'''
list = ["Shawn", "", "James"]
without_empty_strings = []
for string in list:
    if (string != ""):
            without_empty_strings.append(string)
print(without_empty_strings)            
