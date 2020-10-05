"""#empty List
#mylist=[]
#mylist=list()
#print(mylist)

mytuple=()
mytuple=tuple()
print(mytuple)

#mytuple=(1,2,3)             #homo

#mytuple=(1,"hi","2.32")         #hetrogeneous
mytuple=(1,2,3,[4,5,6],(1,2,4))
print(mytuple)

#mytuple=1,2,3
mytuple=(1,)
print(type(mytuple))   #if multiple values have assign to a singlr var it is a tuple

mytuple=(1,2,3)
#mytuple.append(4)   #not working
mytuple[0]=(4) #not working
print(mytuple)

mytuple=(1,2,3,1,2)
#print("Count= ",mytuple.count(1),"Index=",mytuple.index(3))
print(len(mytuple))

t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)"""
mytuple=(1,2,3)   #create a tuple
l=list(mytuple) #type casted into a list
del l[2]  #provide specific location
print(1)   # printed updated list