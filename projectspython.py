class SurvivalDurationCalculator:
    def __init__(self, age):
        self.age = age

    def calculate_duration(self, unit):
        # Map of unit conversions
        unit_conversions = {
            'months': self.age * 12,
            'm': self.age * 12,
            'weeks': round(self.age * 52.1429, 2),
            'w': round(self.age * 52.1429, 2),
            'days': round(self.age * 365.25, 2),
            'd': round(self.age * 365.25, 2),
            'hours': round(self.age * 365.25 * 24, 2),
            'h': round(self.age * 365.25 * 24, 2),
            'minutes': round(self.age * 365.25 * 24 * 60, 2),
            'min': round(self.age * 365.25 * 24 * 60, 2),
            'seconds': round(self.age * 365.25 * 24 * 60 * 60, 2),
            's': round(self.age * 365.25 * 24 * 60 * 60, 2)
        }
        return unit_conversions.get(unit.lower(), None)  # Return None for invalid units

# Function to get a valid age
def get_valid_age():
    while True:
        try:
            age = float(input("Enter your age in years: "))
            if age < 0:
                raise ValueError("Age cannot be negative.")
            return age
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid age.")

# Function to get a valid unit
def get_valid_unit():
    valid_units = ['months', 'm', 'weeks', 'w', 'days', 'd', 'hours', 'h', 'minutes', 'min', 'seconds', 's']
    while True:
        unit = input("Enter the unit (months/m, weeks/w, days/d, hours/h, minutes/min, seconds/s): ").lower()
        if unit in valid_units:
            return unit
        print("Invalid unit. Please try again.")

# Main program
if __name__ == "__main__":
    age = get_valid_age()
    unit = get_valid_unit()

    calculator = SurvivalDurationCalculator(age)
    duration = calculator.calculate_duration(unit)

    if duration is not None:
        # Normalize unit to full form
        full_unit_mapping = {
            'm': 'months', 'w': 'weeks', 'd': 'days', 'h': 'hours', 'min': 'minutes', 's': 'seconds'
        }
        unit_full = full_unit_mapping.get(unit, unit)  # Get full form if short form is provided
        print(f"You have lived for {duration} {unit_full}.")
    else:
        print("An error occurred while calculating the duration.")
