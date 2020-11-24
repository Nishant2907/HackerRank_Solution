import cmath

x = complex(input())
r = abs(complex(x))
z = cmath.phase(x)
print(r)
print(z)