s= str(input())
x= s.split("+")
def sort(x):
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] >= x[j]:
                x[i], x[j] = x[j], x[i]
    print("+".join(x))
sort(x)