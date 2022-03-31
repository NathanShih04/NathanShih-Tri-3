def gcd(num1, num2):
    if num1 > num2:
        s = num2
    else:
        s = num1
    for i in range(1, s + 1):
        if num1 % i == 0 and num2 % i == 0:
            value = i
    return value

class GCD:
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	def __call__(self):
		if self.num1 > self.num2:
			s = self.num2

		else:
			s = self.a

		for i in range(1, s+1):
			if self.num1 % i == 0 and self.num2 % i == 0:
				value = i
		return value

def run():
	num = input("imperative(i) or OOP(o)")
	try:
		if num == 'i':
			print("the LCM of 12 and 30 is ", gcd(12,30))
		elif num == 'o':
			gcdoop = GCD(12,30)
			print("the LCM of 12 and 30 is ", gcdoop())
	except:
		print("that was not an option u old swine")


if __name__ == "__main__":
    run()