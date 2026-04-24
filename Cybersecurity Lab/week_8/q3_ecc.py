# Run this in SageMath (sagecell.sagemath.org)

p = 17
E = EllipticCurve(GF(p), [2, 2])

G = E(5, 1)
n = G.order()

d = randint(1, n-1)
Q = d * G

print("Private Key (d):", d)
print("Public Key (Q = d*G):", Q)

M = E(6, 3)
print("\nOriginal Message (Point):", M)

k = randint(1, n-1)
C1 = k * G
C2 = M + k * Q

print("\nEncrypted Message:")
print("C1 =", C1)
print("C2 =", C2)

M_dec = C2 - d * C1
print("\nDecrypted Message:", M_dec)
