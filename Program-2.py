n = int(input("Input an integer:"))
sum_int=0  
while float(n)/10 >= .1:   
    r= n%10
    sum_int += r
    n= n//10   
    if float(n)/10 > .1: print(r,  end= " + ") 
    else: print(r,"=",sum_int)
