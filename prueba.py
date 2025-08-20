a = 1
b = 2
c = 4

A = False
B = False
C = True

r1 = (2 * b - 1) / (2 * a) > 3
r2 = a * (b * c) >= 30 and not ((a + b) * c >= (350 * c))
r3 = A and r1 or B == r2
r4 = A and B and r3 and C != r1

print(f"{r2}, {r3}, {r1}, {r4}")