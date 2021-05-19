def geometricsum(n):
    if n<0:
        return 0
    else :
        count=1/2**n
        return count+geometricsum(n-1)
   
n=int(input())
print ('%.5f'%geometricsum(n))
