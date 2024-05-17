extract the corrosponding configuration any equivalent resistance value from a given list of available resistors.
outputs into a sorted json file with keys being resistance values and configs as an array of values.
eg:
    "1000": [
        "1.0k",
        "500--500",
        "500--(1.0k||1.0k)",
        "1.5k||(1.5k--1.5k)"
    ]
the symbol "--" means in series with ...
the symbol "||" means in parallel with ...
Note: configs are usually sorted from most efficient to least efficient

GET STARTED by opening main.py and change the resistors in "resistor_inventory" array to the resistor values available to you!
TO NAME THE FILE pass a name as an argument vector (e.g. python3 ./main.py test) this will name it "test.json"
if no argument for the name is passed in, the name will be output.json
you can just as easily run it for capacitors if you want, just swap the "--" with a "||" and vice versa when you read the json file.

Goal: an efficient C implementation that can calculate for all the E24 standard resistor values on my 8gb RAM laptop without starting a fire.
