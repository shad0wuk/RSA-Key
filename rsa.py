def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

p,q = 17, 11
n = p*q
phi = (p-1)*(q-1)
e = int(input("Enter the value of e: "))
if (e > 1 & e < phi) & gcd(e,phi) == 1: 
    k = 1
    d = (1 + (k*phi))/e
    if ((d*e) % phi == 1) & (d < phi):
        PU = (e,n)
        PR = (d,n)
        print("Public key is: ", PU)
        print("Private key is: ", PR)
    else:
        print("Invalid d")
else:
    print("Invalid e")