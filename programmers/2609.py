
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b,a%b)

m,n = map(int,input().split())

print(gcd(m,n))
print(m*n//gcd(m,n))