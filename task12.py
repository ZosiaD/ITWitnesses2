'''
Question 12
Sort a tuple of tuples by 2nd item. For example, the output for the tuple [('a', 23),('b', 37),('c', 11), ('d',29)]
should be [('c', 11), ('a', 23), ('d', 29), ('b', 37)]
'''
def Sort_Tuple(tup):
    return(sorted(tup, key=lambda x: x[1]))  
tup = [('a', 23), ('b', 37), ('c', 11), ('d', 29)]
print(Sort_Tuple(tup)) 
