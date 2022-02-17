mylist=[1,2,3,4,5]
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)


mylist1=["aaaaa","bbbbbbbb","c"]
print(mylist1)
mylist1.sort(key=len)
print(mylist1)

def mysort(y):
    return y%7
mylist3=[2,4,14,7]
print(mylist3)
mylist3.sort(key=mysort)
print(mylist3)

def xyz(x):
    return x[1]
mylist4=[[1,4],[3,8],[5,6],[7,7]]
print(mylist4)
mylist4.sort(reverse=True)
print(mylist4)
mylist4.sort(key=xyz)
print(mylist4)