#Get Rich Quick Agency
dep_amt=10000             #dep_amt is principle
apr=6                   #Annual Percentage Rate (APR)
period=5                 #period in years
totalinterest=0
interest=dep_amt/(period*0.01*apr)
for x in range(period):
    print("Year ",x+1)
    print("beigning principle= ",dep_amt)          #beigning principle
    interest=dep_amt*apr
    print("Interest = ",interest)
    
    dep_amt=dep_amt+interest
    totalinterest=totalinterest+interest
print("Principle= ",dep_amt)
print("totalinterest= ",totalinterest)
