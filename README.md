extract the corrosponding configuration any equivalent resistance value from a given list of available resistors.
outputs into a sorted json file with keys being resistance values and configs as an array of values.
eg:
    "1000": [
        "1.0k",
        "(500--500)",
        "(500--(1.0k||1.0k))",
        "(1.5k||(1.5k--1.5k))"
the symbol "--" means in series with ...
the symbol "||" means in parallel with ...

you can just as easily run it for capacitors if you want, just swap the "--" with a "||" and vice versa when you read the json file.

Goal: an efficient C implementation that can calculate for all the E24 standard resistor values on my 8gb RAM laptop without starting a fire.
