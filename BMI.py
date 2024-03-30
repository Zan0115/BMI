h = float(input('your height : '))
w = float(input('your weight : '))
BMI = round(w / h ** 2.0, 1)
print(BMI)

if BMI < 18.5:
    print('Underweight')
elif BMI >= 18.5 and BMI < 24:
    print('Normal')
elif BMI >= 24 and BMI < 27:
    print('Overweight')
elif BMI >= 27 and BMI < 30:
    print('Obese Class I')
elif BMI >= 30 and BMI < 35:
    print('Obese Class II')
else:
    print('Obese Class III')