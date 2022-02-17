I = 34
s1="This is string"
print(len(s1))
for i in range(len(s1)):
    print(s1[i])
print(s1[2:8:1])
print(s1[2:8])
print(s1[::-1])
print(s1[-1])
print("======================================")
###################################
name="abc"
age=34
s1="Hello"+" "+name+" "+"Your age is"+" "+str(age)
print(s1)
s2="Hello {0} your age is {1}".format(name,age)
print(s2)
s3=f"Hello {name} your age is {age}"
print(s3)
print("======================================")
###############count()##################
s1="This is demo.This is my string handling program"
x=s1.count("is")
print(x)
x=s1.count("is",8)
print(x)
print("======================================")
##############find()####################
s1="This is demo.This is my string handling prog"
x=s1.find("is")
print(x)
x=s1.find('is',x+1)
print(x)
print("======================================")
###############split()###############
s1="a,b,hello,d,e,f,g"
arr=s1.split(" ")
print(arr)
print("======================================")
#############################
s2="Thisisdemo"
arr2=list(s2)
print(arr2)
print("======================================")
############capitalize()###########
s3="this IS demo"
print(s3.capitalize())
print("======================================")
########lower()##################
print(s3.lower())
print("======================================")
###########upper()###############
print(s3.upper())
print("======================================")
#############swapcase()#########
print(s3.swapcase())
print("======================================")
###########title()#################
print(s3.title())
print("======================================")
##########endwith()##############
print(s3.endswith("th"))
print("======================================")
##########startwith()#########
print(s3.startswith("t"))
print("======================================")
#########Difference between index() and find()##############
print(len("IS"))
z=s3.index("IS")   ##Exact match is not found then will give error
print(z)
a=s3.find("z")    ##Exact match is not found then will give (-1) not error
print(a)
print("======================================")
###########rfind()#################
b=s3.rfind("e")
print(b)
print("======================================")
#############isalnum()#############
print(s3.isalnum())
print("======================================")
#############isalpha()###############
print(s3.isalpha())
print("======================================")
#############isdigit()##########
c="123457"
print(c.isdigit())
print("======================================")
##############isspace()############
print(c.isspace())
print("======================================")
###########isupper()##################
s4="THIS IS DEMO"
print(s4.isupper())
print("======================================")
############islower()################
print(s4.islower())
print("======================================")
############center()################
print(s4.center(50,'*'))
print("======================================")
##############ljust()###############
print(s4.ljust(50,'*'))
print("======================================")
##############rjust()###############
print(s4.rjust(50,'*'))
print("======================================")
################lstrip()###############
p=" HELLO WORLD "
print(p.lstrip())
print("======================================")
################rstrip()###############
print(p.rstrip())
print("======================================")
###############strip()################
print(p.strip())
print("======================================")
#################join()#################
mylist=["Hello","World","This","Is","Demo"]
s5=" "
for x in mylist:
    s5+=" "+x
print(s5.strip())
#####(or)#####
s5=" ".join(mylist)
print(s5)
print("======================================")
##############replace()##################
s6="This is demo.This is string program"
print(s6)
s6=s6.replace('is','IS')
print(s6)
s7=s6.replace('IS','is',2)
print(s7)
print("======================================")