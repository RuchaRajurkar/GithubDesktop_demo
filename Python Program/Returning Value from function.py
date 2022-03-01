# Return only one value
def add(x,y):
    a=x+y
    return a
p=add(2,4)
print("Addition is:",p)
print("====================================")

# Return Multiple values
def add(x,y):
    a=x+y
    b=x-y
    return a,b
p,q=add(2,4)
print("Addition is:",p)
print("Subtraction is:",q)
print("====================================")


