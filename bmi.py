weight = int(input('what is your weight?'))
height = int(input("what is your height? (in inches)"))

BMI = ((weight*703)/(height**2))
BMIS = str(BMI)
print("you have a BMI of " + BMIS)

if BMI < 18.5:
    print ("You are a weee bit underweight")
if BMI > 18.5 and BMI < 25:
    print ("you're healhty!")
if BMI > 25:
    print ("you need to lose some weight")
 