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

def compute_and_push(x_limiter, y_limiter, x, y_value=None):
    set_y_to_x_flag = True if y_value is None else False
    while x < x_limiter:
        y = x if set_y_to_x_flag is True else y_value 
        while y < y_limiter:
            series = calculated_combinations[x] + calculated_combinations[y]
            calculated_combinations.append(series)
            parallel = (calculated_combinations[x] * calculated_combinations[y]) / series
            calculated_combinations.append(parallel)
            y += 1
        x += 1

compute_and_push(k1, k1, 0)
compute_and_push(k1+k2, k1, k1, 0)

print(calculated_combinations)