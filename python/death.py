import datetime
import numpy as np

# Base life expectancy by country and gender
life_expectancy_data = {
    'India': {'male': 70.5, 'female': 73.6},
    'USA': {'male': 76, 'female': 81},
    'UK': {'male': 79, 'female': 83},
    'Japan': {'male': 81, 'female': 87},
}

# Risk factor impact in years (approximate average reductions)
risk_factors = {
    'hypertension': 2,
    'diabetes': 3,
    'cardiovascular_disease': 5,
    'cancer': 10,
    'respiratory_disease': 4,
    'mental_health': 2,
    'kidney_disease': 3,
    'liver_disease': 3,
    'smoking': 5,
    'alcohol': 3,
    'physical_inactivity': 2,
    'poor_diet': 2,
    'obesity': 3,
    'high_stress': 2,
    'air_pollution': 1
}

def get_user_data():
    print("🔹 Personal Information")
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("gender (male/female): ").lower()
    country = input("Country (India/USA/UK/Japan): ")
    family_history = input("Family history of major diseases? (yes/no): ").lower() == 'yes'
    
    weight = float(input("Weight (kg): "))
    height = float(input("Height (cm): "))
    bmi = weight / ((height/100) ** 2)
    overweight = bmi >= 25
    
    print("\n🔹 Health Conditions (yes/no)")
    health = {
        'hypertension': input("Hypertension? ").lower() == 'yes',
        'diabetes': input("Diabetes? ").lower() == 'yes',
        'cardiovascular_disease': input("Heart disease? ").lower() == 'yes',
        'cancer': input("Cancer? ").lower() == 'yes',
        'respiratory_disease': input("Respiratory disease? ").lower() == 'yes',
        'mental_health': input("Mental health issues? ").lower() == 'yes',
        'kidney_disease': input("Kidney disease? ").lower() == 'yes',
        'liver_disease': input("Liver disease? ").lower() == 'yes',
    }
    
    print("\n🔹 Lifestyle Factors")
    lifestyle = {
        'smoking': input("Do you smoke? ").lower() == 'yes',
        'alcohol': input("Do you drink alcohol regularly? ").lower() == 'yes',
        'physical_inactivity': input("Are you physically inactive? ").lower() == 'yes',
        'poor_diet': input("Do you have a poor diet? ").lower() == 'yes',
        'obesity': overweight,
        'high_stress': input("Do you experience chronic stress? ").lower() == 'yes',
    }
    
    print("\n🔹 Environmental Factors")
    environment = {
        'air_pollution': input("Do you live in a highly polluted area? ").lower() == 'yes',
    }
    
    return name, age, gender, country, family_history, health, lifestyle, environment

def calculate_life_expectancy(age, gender, country, family_history, health, lifestyle, environment):
    base_life = life_expectancy_data.get(country, {}).get(gender, 75)
    
    # Calculate total risk
    total_risk = sum(risk_factors[k] for k, v in {**health, **lifestyle, **environment}.items() if v)
    if family_history:
        total_risk += 3  # approximate additional risk
    
    adjusted_life = max(base_life - total_risk, age + 1)
    
    # Probabilistic modeling: add ± standard deviation based on total risk
    std_dev = max(total_risk * 0.2, 2)  # uncertainty ~20% of total risk, minimum 2 years
    simulated_lifespans = np.random.normal(adjusted_life, std_dev, 1000)
    simulated_lifespans = [max(l, age + 1) for l in simulated_lifespans]  # no death before current age
    
    median_life = np.median(simulated_lifespans)
    p10 = np.percentile(simulated_lifespans, 10)
    p90 = np.percentile(simulated_lifespans, 90)
    
    current_year = datetime.datetime.now().year
    median_death_year = int(current_year + (median_life - age))
    death_year_range = (int(current_year + (p10 - age)), int(current_year + (p90 - age)))
    
    return median_life, median_life - age, median_death_year, death_year_range

def main():
    print("🔬 Probabilistic Death Year Estimator 🔬")
    name, age, gender, country, family_history, health, lifestyle, environment = get_user_data()
    
    median_life, remaining_years, median_death_year, death_year_range = calculate_life_expectancy(
        age, gender, country, family_history, health, lifestyle, environment
    )
    
    print(f"\n📊 {name}'s Personalized Life Expectancy:")
    print(f"- Median life expectancy: {median_life:.1f} years")
    print(f"- Remaining years: {remaining_years:.1f}")
    print(f"- Median estimated death year: {median_death_year}")
    print(f"- Probabilistic death year range (10th–90th percentile): {death_year_range[0]} – {death_year_range[1]}")
    print("\n⚠️ Note: This is a statistical estimate for educational purposes, not a precise prediction.")

if __name__ == "__main__":
    main()
