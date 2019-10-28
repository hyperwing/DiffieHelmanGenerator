import math

def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1


root = int(input('enter primitive root: '))
prime = int(input("enter common prime: "))

generateA = int(input('enter public string A sends to B: '))
generateB = int(input("enter public string B sends to A: "))

print(modInverse(generateA, prime))
print(pow(root, 3) % prime)

print("A key: "+str(math.log(modInverse(generateA, prime),2)/math.log(root,2)))
print("B key: "+str(math.log(modInverse(generateB, prime),2)/math.log(root,2)))