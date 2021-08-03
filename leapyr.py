year=int(input("Enter Year:"))
if (year>=0):
    if(year%4)==0:
        print("Leap Year")
    else:
        print("Not a leap year")
        
else:
    print("Year given is invalid")