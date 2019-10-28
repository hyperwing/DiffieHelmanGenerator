# Finds the secret number

root = int(input('enter primitive root: '))
prime = int(input("enter common prime: "))

secretA = int(input("secret for person A: "))
secretB = int(input("secret for person B: "))

generateA = pow(root, secretA) % prime
generateB = pow(root, secretB) % prime

print("person A sends " + str(generateA))
print("person B sends " + str(generateB))

decodedA = str(pow(generateB, secretA) % prime)
decodedB = str(pow(generateA, secretB) % prime)

print("A decodes " + decodedA)
print("B decodes " + decodedB)

if (decodedA == decodedB):
    print("successfully made key pair")
else:
    print("failed to make matching keys")