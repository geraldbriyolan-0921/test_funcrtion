def print_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Example: Print the first 10 Fibonacci numbers
print_fibonacci(1000)
