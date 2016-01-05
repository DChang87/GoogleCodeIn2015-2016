name = input("What is your name?")
weight = float(input("How much do you weigh in kg?"))
height = float(input("How tall are you in cm?"))
BMI = weight/((height/100)**2)
if BMI>25:
  print("You're overweight with a BMI of",BMI)
elif (BMI>=18.5):
  print("You're doing great with a BMI of",BMI)
else:
  print("You're underweight with a BMI of",BMI)
