total = int(input("Enter total number of days : "))

years = total//365
months = (total%365)//30
days =(total%365)%30

print(years,months,days)