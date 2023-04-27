p = 0
def bmi(height, weight):

    #print("Height is: " + str(height))
    #print("Weight is: " + str(weight))

    heightm = height / 100

    value1 = heightm * heightm
    value2 = weight / value1

    print("BMI is: " + str(value2))

    if value2 <18.5:
        print("Under weight")
    elif value2 >=18.5 and value2 <25:
        print("Normal Weight")
    else:
        print("Over weight")



heit = input("Your height is: ")
print ("Height is: " + heit)
het = int(heit)
weit = input("Your weight is: ")
print ("Weight is: "+ weit)
wei = int(weit)
bmi(het, wei)



