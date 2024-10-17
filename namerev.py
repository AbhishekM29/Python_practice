bill=float(input("enter bill"))

if(bill>=0 and bill<=100):

    unit=150
    print("unit and bill",unit)


elif(bill>=51 and bill<=100):

    unit=150+bill*1.5
    print("unit and bill",unit)

elif(bill>=101 and bill <=200):
    unit=150+bill*2
    print("unit and bill",unit)

elif(bill>=201 and bill<=300):
    unit=150+bill*3
    print("unit and bill",unit)

else:
    unit=300+bill*5
    print("unit and bill",unit)
