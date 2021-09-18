a = 0
b = 0
x = list(map(int, input()))
print('The total number of items in the list', len(x))
print('The last item in the list', x[-1])
x.reverse()
print('The list in reverse order', x)
for i in x:
    if i == 5:
        a += 1
    elif i < 5:
        b += 1
if a > 0:
    print('This list contains a 5,', 'number of 5 : ', a)
else:
    print('This list do not contains a 5')
print(b, 'integers in the list are less than 5')



