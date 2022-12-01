a = 0
b = 1
c = 11
print(a)
print(b)
for i in range(1,c+1):
    s = a+b
    a = b
    b = s
    print(s)