#######################creating set#####################
s1={10,20,30,40,'A',1.2,(1,2,3)}
print(type(s1))
print(s1)
print("===============================================")
#####################create empty set using set function############
s1=set()
print(type(s1))
print("===============================================")
#################create set object by using set function and list data###########
s2=set([10,20,30])
print(s2)
print(type(s2))
s4=set({1:'a',2:'a'})
print(s4)
print("===============================================")
##################Set Methods()##############
##############add()###################
s1={10,20,30,40}
s1.add(123)
print(s1)
print("===============================================")
##############update()###############
s1.update([1,2,3])
print(s1)
s1.update("abc")
print(s1)
print("===============================================")
################remove()###############
s1.remove("a")
print(s1)
print("===============================================")
#############discard()##################
s1.discard(150)
print(s1)
print("===============================================")
############set operation############
s1={9,2,8,0,5,6}
s2={6,5,2}
print(s1 | s2)
print(s1&s2)
print(s1-s2)
print(s1^s2)
print("===============================================")
###########isdisjoint()#####################
print(s1.isdisjoint(s2))
print("===============================================")
###########issubset()####################
print(s2.issubset(s1))
print("===============================================")
###########issuperset()####################
print(s2.issuperset(s1))
print("===============================================")
