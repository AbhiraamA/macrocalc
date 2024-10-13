def calculate_bmr(weight, height, age, gender):
    # Convert weight from pounds to kilograms
    weight_kg = weight * 0.453592
    # Mifflin-St Jeor Equation for BMR
    if gender == "male":
        bmr = 10 * weight_kg + 6.25 * height - 5 * age + 5
        print(bmr)
    else:
        bmr = 10 * weight_kg + 6.25 * height - 5 * age - 161
    return bmr

def calculate_calories(bmr, activity_level):
    # Activity multiplier based on activity level
    activity_factors = {
        "sedentary": 1.19,       # little or no exercise
        "light": 1.37,         # light exercise/sports 1-3 days/week
        "moderate": 1.55,       # moderate exercise/sports 3-5 days/week
        "active": 1.73,        # hard exercise/sports 6-7 days a week
        "very active": 1.82      # very hard exercise/physical job & exercise twice a day
    }
    return bmr * activity_factors[activity_level]

def calculate_lean_body_mass(weight, body_fat_percentage):
    # Cap the body fat percentage at 33% for calculation
    if body_fat_percentage > 33:
        body_fat_percentage = 33
    lean_body_mass = weight * (1 - body_fat_percentage / 100)
    return lean_body_mass

def calculate_macros(lean_body_mass, calorie_goal):
    # Protein is 1.1 to 1.6 grams per pound of lean body mass depending on leanness
    protein_low = 1.1 * lean_body_mass
    protein_high = 1.6 * lean_body_mass
    protein = (protein_low + protein_high) / 2  # Midpoint of the protein range

    # 1g of protein = 4 calories, 1g of carbs = 4 calories, 1g of fats = 9 calories
    protein_calories = protein * 4
    fat_percentage = 0.25  # Assuming 25% of calories come from fats
    fat_calories = calorie_goal * fat_percentage
    fat = fat_calories / 9

    # Remaining calories go to carbs
    carb_calories = calorie_goal - (protein_calories + fat_calories)
    carbs = carb_calories / 4

    return protein, carbs, fat

def calculate_goal_calories(maintenance_calories, goal_type):
    if goal_type == "gain":
        return maintenance_calories + 500  # ~1lb/week gain
    elif goal_type == "lose":
        return maintenance_calories - 500  # ~1lb/week loss
    else:
        return maintenance_calories  # Maintenance

def main():
    # Gather user input
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in cm: "))
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ").lower()
    activity_level = input("Enter your activity level (sedentary, light, moderate, active, very active): ").lower()
    body_fat_percentage = float(input("Enter your approximate body fat percentage (max 33%): "))
    goal_type = input("What is your goal? (gain, lose, maintain): ").lower()

    # Calculate BMR and maintenance calories
    bmr = calculate_bmr(weight, height, age, gender)
    maintenance_calories = calculate_calories(bmr, activity_level)

    # Adjust for goal (weight gain, loss, or maintenance)
    calorie_goal = calculate_goal_calories(maintenance_calories, goal_type)

    # Calculate lean body mass
    lean_body_mass = calculate_lean_body_mass(weight, body_fat_percentage)

    # Calculate macros
    protein, carbs, fats = calculate_macros(lean_body_mass, calorie_goal)

    # Output the results
    print(f"\nYour daily maintenance calorie needs: {maintenance_calories:.0f} calories")
    print(f"Your daily calorie goal for {goal_type} weight: {calorie_goal:.0f} calories")
    print(f"Ideal daily macros for {goal_type} weight:")
    print(f"Protein: {protein:.0f} grams")
    print(f"Carbohydrates: {carbs:.0f} grams")
    print(f"Fats: {fats:.0f} grams")

if __name__ == "__main__":
    main()
