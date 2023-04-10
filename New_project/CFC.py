# Carbon Footprint Calculator

# Define constants (in kg CO2 equivalents)
CAR_EMISSION_FACTOR = 0.2        # kg CO2e per mile driven
ELECTRICITY_EMISSION_FACTOR = 0.6 # kg CO2e per kWh of electricity used
GAS_EMISSION_FACTOR = 0.2        # kg CO2e per therm of natural gas used
WATER_CONSUMPTION_EMISSION_FACTOR = 0.005  # kg CO2e per gallon of water used

# Gather input from user
car_miles = float(input("Enter the number of miles driven per year: ")) # ask user for input on miles driven per year
electricity_kwh = float(input("Enter the number of kWh of electricity used per year: ")) # ask user for input on electricity used per year
gas_therms = float(input("Enter the number of therms of gas used per year: ")) # ask user for input on natural gas used per year
water_gallons = float(input("Enter the number of gallons of water used per year: ")) # ask user for input on water consumed per year

# Calculate carbon footprint
car_emissions = car_miles * CAR_EMISSION_FACTOR # calculate emissions from driving using the inputted value for miles and the constant for car emissions factor
electricity_emissions = electricity_kwh * ELECTRICITY_EMISSION_FACTOR # calculate emissions from electricity use using the inputted value for kWh and the constant for electricity emissions factor
gas_emissions = gas_therms * GAS_EMISSION_FACTOR # calculate emissions from natural gas use using the inputted value for therms and the constant for natural gas emissions factor
water_emissions = water_gallons * WATER_CONSUMPTION_EMISSION_FACTOR # calculate emissions from water consumption using the inputted value for gallons consumed and the constant for water consumption emissions factor

total_emissions = car_emissions + electricity_emissions + gas_emissions + water_emissions # sum up all the emissions

# Print results
print("\nCarbon Footprint Calculator Results")
print("-----------------------------------")
print(f"Transportation: {car_emissions:.2f} kg CO2e") # print emissions from driving in kg CO2e with 2 decimal points
print(f"Electricity: {electricity_emissions:.2f} kg CO2e") # print emissions from electricity use in kg CO2e with 2 decimal points
print(f"Natural Gas: {gas_emissions:.2f} kg CO2e") # print emissions from natural gas use in kg CO2e with 2 decimal points
print(f"Water Consumption: {water_emissions:.2f} kg CO2e") # print emissions from water consumption in kg CO2e with 2 decimal points
print("-----------------------------------")
print(f"Total: {total_emissions:.2f} kg CO2e") # print total emissions in kg CO2e with 2 decimal points