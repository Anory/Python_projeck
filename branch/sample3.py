a = 1 == 1  # True
b = 1 > 2  #
c = 8 > 5
d = 5 == 7

print(a, b, c, d)
r1 = a and b
r2 = a or b
r3 = not a
print(r1)
print(r2)
print(r3)

r4 = a and b or c and not d
# a and b or c and True
# False or c and True
# False or True
# True
print(r4)
