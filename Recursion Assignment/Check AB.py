def check(s,i,l):
    if l==1 :
        if s[0]!="a" :
            return "false"
        else:
            return "true"
            
    if i==(l-2):
        return "true"
    if s[0]!="a":
        return "false"
    if s[i]=='a':
        if s[i:i+3]!="abb" and s[i:i+2]!="aa":
            return "false"
    if s[i]=="b":
        if s[i:i+3]!="bba" and s[i:i+2]!="ba":
            return "false"
    i+=1
    return check(s,i,l)
s=input()
print(check(s,0,len(s)-1)) 
