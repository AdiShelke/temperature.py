# celcius = (c*9/5)+32f,f =(f-32)*5/9,c= c+273.15k,k = k-273.15c,f = (f-32)*5/9+273.15k,k =(k-273.15)*9/5+32--->formulas
print("What would you like to do")
print("1 for celcius to farenhite\n2 for celcius to kelvin\n3 for farenhite to celcius\n4 for farenhite to kelvin\n5 for kelvin to celcius\n6 for kelvin to farenhite")
user_input = int(input())
degree = float
if user_input == 1:
    degree = input("Temperature : ")
    temp = (float(degree)*9/5)+32
    print(temp,"F")
    
elif user_input == 2:
    degree = input("Temperature : ")
    temp = (float(degree)+273.15)
    print(temp,"K")
    
elif user_input == 3:
    degree = input("Temperature : ")
    temp = (float(degree-32)*5/9)
    print(temp,"C")
    
elif user_input == 4:
    degree = input("Temperature : ")
    temp = (float(degree-32)*5/9)+273.15
    print(temp,"K")
    
elif user_input == 5:
    degree = input("Temperature : ")
    temp = (float(degree)-273.15)
    print(temp,"C")
    
elif user_input == 6:
    degree = input("Temperature : ")
    temp = (float(degree)-273.15)*9/5+32
    print(temp,"F")