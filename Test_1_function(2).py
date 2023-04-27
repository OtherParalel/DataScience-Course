import time

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

start = time.perf_counter()

for i in range(1, 11):
    print(factorial(i))

finish = time.perf_counter()

print(f"Finished in {finish - start:.4f} seconds")
