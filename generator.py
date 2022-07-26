# !! This is a sample !!
# Must be configured as required

import sys
from random import randint

NEWLINE = '\n'

MAX_T = 100
MIN_N = 2
MAX_N = 1000
MAX_A = int(1e9)

id = 0

def write_tests(t, min_n, max_n, min_a, max_a):
    global id

    file = open(f"tests/inputs/in{id:02}.txt", "w")
    
    file.write(str(t))
    file.write(NEWLINE)
    
    for _ in range(t):
        n = randint(min_n, max(max_n // t, min_n))
        file.write(str(n))
        file.write(NEWLINE)
        a = ""
        for __ in range(n):
            a += str(randint(min_a, max_a)) + " "
        a = a.strip(' ')
        file.write(a)
        file.write(NEWLINE)
    
    file.close()
    id += 1

write_tests(5, 2, 30, 1, 10)
write_tests(5, 6, 50, 1, 20)
write_tests(10, 2, MAX_N, 1, 10)

for t in range(10, MAX_T - 1, 10):
    alpha = t / MAX_T
    write_tests(t, MIN_N, int(MAX_N * alpha), 1, int(MAX_A * alpha))

write_tests(MAX_T, MIN_N, MIN_N, 1, MAX_A)
write_tests(1, MAX_N, MAX_N, 1, MAX_A)
write_tests(MAX_T, MIN_N, MAX_N, 1, MAX_A)
