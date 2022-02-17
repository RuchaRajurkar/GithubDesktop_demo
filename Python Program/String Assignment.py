# Write a python program to calculate the length of a string
s1=input("Enter the string")
s2=len(s1)
print(s2)
print("===============================================")

# Write python program to count the number of characters (character frequency)in a string.
s1=input("Enter the string")
d1={}
for x in s1:
    a=s1.count(x)
    d1[x]=a
print(d1)
print("===============================================")

# Write python program to get a string made of first 2 and last 2 chars from a given a string.
# If the string length is less than 2,return instead of the empty string
s1=input("Enter the string")
if len(s1)>2:
    print(s1[:2])
    print(s1[-2::])
else:
    print(s1)
print("===============================================")

# Write python program to get a string from a given string where all the occurrences of its
# first char have been changed to '$',except the first char itself
s1=input("Enter the string")
x=s1.find(s1[0])
x=s1.find(s1[0],x+1)
s2=s1.replace(s1[0],'$')
s3=s2.replace('$',s1[0],1)
print(s3)
print("===============================================")

# Write python program to get single string from two given string , separated by a space and swap the first two
# character of each string
s1=input("Enter the string")
s2=input("Enter the string")
s3=s1+" "+s2
s4=s3.replace(s3[4],s3[0]).replace(s3[5],s3[1]).replace(s3[0],s3[4],1).replace(s3[1],s3[5],1)
print(s4)
print("===============================================")

# Write python program to add 'ing' at the end of a given string (length should be at least 3).If the
# given string already ends with 'ing' then add 'ly' instead.If the string length of the given string is less than
# 3,leave it unchanged.
s1=input("Enter the string")
if len(s1)>=3:
     if s1[-3:]=='ing':
         print(s1+'ly')
     else:
         print(s1+'ing')
else:
    print(s1)
print("===============================================")


# Write Python function that takes a list of words and return the length of the longest one
s1 = ["aaaaaaa", "aa", "bbbbttttta", "ads", "oaaa"]
prev = len(s1[0])

for ele in s1:
    a = len(ele)
    if a > prev:
        prev = a

print(prev)
print("===============================================")

# Write python program to remove the nth index character from nonempty string.
s1=input("Enter the string")
s2=int(input("Enter the index"))
s3=list(s1)
del(s3[s2])
print("".join(s3))
print("===============================================")

# Write a python program to change a given string to a new string where the
# first and last chars has been exchanged
s1 = input("Enter the string")
s1=s1.replace(s1[-1],s1[0]).replace(s1[0],s1[-1],1)
print(s1)
print("===============================================")

# Write a python program to count the occurrences of each word in the given sentences
s1 = input("Enter the string")
s3=s1.split(" ")
s4=[]
for ele in s3:
    if ele not in s4:
        s2 = s3.count(ele)
        s4.append(ele)
        print(ele,":",s2)
print("===============================================")

# Write a python program that accepts a comma separated sequence of words as input and
# print the unique words in sorted form
s1= ['red','white','black','red','green','black']
s2=[]
for ele in s1:
     if ele not in s2:
          s2.append(ele)
          s2.sort()
print(s2)
print("===============================================")