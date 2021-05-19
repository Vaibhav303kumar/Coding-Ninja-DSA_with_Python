l=input().split()
N=int(l[0])
P=int(l[1])
def power(N, P): 
  
    # if power is 0 or 1 then number is returned 
    if(P == 0): 
        return 1 
    else: 
        return (N*power(N, P-1)) 

print(power(N,P))
