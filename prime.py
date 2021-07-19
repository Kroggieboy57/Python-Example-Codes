number=int(input("Enter Your number:"))
flag=False

if int(number) > 1:
    for i in range(2,int(number)-1):
        if int(number)%i==0:
            flag=True
            break

if flag==False:
    print("Prime")
else:
    print("Not Prime")