def removeConsecutiveDuplicates(string):
    # Please add your code here
    if len(string)<=1:
        return string
    s2= removeConsecutiveDuplicates(string[1:])
    if string[0] == string[1]:
        return s2
    else:
      return string[0] +s2  
        
        
# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
