def factorial(n):
        if n == 0:
                return 1
        else:
                return n * factorial(n-1)

def sum_series(n):
        sum = 0
        for i in range(1, n + 1):
                sum += (i ** i) / factorial(i)
        return sum

n = int(input("Enter a Number: "))
print("Sum of the series:", sum_series(n))


