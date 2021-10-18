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


