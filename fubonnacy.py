def fubonacci():
    while True:
        try:
            number = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            print("please, try again")
            fubonacci()
        else:
            print("Thanks!")
            print("This is a list of your fubonacci number :")
            break
    list = []
    x=0
    y=1
    for a in range(number):
        x = x+y
        y = x+y
        list.append(x)
        list.append(y)
    print (list[0:number])
