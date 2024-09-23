import math
r = int(input("What is the radius of your circle?"))
c = 2*r*math.pi
a = math.pi*r**2
print("c=",c," a=" ,a)


import math
r = int(input("What is the radius of your circle?"))
h = int(input("What is the height of your circle?"))
v = math.pi*r**2*h
print("v=" ,v)

#round to the hundereths
import math
r = int(input("What is the radius of your circle?"))
h = int(input("What is the height of your circle?"))
v = round(math.pi*r**2*h,2)
print("v=" ,v)
