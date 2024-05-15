resistor_inventory = [1000, 2000]
calculated_combinations = []

x = len(resistor_inventory)
k1 = x
k2 = x^2 + x
k3 = 2*x^3 + 2*x^2
# k4_1 = 4*x^4 + 4*x^3
# k4_2 = x^4 + 2*x^3 + 2*x^2 + x

calculated_combinations += resistor_inventory
x -= 1 # decrease by 1 to be used as the array index

while x >= 0:
    y = x
    while y >= 0:
        series = resistor_inventory[x] + resistor_inventory[y]
        calculated_combinations.append(series)
        parallel = (resistor_inventory[x] * resistor_inventory[y]) / series
        calculated_combinations.append(parallel)
        y -= 1
    x -= 1

print(calculated_combinations)