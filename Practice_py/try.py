for i in range(0,101):
    d=0
    a=i
    count=0

    while(a>0):
        x=a%10
        d=d+(x*(10**count))
        a=a//10
        count=count+1
    
    if(d==i):
        s=0
        b=i
        while(b>0):
            y=b%10
            s=s+y
            b=b/10
    if(s==i):
        print(i)