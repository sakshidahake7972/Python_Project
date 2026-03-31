POWER_LIMIT = 1000

def calculate(voltage, resistance):
    if resistance == 0:
        return None, None
    current = voltage / resistance
    power = voltage * current
    return current, power


def main():
    print("SMART HOME ENERGY CONSUMPTION MONITOR\n")

    n = int(input("Enter number of appliances: "))

    appliances = {}

    # Taking input from user
    for i in range(n):
        print(f"\nEnter details for Appliance {i+1}")
        name = input("Appliance Name: ")
        voltage = float(input("Voltage (V): "))
        resistance = float(input("Resistance (Ohms): "))
        appliances[name] = (voltage, resistance)

    # Create report file
    with open("Daily_Consumption_Report.txt", "w") as file:

        file.write("SMART HOME ENERGY CONSUMPTION REPORT\n\n")

        # Process each appliance
        for name, (voltage, resistance) in appliances.items():

            current, power = calculate(voltage, resistance)

            if current is None:
                print(f"{name}: Invalid resistance value!\n")
                continue

            # Display output
            print(f"\nAppliance: {name}")
            print(f"Current: {current:.2f} A")
            print(f"Power: {power:.2f} W")

            # Write to file
            file.write(f"Appliance: {name}\n")
            file.write(f"Voltage: {voltage} V\n")
            file.write(f"Resistance: {resistance} Ohms\n")
            file.write(f"Current: {current:.2f} A\n")
            file.write(f"Power: {power:.2f} W\n")

            # Control flow (checking power)
            if power > POWER_LIMIT:
                msg = "High Power Consumption! Reduce usage."
            else:
                msg = "Power consumption is normal."

            print(msg)
            file.write(msg + "\n\n")

        # Suggestions
        file.write("ENERGY SAVING SUGGESTIONS\n")
        file.write("1. Turn off appliances when not in use.\n")
        file.write("2. Use energy-efficient appliances.\n")
        file.write("3. Avoid using multiple high-power devices together.\n")
        file.write("4. Regular maintenance improves efficiency.\n")

    print("\nReport file created successfully!")
#Run Program
main()