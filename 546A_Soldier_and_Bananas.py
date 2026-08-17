k,n,w = map(int, input().split())
list = []
for x in range(1,w+1):
    res = k * x
    list.append(res)
borrow=sum(list)-n
if borrow < 0:
    print(0)
else:
    print(borrow)
 