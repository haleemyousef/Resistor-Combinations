resistor_inventory = [1000, 2000]
combination_symbols = []
calculated_combinations = []
calculated_combinations = resistor_inventory

n = len(resistor_inventory)
k1 = n
k2 = n**2 + n
k3 = 2 * n**3 + 2 * n**2
# k4_1 = 4*n^4 + 4*n^3
# k4_2 = n^4 + 2*n^3 + 2*n^2 + n

def generate_initial_hash(resistor, symbol=None):
    if resistor < 1000:
        symbol = str(resistor)
    elif resistor < 1000000:
        symbol = str(resistor/1000)+"k"
    else:
        symbol = str(resistor/1000000)+"M"
    return symbol

def generate_hash(x, y, is_parallel=None):
    is_parallel = False if is_parallel is None else True
    combination_symbols.append(f"({combination_symbols[y]}{"--" if is_parallel is False else "||"}{combination_symbols[x]})")
        

def compute_and_push(x_limiter, y_limiter, x, y_value=None):
    set_y_to_x_flag = True if y_value is None else False
    while x < x_limiter:
        y = x if set_y_to_x_flag is True else y_value 
        while y < y_limiter:
            series = calculated_combinations[x] + calculated_combinations[y]
            calculated_combinations.append(series)
            generate_hash(x, y)
            parallel = (calculated_combinations[x] * calculated_combinations[y]) / series
            calculated_combinations.append(parallel)
            generate_hash(x, y, True)
            y += 1
        x += 1


if __name__ == "__main__":
    combination_symbols = list(map(generate_initial_hash, calculated_combinations))
    compute_and_push(k1, k1, 0)
    compute_and_push(k1+k2, k1, k1, 0)

    for i, comb in enumerate(calculated_combinations):
        print(combination_symbols[i], comb)
    print(len(calculated_combinations),len(combination_symbols), k1+k2+k3)