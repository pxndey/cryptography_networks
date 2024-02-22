import numpy

p = int(input("enter p "))
q = int(input("enter q "))

n=p*q

def findGCD(n1,n2):
    gcd=1
    if n1>n2:
        for i in range(2,n2):
            if n1%n2==0:
                gcd=i
    else:
        for i in range(2,n1):
            if n2%n1==0:
                gcd=i
    return gcd

phi_pq=((p-1)*(q-1))
while True:
    e=numpy.random.randint(1,phi_pq)
    if findGCD(e,phi_pq)==1:
        break

print(e)
print(phi_pq)

public_key=(e,n)
private_key= (0,0)

#brute forcing for d
for d in range(2,100000000):
    exp = (e*d)%(phi_pq)
    if exp==1:
        private_key= (d,n)
        break

print(private_key)
print(public_key)
