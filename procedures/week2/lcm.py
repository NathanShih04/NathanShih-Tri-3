def lcm(a,b):
  if (a > b):
      maximum = a
  else:
      maximum = b
  while (True):
      if (maximum % a == 0 and maximum % b == 0):
          break
      maximum = maximum + 1
  return maximum

def perform():
  print("The LCM of 38, 12 is", lcm(38,12))
  print("The LCM of 94, 11 is",lcm(94, 11))