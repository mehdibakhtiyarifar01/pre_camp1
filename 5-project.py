length=int(input("enter length : "))
height=int(input("enter height :"))

for i in range(1,height+1):
    for j in range(1, height - i +1):
        print(end=' ')
    if i == 1 or i ==height:
        for j in range (1,length+1):
            print("*",end="")
    else:
        for j in range(1,length+1):
            if j==1 or j==length:
                print("*",end="")
            else:
                print(end=' ')


    print()