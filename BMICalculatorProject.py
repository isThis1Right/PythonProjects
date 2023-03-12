
# Collect information from user
def user_input_func(prompt, field_type=str):
    user_input = input(prompt)

    if field_type == str:
        while user_input.isdigit():
            user_input = input("Invalid input. " + prompt)
            
        return user_input
    elif field_type == int:
        while not user_input.isdigit() or int(user_input) <= 0:
            user_input = input("Invalid input. " + prompt)
            
        return int(user_input)

# Calculate user's BMI
def bmi_calc(weight, height):
    bmi = (weight * 703)/(height * height)

    if bmi > 0:
        if bmi < 18.5:
            response = "You are considered to be underweight."
        elif bmi <= 24.9:
            response = "You are considered to be normal weight."
        elif bmi <= 29.9:
            response = "You are considered to be overweight."
        elif bmi <= 34.9:
            response = "You are considered to be obese."
        elif bmi <= 39.9:
            response = "You are considered to be severely obese."
        else:
            response = "You are considered to be morbidly obese."

    return bmi, response

# Logic for BMI calculator
print("Welcome to the BMI Calculator!\n")

name = user_input_func("Please enter your name: ")
weight = user_input_func("Enter your weight in pounds: ", int)
height = user_input_func("Enter your weight in inches: ", int)
result = bmi_calc(weight,height)

print("\n{name}, your BMI is {bmi}. {response}\n".format(name = name, bmi = result[0], response = result[1]))

input("Press Enter to exit...")

