#AMSTRONG
l=int(input("enter a number"))
v=int(input("enter a number"))
for  num in range(l,v+1):
    t=num
    sum=0
    while t >0:
        x=t%10
        c=x*x*x
        sum+=c
        t=t//10
    if (num == sum):
        print(sum)
        break
        


            
                
                
            
            
    
    


