d1={1:'A',2:'B','C':100,(10,20):'abc'}
print(type(d1))
print(d1)
# ###################get()################
print("===================================")
print(d1.get(2))
print(d1.get('C'))
# ###################keys()#############
print("===================================")
mykeys=d1.keys()
print(mykeys)
print(type(mykeys))
for k in mykeys:
    print(k)
# ##################values()###################
print("===================================")
myvalues=d1.values()
print(type(myvalues))
for v in myvalues:
    print(v)
# ##################items()####################
print("===================================")
myitems=d1.items()
print(type(myitems))
for k,v in myitems:
    print(k,v)
################update()#######################
print("===================================")
d1[1]='pqr'
d1[200]='xyz'
print(d1)
d2={400:'ttt',2:123}
d1.update(d2)
print(d1)
###################pop()########################
print("===================================")
print(d1)
d1.pop(1)
print(d1)
d1.popitem()
print(d1)
d1.popitem()
print(d1)
# ################copy()########################
print("===================================")
d1={1:'A'}
d2=d1.copy()
d2[1]='xyz'
print(d1)
print(d2)
print(id(d1))
print(id(d2))
