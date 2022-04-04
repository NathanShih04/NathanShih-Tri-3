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

class LCM:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2

  def __call__(self):
    if self.num1 > self.num2:
      max = self.num1
      
    else:
      max = self.num2
    while (True):
      if (max % self.num1 == 0 and max % self.num2 == 0):
        break
      max = max + 1
    return max

def perform():
  print("The LCM of 38, 12 is", lcm(38,12))
  print("The LCM of 94, 11 is",lcm(94, 11))