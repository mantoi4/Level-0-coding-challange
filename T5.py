def triangle(a, b, c):

  a = int(a)
  b = int(b)
  c = int(c)

  area = (a + b + c) * 1/2

  return abs((area*(area - a) * (area - b) * (area - c))) ** 0.5

print(round(triangle(8, 4, 3),2))