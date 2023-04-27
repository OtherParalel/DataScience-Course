import concurrent.futures
import time

import math

def factorial(n):
    return math.factorial(n)


start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(factorial, i) for i in range(1, 11)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f"Finished in {finish - start:.4f} seconds")
