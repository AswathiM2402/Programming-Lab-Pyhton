year=int(input("Enter the starting year:"))
limit=int(input("Enter the limit:"))
while(year<=limit):
    if(year%4==0 and year%100!=0 or year%400==0):
        print(year)
    year=year+1