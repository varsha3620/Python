square = lambda side: side * side
rectangle = lambda length, width: length * width
triangle = lambda base, height: 0.5 * base * height

print("Square Area")
side = int(input("Enter the side of square : "))
print(square(side))
print("Rectangle Area")
length = int(input("Enter the length of rectangle : "))
width = int(input("Enter the width of rectangle : "))
print(rectangle(length, width))
print("Triangle Area")
base = int(input("Enter the base of triangle : "))
height = int(input("Enter the height of triangle : "))
print(triangle(base, height))
