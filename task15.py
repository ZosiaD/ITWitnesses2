'''
Question 15
Write a function called is_sorted that is given a list and returns
True if the list is sorted and False otherwise.
'''
def is_sorted(a):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True
print(is_sorted([0, 2, 3, 4, 6]))
print(is_sorted([8, 2, 3, 4, 6]))
