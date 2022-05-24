def triangleArea(a, b, c):

  area = (a + b + c) * 1/2

  return abs((area*(area - a) * (area - b) * (area - c))) ** 0.5

print(round(triangleArea(8, 4, 3),2))


