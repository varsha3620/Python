def powers_of_two(n):
    numbers = range(n)
    powers = map(lambda x: 2 ** x, numbers)
    return list(powers)

n = int(input("Enter a number to display powers of 2 up to that power: "))

result = powers_of_two(n)
print(f"Powers of 2 from 0 to {n-1}: {result}")




