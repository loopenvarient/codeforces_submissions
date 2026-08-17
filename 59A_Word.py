n= str(input())
count=0
for x in range(len(n)):
    if n[x].isupper():            
        count+=1
    if count>len(n)/2:              
        print(n.upper())
        break
else:                           
    print(n.lower())