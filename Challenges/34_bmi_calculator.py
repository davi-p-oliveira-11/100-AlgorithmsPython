'''
 34) The Body Mass Index (BMI) is a value calculated based on a person's height and weight. 
According to the BMI value, we can classify the individual within certain ranges.   

below 18.5: Underweight
between 18.5 and 25: Normal weight   
between 25 and 30: Overweight
between 30 and 40: Obese
above 40: Morbidly obese 

Note: BMI is calculated by the expression weight/height² (weight divided by height squared).
'''

weight = float(input('Enter your weight in kgs: '))
height = float(input('Enter your height in meters: '))

bmi = weight / height ** 2

if bmi < 18.5:
    print(f'Your BMI is {bmi:.2f} — you are underweight.')
elif 18.5 <= bmi <= 24.9:
    print(f'Your BMI is {bmi:.2f} — you have normal weight.')
elif 25 <= bmi <= 29.9:
    print(f'Your BMI is {bmi:.2f} — you are overweight.')
elif 30 <= bmi <= 39.9:
    print(f'Your BMI is {bmi:.2f} — you are obese.')
elif bmi > 40:
    print(f'Your BMI is {bmi:.2f} — you are morbidly obese.')



input("Press Enter to exit ... ")
