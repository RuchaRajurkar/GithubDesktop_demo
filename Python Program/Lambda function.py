def sqr(x):
    y=x*x
    return y
a=sqr(12)
print(a)
print("==================================")

sqr=lambda x:x*x
print(type(sqr))
a=sqr(12)
print(a)
print("==================================")

add=lambda a,b,c:a+b+c
print(add(3,6,4))