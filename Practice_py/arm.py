a = int(input())
ans = a
temp = a
count = 0
sum = 0

while(temp>0):
    x = temp%10
    count +=1
    temp = temp//10
print(count)

while(a>0):
    y = a%10
    sum = sum+(y**count)
    a = a//10

if sum==ans:
    print("armstrong")

