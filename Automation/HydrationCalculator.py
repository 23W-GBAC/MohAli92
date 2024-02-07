def calculate_water_intake(age, height, weight, sex):
    # Constants for calculation (values are indicative and can be adjusted)
    water_per_kg = 0.033  # liters of water per kg of body weight
    age_factor = 0.0002    # additional water intake per year of age
    height_factor = 0.0003 # additional water intake per cm of height
    male_factor = 0.3   # additional water intake for males compared to females
    female_factor = 0.15   # additional water intake for males compared to females


    # Calculate base water intake based on weight
    base_water_intake = weight * water_per_kg
    
    # Adjust water intake based on age, height, and sex
    adjusted_water_intake = base_water_intake + (age * age_factor) + (height * height_factor)
    if sex.lower() == "male":
        adjusted_water_intake += male_factor

    if sex.lower() == "female":
        adjusted_water_intake += female_factor

    return adjusted_water_intake

def main():
    # Input gathering
    age = int(input("Enter your age in years: "))
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))
    sex = input("Enter your sex (male/female): ")

    # Calculate recommended water intake
    recommended_water_intake = calculate_water_intake(age, height, weight, sex)

    # Display output
    print(f"Based on your age, height, weight, and sex, you should drink approximately {recommended_water_intake:.2f} liters of water per day.")

if __name__ == "__main__":
    main()
