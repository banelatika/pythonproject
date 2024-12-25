def calculate_duration(self, unit):
    if unit.lower() == 'months' or unit.lower() == 'm':
        return self.age * 12  
    elif unit.lower() == 'weeks' or unit.lower() == 'w':
        return round(self.age * 52.1429, 2)  
    elif unit.lower() == 'days' or unit.lower() == 'd':
        return round(self.age * 365.25, 2)  
    elif unit.lower() == 'hours' or unit.lower() == 'h':
        return round(self.age * 365.25 * 24, 2)  
    elif unit.lower() == 'minutes' or unit.lower() == 'min':
        return round(self.age * 365.25 * 24 * 60, 2) 
    elif unit.lower() == 'seconds' or unit.lower() == 's':
        return round(self.age * 365.25 * 24 * 60 * 60, 2)  
    else:
        return None  
        age = get_valid_age()
unit = get_valid_unit()


calculator = SurvivalDurationCalculator(age)
duration = calculator.calculate_duration(unit)

if duration is not None:
    if unit == 'm':
        unit = 'months'
    elif unit == 'w':
        unit = 'weeks'
    elif unit == 'd':
        unit = 'days'
    elif unit == 'h':
        unit = 'hours'
    elif unit == 'min':
        unit = 'minutes'
    elif unit == 's':
        unit = 'seconds'
    print(f"You have lived for {duration} {unit.capitalize()}.")
else:
    print("An error occurred while calculating the duration.")