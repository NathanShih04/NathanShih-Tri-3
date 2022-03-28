class factorial:
  def __call__(self, num):
    ans = 1
    for i in range(1, num + 1):
      ans = ans * i
    return ans

factorial = factorial()
number = input("Number to find factorial of: ")
number = int(number)
print("Factorial of ", number, "is",   factorial(number))