# -*- coding: utf-8 -*-
"""BodyMassIndex

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JVraXaRCz1x0HJWpzNvy3_idtQLtWhaS
"""

Weight = float(input("Enter Your Weight(in kgs) :"))
Height = float(input("Enter Your Height(in m) :"))
if Weight <= 0 or Height <= 0:
    print("Please enter valid positive numbers for weight and height.")
else:
  BMI = Weight / (Height*Height)
  if BMI < 18.5 :
    Category = "Underweight"
    Direction = "Consider gaining weight to reach a healthier range."
  elif 18.5 <= BMI <= 24.9:
    Category = "Normal"
    Direction = "Great job! Keep maintaining your current weight."
  elif 25 <= BMI <= 29.9:
    Category = "Overweight"
    Direction = "Consider losing weight to improve your health."
  elif 30 <= BMI :
    Category = "Obese"
    Direction = "It's important to work towards a healthier weight range."
  print(f"Your BMI is {BMI:.2f}")
  print(f"You are in the {Category} range. {Direction}, Thank You")

