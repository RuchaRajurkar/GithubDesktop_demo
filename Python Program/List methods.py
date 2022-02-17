#########################List Methods################################

mylist=[1,2,3,4,5]
#append()
mylist.append(5)
mylist.append("abc")
mylist.append([1,2,3])
print(mylist)
print("================================")

#extends()
mylist.extend([4,5,6])
print(mylist)
print("================================")

#insert()
mylist.insert(2,8)
print(mylist)
print("================================")

#remove()
mylist.remove(5)
print(mylist)
for x in mylist:
    if x==5:
        mylist.remove(x)
print(mylist)
print("================================")

#pop()
x=mylist.pop(2)
print(x)
print(mylist)
print("================================")

#count()
x=mylist.count(5)
print(x)
print("================================")

#reverse()
mylist.reverse()
print(mylist)
print("================================")

