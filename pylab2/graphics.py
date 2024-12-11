from graphics.rectangle import *
from graphics.circle import *
from graphics.threeDGraphics.cuboid import *
from graphics.threeDGraphics.sphere import *

print("Rectangle")
l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
print("Area of rectangle:",RectArea(l,b))
print("Area of rectangle:",RectPerimeter(l,b))

print("Circle")
r=int(input("Enter the radius :"))
print("Circle Area:",circleArea(r))
print("Circle Perimeter:",circlePerimeter(r))


print("Cuboid")
l=int(input("Enter the length:"))
w=int(input("Enter the width :"))
h=int(input("Enter the height:"))
CuboidArea(l,w,h)
CuboidPerimeter(l,w,h)


print("Sphere")
r=int(input("Enter the radius : "))
print("Sphere Area:",SphereArea(r))
print("Sphere Perimeter:",SphereVolume(r))




