
appliances = {
    "Refrigerator": (230, 115),
    "Washing Machine": (230, 50),
    "Air Conditioner": (230, 30),
    "Television": (230, 460),
    "Fan": (230, 800)
}

POWER_LIMIT = 1000

print("SMART HOME ENERGY CONSUMPTION REPORT")
print("=====================================\n")


with open("Daily_Consumption_Report.txt", "w") as report:

    report.write("SMART HOME ENERGY CONSUMPTION REPORT\n")
    report.write("=====================================\n\n")

    for appliance in appliances:

        V = appliances[appliance][0]
        R = appliances[appliance][1]


        if R == 0:
            print(f"{appliance}: Invalid resistance value!")
            continue

        #current formula
        current = V / R

        # Power Formula
        power = V * current


        print("Appliance:", appliance)
        print("Current: {:.2f} A".format(current))
        print("Power: {:.2f} W".format(power))


        report.write("Appliance: " + appliance + "\n")
        report.write("Voltage: " + str(V) + " V\n")
        report.write("Resistance: " + str(R) + " Ohms\n")
        report.write("Current: {:.2f} A\n".format(current))
        report.write("Power: {:.2f} W\n".format(power))


        if power > POWER_LIMIT:
            print("High Power Consumption! Reduce usage.\n")
            report.write("High Power Consumption! Reduce usage.\n\n")
        else:
            print("Power consumption is normal.\n")
            report.write("Power consumption is normal.\n\n")


    report.write("ENERGY SAVING SUGGESTIONS\n")
    report.write("--------------------------\n")
    report.write("1. Turn off appliances when not in use.\n")
    report.write("2. Use energy-efficient appliances.\n")
    report.write("3. Avoid using multiple high-power devices together.\n")
    report.write("4. Regular maintenance improves efficiency.\n")

print("Report file created successfully!")