def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

n = 10
fib_gen = fibonacci_generator()
fib_series = [next(fib_gen) for _ in range(n)]
print(f"First {n} Fibonacci numbers (Generator):", fib_series)


