status = ""

def energy_calculation():
    # Ask the user to input the appliance's power, hours of use per day and number of days 
    power = float(input("Enter appliance's power (W): "))
    hours = float(input("Enter hours of use per day: "))
    days = float(input("Enter number of days: "))

    # calculates the total energy consumption using the formula
    energy = power * hours * days / 1000
  
    if energy < 10:
        status = "Low"
    elif energy > 10 and energy < 30:
        status = "Medium"
    elif energy > 30:
        status = "High"
    print(str(energy) + f" kWh, {status}")
 
# Call the function to get the result in kWh
energy_calculation()
