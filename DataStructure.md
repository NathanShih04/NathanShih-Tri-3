{% include navbar.html %}

<iframe frameborder="0" width="100%" height="800px" src="https://replit.com/@TankeeTort/NathanShih-Tri-3?embed=true">

## Week 0
### Learning how menus work and are built in terminal.
```
def menu():
    title = "menu" + banner 
    menu_list = main_menu.copy()
    menu_list.append(["patterns", submenu])
    buildMenu(title, menu_list)


```
## Week 1
### Learned how to create datalists and print them 3 different ways.

```
InfoDb = []

InfoDb.append({  
               "Name": "Nathan Shih",  
               "Birth": "November 12",
               "Siblings": "Yes",
               "Hobbies":["Coding", "Fishing", "Driving", "Gaming"]  
              })  

InfoDb.append({  
               "Name": "Noah Jeng",  
               "Birth": "February 14",
               "Siblings": "Yes",
               "Hobbies":["Soccer", "Driving", "Gaming", "Sleeping"] 
              })

InfoDb.append({  
               "Name": "Isaac Le",  
               "Birth": "December 3",
               "Siblings": "No",
               "Hobbies":["School", "Gaming", "Listening to Music", "Math"] 
              })
```
```
# For Loop
def for_loop():
  for n in range(len(InfoDbLoop)):
    print_data(n)

# While Loop
# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
  while n < len(InfoDbLoop):
    print_data(n)
    n += 1
  return

# Recursion
# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
  if n < len(InfoDbLoop):
    print_data(n)
    recursive_loop(n + 1)
  return # exit condition
```

## Week 2
### Created factorial, least common multiple, and palindrome functions.

Factorial:
```
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
```
Least Common Multiple:
```
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
```
Palindrome:
```
class Palindrome():
    def __init__(self):
        self.strArr = ["radar", "racecar", "palindrome"]

    def __call__(self):
        for str in self.strArr:
            original = str
            str = str.strip()
            str = ''.join(char for char in str if char.isalnum())
            str = str.lower()

            if str == str[::-1]:
                print(original + " is a palindrome")
            else:
                print(original + " is not a palindrome")


P = Palindrome()
P()
```
