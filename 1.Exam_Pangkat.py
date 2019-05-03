def pangkat(x,y):   
    i = 0
    a = 1
    while i < y:    
        b = a * x
        a = b
        i+=1
    return a

print(pangkat(2,3))
print(pangkat(3,3))
print(pangkat(10,5))