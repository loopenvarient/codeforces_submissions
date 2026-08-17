n= str(input()).lower()
m= str(input()).lower()
for __ in range(len(n)== len(m)):
    if n[0:len(n)]== m[0:len(m)]:
        print("0")
    elif n[0:len(n)]> m[0:len(m)]:
        print("1")
    else:
        print("-1")
    