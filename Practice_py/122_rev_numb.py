a = 1234
temp = a
s = 0
while(temp!=0):
    x = temp%10
    temp = temp//10
    s = s*10+x
print(s)

if(s==a):
    print("palindrome")

