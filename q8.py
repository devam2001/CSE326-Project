s = ""    
for i in range(0,7):    
    for j in range(0,7):     
        if (j==1 or ((i==0 or i==6) and (j>1 and j<5)) or (j==5 and i!=0 and i!=6)):    
            s=s+"*"    
        else:      
            s=s+" "    
    s=s+"\n"    
print(s)
