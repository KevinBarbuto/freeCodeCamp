# Prints out a list of randomly generated arithmetic statements.
# Inspired by this forum post: https://smwc.me/1388949

import random

for i in range(1,101): # Change "101" into however many items to generate, +1. In the case of the inspiring post, this would be 9001.
    a = random.randint(1,9999)

    operator = random.choice(["+","-","*","/"])
    b = eval(f"{9000} {operator} {a}")
    print(i, ") ", "9000 ", operator, " ", a, " = ", b, sep = '')


# Note to self: Although the eval function is incredibly useful here, let's try not to use it in programs that are meant to take a user input.
