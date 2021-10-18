list_a = ['cat', 'dog', 'chicken', 'cow', 'horse']
list_n = ['3','5','22','13','9']

def mysort(mylist = [], numflag = False):
    if numflag == False:
        mylist.sort(key = lambda x: x[0])
    else:
        mylist.sort(key = len)
    return print(mylist)

mysort(list_a, True)
mysort(list_n, True)

print('DONE')
