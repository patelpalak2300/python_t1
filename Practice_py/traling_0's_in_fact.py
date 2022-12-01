num = int(input())

x =num//5
y=x
while x>0:
    x = x//5
    y = y+x

print(y)