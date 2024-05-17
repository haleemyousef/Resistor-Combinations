import sys
import json

resistor_inventory = [100, 200, 500, 1000, 1500, 2200, 4700, 6800, 8200,
                       10000, 15000, 20000, 25000, 33000, 47000, 68000, 75000,
                         100000, 150000, 200000, 270000, 470000, 820000,
                           1000000, 2000000]
combination_symbols = []
calculated_combinations = []
calculated_combinations = resistor_inventory
data = {}

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
    combination_symbols.append(f"({combination_symbols[y]}{'--' if is_parallel is False else '||'}{combination_symbols[x]})")      

def compute_and_push(x_limiter, y_limiter, x, y_value=None):
    set_y_to_x_flag = True if y_value is None else False
    while x < x_limiter:
        y = x if set_y_to_x_flag is True else y_value 
        while y < y_limiter:
            series = calculated_combinations[x] + calculated_combinations[y]
            calculated_combinations.append(round(series, 2))
            generate_hash(x, y)
            parallel = (calculated_combinations[x] * calculated_combinations[y]) / series
            calculated_combinations.append(round(parallel, 2))
            generate_hash(x, y, True)
            y += 1
        x += 1

def adjoin_lists_into_dict():
    for key, value in zip(calculated_combinations, combination_symbols):
        if key in data:
            # If the key already exists, append the value to its array
            data[key].append(value[1:-1])
        else:
            # If the key doesn't exist, create a new array with the value
            data[key] = [value[1:-1]]

if __name__ == "__main__":
    file_name = sys.argv[1] if len(sys.argv) == 2 else "output"
    print(file_name)
    combination_symbols = list(map(generate_initial_hash, calculated_combinations))
    compute_and_push(k1, k1, 0) # k=2 i.e. maximum of 2 resistors per combination
    compute_and_push(k1+k2, k1, k1, 0) # k=3
    adjoin_lists_into_dict()
    sorted_data = {k: data[k] for k in sorted(data)}
    with open(f"{file_name}.json", "w") as json_file:
        json.dump(sorted_data, json_file, indent=4)


    # for i, comb in enumerate(calculated_combinations):
    #     print(combination_symbols[i], comb)
    print(len(data), len(sorted_data), len(calculated_combinations),len(combination_symbols), k1+k2+k3, k1)