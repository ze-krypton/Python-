# Run this in SageMath (sagecell.sagemath.org)

p = 17
E = EllipticCurve(GF(p), [2, 2])

G = E(5, 1)
n = G.order()

print("Elliptic Curve:", E)
print("Base Point G:", G)

a = randint(1, n-1)
b = randint(1, n-1)

A = a * G
B = b * G

print("\nAlice's Private Key:", a)
print("Bob's Private Key:", b)
print("\nAlice's Public Key:", A)
print("Bob's Public Key:", B)

ka = a * B
kb = b * A

print("\nShared Secret computed by Alice:", ka)
print("Shared Secret computed by Bob:", kb)
print("\nKeys match?", ka == kb)
