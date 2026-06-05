def evenly_divisible(a,b,c):
    total=0
    for i in range(a,b+1):
        if i%c==0:
            total+=i
    return total
print(evenly_divisible(1,10,2))
print(evenly_divisible(1,10,3))
print(evenly_divisible(1,10,4))
