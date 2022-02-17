##############Types of function#############
##############function withuot Arguments##########
def add():
    s1=int(input("Enter the number:"))
    s2=int(input("Enter the number:"))
    s3=s1+s2
    print("Addition is",s3)
add()
print("===============================================")

#############fix Argument#################
def add(s1,s2):
    s3=s1+s2
    print("Addition is",s3)
add(5,4)
add(1.5,2.4)
add(50,40)
print("===============================================")

##############Default Arguments##############
def add(s1=1,s2=6):
    s3 = s1 + s2
    print("Addition is",s3)
add()
add(5,4)
add(4)
print("===============================================")

###############Keyword Arguments############
def add(s1,s2):
    print("Value of s1:",s1)
    print("Value of s2:",s2)
    s3=s1+s2
    print("Addition is",s3)
add(s2=5,s1=4)
add(1.5,2.4)
add(50,40)
print("===============================================")

##################Arbitary Arguments############
def show (*names):
    print("===============================================")
    print(names)
    for x in names:
        print(x)
show("a","b","c")
show("a","b")
show("a")