distance= int(input())
moves=0 
while distance>0:
    if distance>=5:
        distance-=5
        moves+=1
    else:
        distance-=distance
        moves+=1
print(moves)