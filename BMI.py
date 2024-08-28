print("================================")
print("""Body Mass Index Calculator(BMI)""")
print("================================")

weight=int(input("enter your weight in kg: "))
print("enter your height in feet:")
heightInFeet=int(input("enter feet: "))
heightInInches=int(input("enter inches: "))
#covert height from feet to inches
feetTOInches=(heightInFeet*12)+heightInInches
#convert height from inches to meter
inchesToMeter=feetTOInches*0.0254
#calculate BMI
BMI= weight/(inchesToMeter**2)
print("--------------------------------")
print(f"""your BMI is "{BMI}" """)

if BMI<18.5 :
    print("""you are "UnderWeight" """)
elif BMI>=18.5 and BMI<=24.9:
    print("""you have "Normal weight" """)
elif BMI>=25.0 and BMI<=29.9: 
    print("""you are "overweight" """)
elif BMI>30.0: 
    print("""you are obese""")     
print("--------------------------------")