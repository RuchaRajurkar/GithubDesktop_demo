def sqr(list1):
    temp=[]
    for x in list1:
            temp.append(x*x)
    return temp
mylist=[1,2,3,4,5,6,7,8,9,10]
list2=sqr(mylist)
print(list2)
print("=======================================")

mylist=[1,2,3,4,5,6,7,8,9,10]
list2=list(map(lambda x:x*x,mylist))
print(type(list2))
print(list2)
print("=======================================")

s1=input("Enter values:")
arr=s1.split(",")
list2=list(map(int,arr))
print(list2)

##########################################
list2=list(map(int,input("Enter values").split(",")))
print(list2)