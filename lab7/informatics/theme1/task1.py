def hypotenuse(a, b):
  from math import sqrt
  return sqrt(a**2 + b**2)


a = float(input())
b = float(input())

hypotenuse = hypotenuse(a, b)
print(hypotenuse)
