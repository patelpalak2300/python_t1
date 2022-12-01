#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a=int(input('Enter Value of base :'))
b=int(input('Enter Value of height :'))
Area=(a*b*0.5)
print(f'area of triangle is {Area}')


# In[9]:


a=4%2
b=2**5
print(a)
print(b)


# In[ ]:


#WAP to find length of hypotenuse of a right angled triagle
import math
a = int(input('Enter Height '))
b = int(input('Enter Base'))
c =math.sqrt((a**2) + (b**2 ))
print(c)


# In[11]:


#WAP Area of circle
from math import *
r = int(input('Enter radius '))
A = pi*(r**2)
print(format(A, '0.5f'))


# In[2]:


a=7
b=0
not a


# In[5]:


a=int(input ())

print('Young' if a<10==0 'Medium aged' elif 11<=a>=40 else 'Old')


# In[31]:


a='tree'
b='t'
print(ord('A'))
a<b


# In[38]:


a=10
a*=19
print(a)


# In[1]:


#wap to swap two letters
a=5 
b=4
a= a+b
b=a-b
a=a-b
print(a)
print(b)


# In[19]:


a = "Hello"
"e" in a


# In[22]:


# wap to find surface area of a cylinder and its volue use fstring method to print th output


# In[27]:


from math import *
r= int (input('enter radius : '))
h= int (input('enter height : '))
surface_area = 2*pi*r*r + 2*pi*r*h
volume=pi*r*r*h
print (f'surface area of cynlinder is {surface_area:0.2f}')
print (f'volume of cynlinder is {volume:0.2f}')


# In[31]:


#wap to get an int value from user which gives output in the form of binary,hexadecimal and octal
a= int(input("Enter Number : "))
print(f'Binary {bin(a)}')
print(f'Hexadecimal {hex(a)}')
print(f'Octal {oct(a)}')


# In[10]:


#wap to give the following output 
q = int(input("Enter quantity "))
v = int(input("Enter Value "))
total_value = q*v
discount = int(input("Enter discount "))
Amount = total_value - (total_value*discount)/100
Tax = int(input("Enter tax"))
Final_Amount = Amount + (Amount*Tax)/100
print('\n********************************')
print(format('Bill\n','^32'))
print(f'Quantity {q}')
print(f'Value {v}Rs.')
print(f'Total_Value {total_value}Rs.')
print(f'Discount {discount}%')
print(f'Amount  {Amount}Rs.')
print(f'Tax  {Tax}%')
print(f'Final Amount {Final_Amount:0.0f}Rs.')


# In[9]:


#wap to find square root of complex no. 
from cmath import *
a= int (input ())
i= int(input ())
c=complex(a,i)
print(c)
sqrt = sqrt(c) 
print(sqrt)


# In[3]:


#wap to convert ferhanite to celcius
F = int(input('Ferhanite '))
celcius = (F-32)*5/9
print(f'celcius  {celcius}')


# In[5]:


print(*"PYTHON")


# In[18]:


print(r"c:\same\name")


# In[23]:


print('''ABC DEF GHI''')


# In[2]:


#WAP to find total amount collected in the pigi bank if there are Rs. 10,5,2,1 coins in it
a = int(input("Enter no. of Rs.10 coins"))
b = int(input("Enter no. of Rs.5 coins"))
c = int(input("Enter no. of Rs.2 coins"))
d = int(input("Enter no. of Rs.1 coins"))
total= (a*10)+(b*5)+(c*2)+d
print(f'total amount of Rs. in pigi bank is {total}Rs.')


# In[14]:


#WAP to find average of two user defined values and find its deviation
a=int(input("Enter No. 1 = "))
b=int(input("Enter No. 2 = "))
avg=(a+b)/2
dev_a=(a-avg)
dev_b=(b-avg)
print(f'avg = {avg}')
print(dev_a)
print(dev_b)


# In[8]:


import math
import cmath
a=int(input())
b=int(input())
c=int(input())
D=(b*b)-(4*a*c)
if (D>=0):
    print('Real Roots')
    Root_1=(-b + math.sqrt(D)/(2*a))
    Root_2=(-b - math.sqrt(D)/(2*a))
    print(f'Root_1 = {Root_1}')
    print(f'Root_2 = {Root_2}')
else:
    print('Complex Roots')
    Root_1=(-b + cmath.sqrt(D)/(2*a))
    Root_2=(-b - cmath.sqrt(D)/(2*a))
    print(f'Root_1 = {Root_1}')
    print(f'Root_2 = {Root_2}')


# 

# In[3]:


#Wap to get the number of base of the user which gives output in the form of years months and days 
a=int(input("Enter The No. of days = "))
Years=(a//365)
months=(a - (365*Years))//30
days= a- (365*Years + 30*months )
print(f'500 DAYS = {Years} Years {months} Months {days} Days')


# In[5]:


a=int(input("Enter The No. of seconds = "))
Hours=(a//3600)
minutes=(a - (3600*Hours))//60
seconds= a- (3600*Hours + 60*minutes )
print(f'{a} Seconds = {Hours} Hours {minutes} Minutes {seconds} Seconds')


# In[ ]:


a=int(input('Enter roll no. : '))
b=input("Enter Name : ")
c=bool(input("belogs to Branch CSE[True or false]"))
print(type(a))
print(b)
print(c)


# In[2]:


a=eval(input('Enter roll no. : '))
print(type(a))


# In[4]:


a=eval(input('Enter roll no. : '))
print(type(a))


# In[6]:


a=eval(input('Enter roll no. : '))
print(type(a))


# In[ ]:


a=eval(input('Enter roll no. : '))
print(type(a))


# In[1]:


print('sum = ', int(input())+int(input()))


# In[5]:


#wap to convert degrees to radian
from math import *
d=eval(input("enter degree "))
r=eval(input("enter radians "))
degrees= 180*r/pi
radians = pi*d/180
print(degrees)
print(radians)


# In[18]:


a,b,c=10,20,30
print(a,end=" , ")
print(b,end=" & ")
print(c)


# In[1]:


#wap to check whether a user defined no. is divisible 5 or not
a= int(input())
if(a%5==0):
    print("Divisible By 5")
else:
    print("Not divisible by 5")


# In[4]:


a=int(input())
if(a>0):
    print('Positive')
elif(a<0):
    print('Negative')
else:
    print('Zero')
b=int(input())
if(b>0):
    print('Positive')
elif(b<0):
    print('Negative')
else:
    print('Zero')
c=int(input())
if(c>0):
    print('Positive')
elif(c<0):
    print('Negative')
else:
    print('Zero')


# In[ ]:


#WAP to get the total score of indian cricket team if the runrate is greater than 8 the output should be High chance of win as the 
total_score=int(input('Enter the score '))
runrate=total_score/20
if(total_score>=200):
    print("INDIA V/S PAKISTAN FINAL")
if(runrate>=8):
    print(f'High chance of win as the runrate is {runrate}')
elif(7<=runrate<8):
    print(f'Medium chance of win as the runrate is {runrate}')
else:
    print(f'Low chance of win as the runrate is {runrate}')    


# In[2]:


#WAP input from  user between 1  and 7
a=int(input())
if(a>7 or a<1):
    print('Enter the bnumber Between 1 to 7')
elif(a==1):
    print('Monday')
elif(a==2):
    print('Tuesday')
elif(a==3):
    print('Wednesday')
elif(a==4):
    print('Thursday')
elif(a==5):
    print('Friday')
elif(a==6):
    print('Saturday')
else:
    print('Sunday')


# In[17]:


#WAP to generate an electricity bill
unit=float(input("Enter to No. of Units "))
print(f'Total Unit = {unit}')
if(unit<100):
    print('Total = 0')
elif(100<unit<=200):
    cost=(unit-99)*10
    print(f'Total cost = {cost} Rs.')
else:
    cost=101*10 + (unit-200)*15
    print(f'Total cost = {cost} RS.')


# In[4]:


price=int(input('Enter Show room price '))
if(price<=80000):
    tax=(price*7/100)
    Amount=price + (price*7/100)
    print(f'Total Tax = {tax}Rs.')
    print(f'On Road Price = {Amount}Rs.')
elif(price<=150000):
    tax=(price*15/100)
    Amount=price + (price*15/100)
    print(f'Total Tax = {tax}Rs.')
    print(f'On Road Price = {Amount}Rs.')
if(price>150000):
    tax=(price*18/100)
    Amount=price + (price*18/100)
    print(f'Total Tax = {tax}Rs.')
    print(f'On Road Price = {Amount}Rs.')


# In[21]:


#WAP to  enter any character from user which gives output in the form of whether the enetered character is uppercase or lowercase or digit
a1=(input())
if(a1>='0' and a1<='9'):
    print(f'{a1} is digit ')
elif('a'<=a1 and a1<='z'):
    print(f'{a1} is Lowercase')
elif('A'<=a1 and a1<='Z'):
    print(f'{a1} is Uppercase')
else:
    print("Enter Valid No. or Digit ")


# In[27]:


#WAP to check whether the user to vote or not,if not output shour no. ofn years to start voting
a=int(input())
if(a<18):
    print('You are not eligile to Vote')
    b=18-a
    print(f'Years left to be eligible for voting is {b}')
else:
    print('You Are eligible to vote')


# In[32]:


PS=int(input('Enter the marks of PS = '))
DE=int(input('Enter the marks of DE = '))
FSD_1=int(input('Enter the marks of FSD-1 = '))
PYTHON=int(input('Enter the marks of PYTHON = '))
ETC=int(input('Enter the marks of ETC = '))
totalmarks=125
marksobtained=PS+DE+FSD_1+PYTHON+ETC
percentage=(marksobtained/totalmarks)*100
print(f'Total percentage = {percentage}%')
if(percentage>=80):
    print("First Class")
elif(80<percentage>=70):
    print("Second Class")
elif(70<percentage>=600):
    print("First Class")
elif(percentage<60):
    print("PASS")


# In[43]:


salary=int(input("Enter Salary "))
gender=(input("Enter Gender "))
if(salary<=10000):
    if(gender=="MALE" or gender=="male"):
        bonus= (salary*0.07)
        print(f'Bonus = {bonus}Rs.')
    elif(gender=="FEMALE" or gender=="female"):
        bonus= (salary*12)/100
        print(f'Bonus = {bonus}Rs.')
    else:
        print("Enter Valid Gender")
else:
    if(gender=="MALE" or gender=="male"):
        bonus= (salary*5)/100
        print(f'Bonus = {bonus}Rs.')
    elif(gender=="FEMALE" or gender=="female"):
        bonus= (salary*10)/100
        print(f'Bonus = {bonus}Rs.')
    else:
        print("Enter Valid Gender")


# In[11]:


#wap to construct a calculator whick performs +,_,*,/,%,// from user defined values
print("Enter + for addition")
print("Enter - for subraction")
print("Enter * for multiplication")
print("Enter / for division")
print("Enter % for modulus")
print("Enter // for floor divivsion")
a=float(input())
choice=input()
d=float(input())
if(choice=="+"):
    ans=a+d
    print(f'Ans = {ans}')
elif(choice=="-"):
    ans=a-d
    print(f'Ans = {ans}')
elif(choice=="*"):
    ans=a*d
    print(f'Ans = {ans}')
elif(choice=="/"):
    ans=a/d
    print(f'Ans = {ans}')
elif(choice=="%"):
    ans=a%d
    print(f'Ans = {ans}')
elif(choice=="//"):
    ans=a//d
    print(f'Ans = {ans}')
else:
    print("Enter Valid Operator")


# In[14]:


#WAP to get a character from a user and defined whether it is a vovwl or consonant
a=(input("Enter alphabet "))
A=('a','e','i','o','u','A','E','I','O','U')
if(a in A):
    print(f'{a} is Vowel')
else:
    print("Entered Alphabet is consonant")


# In[15]:


a=int(input("Enter the year "))
if(a%100!=0):
    if(a%4==0):
        print(f'{a} Year is a Leap year')
    else:
        print(f'{a} Year is a Leap year')
else:
    if(a%400==0):
        print(f'{a} Year is a Leap year')
    else:
        print(f'{a} Year is a Leap year')
    


# In[3]:


import calendar
a=int(input("Enter the year "))
if(calendar.isleap(a)):
    print("It is a leap year")
else:
    print("It is not a leap year")


# In[2]:


#WAP to get 2 no. from user which shows satrting and ending range and find all the no. divisible by 3
a=int(input("start = "))
b=int(input("End = "))
div=int(input("Enter the divivble by no. "))
count=0
for c in range(a,b+1):
    if(c%div==0):
        count+=1
        print(c)
print(f'count = {count}')


# In[5]:


#WAP to get an int value from user and print it multiplication table
a=int(input("Table = "))
count=0
for c in range(1,11):
    print(f'{a} x {c} = {a*c}')


# In[15]:


#WAP to get a int value from user which gives the sumation of all natural no. 
a=int(input())
sum=1
for c in range(1,a+1):
    sum*=c
print(f'factorial = {sum}')


# In[16]:


#WAP to get a user defined range which print all values except divisible by 3 & 6


# In[21]:


a=int(input("start = "))
b=int(input("End = "))
count=0
for c in range(a,b+1):
    if(c%3==0 or c%6==0):
        continue
    count+=1
    print(c)
print(f'count = {count}')


# In[27]:


#WAP to get 3 no. from users which prints the max od these 3
a=(int(input()))
b=(int(input()))
c=(int(input()))
if(a>b and b>c):
    print(f'{a} is max')
elif(b>c and a<c):
    print(f'{b} is max')
else:
    print(f'{c} is max')


# In[ ]:


#WAP to get an integer from user which printd the sum of all individual digits
a=int(input())
sum=0
while(a>0):
    d= a%10
    sum+=d
    a//=10
print(sum)
    


# In[9]:


#WAP to get 3 no. from user and print then in ascending order
a=int(input())
b=int(input())
c=int(input())
if(a>b):
    a,b=b,a
    if(b>c):
        b,c=c,b
        a,b=b,a
        print(f'{a},{b},{c}')
    else:
        
        print(f'{a},{b},{c}')
else:
    if(b>c):
        b,c=c,b
        print(f'{a},{b},{c}')
    else:
        print(f'{a},{b},{c}')


# In[4]:


#WAP to get an int value from user check if it is a 3 digit no. or not if it is a 3 digit no. the output should print the middle digit
a=int(input())
count=0
d=a
while(d>0):
    count+=1
    d=d//10
    
if(count==3):
    b=a//10
    c=b%10
    print(f'middle no. is {c}')
print(f' count = {count}')


# In[3]:


#WAP to printfibonacci series upto nth no.
n=int(input())
a=0
b=1
for i in range(2,n):
    s=a+b
    print(a)
    a=b
    b=s


# In[10]:


#WAP to get an int value from user and print its reverse
a=int(input())
while(a>0):
    d= a%10
    reverse=d
    a//=10
    print(reverse,end="")


# In[20]:


a=int(input())
b=a
reverse=0
while(a>0):
    d= a%10
    reverse=reverse*10 + reverse
    a//=10
print(reverse)
if(reverse==b):
    print("the given no. is palindrome")


# #WAP to get 10 int input from user in a loop and print the sum and avg
# sum=0
# while(a>-1):
#     a=int(input())
#     sum=sum+a
# avg=sum/10
# print(f'sum = {sum}')
# print(f'avg = {avg}')

# sum=0
# count=0
# for i in range(i>-1):
#     a=int(input())
#     sum=sum+a
#     count+=1
# avg=sum/count
# print(f'count = {count}')
# print(f'sum = {sum}')
# print(f'avg = {avg}')

# 

# In[5]:


sum=0 
count=0
while(True):
    a=int(input())
    if(a==-1):
        break
    else:
        count+=1
        sum=sum+a 
avg=sum/count 
print(f'count = {count}')
print(f'sum = {sum}') 
print(f'avg = {avg}')


# In[13]:


#WAP to get initial value of investment and rate of interest from user take no. of years
a=int(input("Investment = "))
b=int(input("For How many Years= "))
c=float(input("Rate of interest = "))
total_amount=a
for i in range(1,b+1):
    interest=(a*c)/100
    total= a + interest
    print(f'After year {i} amount will be {total}')
    a=total


# In[37]:


a=int(input())
b=int(input())
count=0
for i in range(a,b+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)


# In[9]:


a=int(input())
sum=1
for c in range(1,a+1):sum*=c
print(f'factorial = {sum}')
count=0
while(a>0):
    a=a//5
    count+=a
print(f'count = {count}')


# In[12]:


a=int(input("Enter Rupees"))
total_notes=0
temp=a
while (a>0):
    while(a>=500):
        temp=a//500
        total_notes=temp+total_notes
        a=a-temp*500
    while(a>=200):
        temp=a//200
        total_notes=temp+total_notes
        a=a-temp*200
    while(a>=100):
        temp=a//100
        total_notes=temp+total_notes
        a=a-temp*100
    while(a>=50):
        temp=a//50
        total_notes=temp+total_notes
        a=a-temp*50
    while(a>=20):
        temp=a//20
        total_notes=temp+total_notes
        a=a-temp*20
    while(a>=10):
        temp=a//10
        total_notes=temp+total_notes
        a=a-temp*10
print(f'Total notes = {total_notes}')
        


# In[16]:


n,sum=eval(input()),0
print("1",end="")
for i in range(2,n+1):
    print(f' + 1/{i}',end="")
    sum=sum+(1/i)
print(f' sum = {sum}')


# In[1]:


for i in range (1,51):
    if(i%3==0 and i%5==0):print("fizzbizz")
    elif(i%3==0):print("fizz")
    elif(i%5==0):print("Buzz")
    else:print(i)


# In[70]:


for i in range(0,5):
    for j in range(i+1):
        print("*",end=" ")
    print(" ")


# In[71]:


for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print(" ")


# In[48]:


for i in range(5):
    for k in range(5-i):
        print(" ",end=" ")
    for j in range(i+1):
            print("*",end=" ")
    print()


# In[50]:


for i in range(5):
    for k in range(5-i):
        print(" ",end="")
    for j in range(i+1):
            print("*",end=" ")
    print()


# In[69]:


for i in range(5,0,-1):
    for j in range(1,i):
        print(j,end=" ")
    print(" ")


# In[72]:


for i in range(5,0,-1):
    for k in range(6-i):
        print(" ",end="")
    for j in range(i):
            print("*",end=" ")
    print()


# In[78]:


for i in range(6):
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")


# In[83]:


for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")


# In[91]:


for i in range(6):
    for j in range(1,i+1):
        if i%2==0:
            print("#",end=" ")
        else:
            print("*",end=" ")
    print(" ")


# In[ ]:





# In[100]:


print(print(print(*"PYTHON")))


# In[ ]:




