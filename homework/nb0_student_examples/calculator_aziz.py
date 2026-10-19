def energy_consumption(power, hours, days):
    return (power * hours * days) / 1000

power = float(input("Enter the power"))
hours = float(input("Enter amount of hours"))
days = float(input("Enter number of days"))

energy = energy_consumption(power, hours, days)
print(energy)

if energy <= 10:
    print("Low")
elif energy <= 30:
    print("Medium")
else:
    print("High")