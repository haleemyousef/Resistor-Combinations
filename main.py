resistor_inventory = [1000, 2000]
calculated_combinations = []

n = len(resistor_inventory)
k1 = n
k2 = n^2 + n
k3 = 2*n^3 + 2*n^2
# k4_1 = 4*n^4 + 4*n^3
# k4_2 = n^4 + 2*n^3 + 2*n^2 + n

calculated_combinations += resistor_inventory
x = 0 # array index

while x < n:
    y = x
    while y < n:
        series = resistor_inventory[x] + resistor_inventory[y]
        calculated_combinations.append(series)
        parallel = (resistor_inventory[x] * resistor_inventory[y]) / series
        calculated_combinations.append(parallel)
        y += 1
    x += 1



print(calculated_combinations)