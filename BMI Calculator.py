
         

def bmi(weight_kg,height_m):
     bmi = weight_kg/height_m**2
    ## complete your work here ##

    ## return something for now
     return bmi

def print_bmi_level(bmi):
    if (bmi<18.5):
        print("underweight")
    elif (18.5<=bmi<25):
        print("normal weight")
    elif (25<=bmi<30):
        print("over weight")
    elif (25<=bmi<30):
        print("over weight")
    else:
        print("obese")

    

w_kg= float(input("Enter your weight in kilograms "))
h_m= float(input("Enter your height in meters "))

r = bmi(w_kg,h_m)
print("Your BMI is", r)
print_bmi_level(r)



