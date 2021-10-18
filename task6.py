'''
Write a function that asks the user to enter a list of integers. Do the following:

Print the total number of items in the list.
Print the last item in the list.
Print the list in reverse order.
Print Yes if the list contains a 5 and No otherwise.
Print the number of fives in the list.
Remove the first and last items from the list, sort the remaining items, and print the result.
Print how many integers in the list are less than 5.
'''

x = int(input("Enter number of elements : "))
l = []
for i in range(0, x):
    ll = int(input())
    l.append(ll) 
     
print(l)

print('The total number of items in the list:', len(l))
last_item = l[-1]
print('The last item in the list:' , last_item)
l.reverse()
print('The list in reverse order:', l)
if (5 in l) :
    print("YES")
else:
    print("NO")
    
print('Number of 5:', l.count(5))
l.pop(0)
l.pop()
l.sort()
print(l)
print(len([1 for i in l if i > 5]), 'integers in the list are less than 5')


