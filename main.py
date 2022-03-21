# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
# imports from other .py files
import ship
import datalists

# Main Menu
main_menu = [
    ["Fibonacci", "fibonacci.py"],
    ["Datalists", datalists.main]
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Swap", "swap.py"],
    ["Tree", "tree.py"],
    ["Ship", ship.ship],
    ["Keypad", "keypad.py"]

]

border = "=" * 25
banner = f"\n{border}\nChoose one of the options: \n{border}"


def menuc():
    title = "Class Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Submenu", submenuc])
    m = questy.Menu(title, menu_list)
    m.menu()  


def submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, sub_menu)
    m.menu()


def menu():
    title = "Nathan Shih's Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Submenu", submenu])
    buildMenu(title, menu_list)


def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)

def buildMenu(banner, options):

    print(banner)

    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op


    for key, value in prompts.items():
        print(key, '->', value[0])
    choice = input("Type your choice> ")

    try:
        choice = int(choice)
        if choice == 0:
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try: 
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")

    buildMenu(banner, options)  

if __name__ == "__main__":
    menu()







































# import time

# ans = True

# while ans:
#   print("""
#     Repl Main Menu:
#     1. Week 0
#     2. Week 1
#     3. Exit/Quit
#     """)
#   mm = input("Select which week challenge: ")


#   if mm == "1":
#       print("""
#       Repl Menu:
#       1. Ship Pattern
#       2. Build a Christmas Tree
#       3. Number Swap
#       4. Matrix Numberpad
#       5. Exit/Quit
#       """)
    
#       ans = input("What would you like to do? ")
  
#   # WEEK 1 TASKS --------------------------------------------------------------------
    
#       def ocean_print():
#         # print ocean
#         print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
#         print("\n\n\n\n")
#         print(OCEAN_COLOR + "  " * 35)
  
  
#       # print ship with colors and leading spaces
#       def ship_print(position):
#           print(ANSI_HOME_CURSOR)
#           print(RESET_COLOR)
#           sp = " " * position
#           print(sp + "    |\   ")
#           print(sp + "    |/   ")
#           print(SHIP_COLOR, end="")
#           print(sp + "\__ |__/ ")
#           print(sp + " \____/  ")
#           print(RESET_COLOR)
  
  
#       # ship function, iterface into this file
#       def ship():
#           # only need to print ocean once
#           ocean_print()
      
#           # loop control variables
#           start = 0  # start at zero
#           distance = 60  # how many times to repeat
#           step = 2  # count by 2
      
#           # loop purpose is to animate ship sailing
#           for position in range(start, distance, step):
#               ship_print(position)  # call to function with parameter
#               time.sleep(.1)
  
#           # Generating Pole Shape
#       def poleShape(n):
#         for i in range(n):
#             for j in range(n-1):
#                 print(' ', end=' ')
#             print('* * *')
  
#       def triangleShape(n):
#         for i in range(n):
#             for j in range(n-i):
#                 print(' ', end=' ')
#             for k in range(2*i+1):
#                 print('*',end=' ')
#             print()
  
          
#       # Boat animation
#       if ans == "1":
#         ANSI_CLEAR_SCREEN = u"\u001B[2J"
#         ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
#         OCEAN_COLOR = u"\u001B[44m\u001B[2D"
#         SHIP_COLOR = u"\u001B[32m\u001B[2D"
#         RESET_COLOR = u"\u001B[0m\u001B[2D"
  
#         ship()
  
  
#       # Christmas Tree 
#       elif ans == "2":
      
#       # Input and Function Call
#         row = int(input('Enter number of rows: '))
      
#         triangleShape(row)
#         triangleShape(row)
#         poleShape(row)
  
  
#       # Number Swapper
#       elif ans == "3":
  
#         num1 = float(input("Choose first number: "))
#         num2 = float(input("Choose second number: "))
        
#         holder = num1
#         num1 = num2
#         num2 = holder
#         print("After swap...")
#         print("number 1: " + str(num1))
#         print("number 2: " + str(num2))
  
        
#       # Matrix Numberpad
#       elif ans == "4":
#         R = int(3)
#         C = int(3)

#         # Initialize matrix
#         matrix = []
#         print("Enter the entries rowwise:")
        
#         # For user input
#         for i in range(R):          # A for loop for row entries
#             a =[]
#             for j in range(C):      # A for loop for column entries
#                  a.append(int(input()))
#             matrix.append(a)
        
#         # For printing the matrix
#         for i in range(R):
#             for j in range(C):
#                 print(matrix[i][j], end = " ")
#             print()
            
#       else:
#         ans = False
#         print("See you!")
  
#   # END OF WEEK 1 TASKS -------------------------------------------------------
  
#   # WEEK 2 TASKS --------------------------------------------------------------------
#   if mm == "2":
    
#     print("""
#       Repl Menu:
#       1. InfoDB Lists
#       2. InfoDB Loops
#       3. Fibonacci
#       4. Exit/Quit
#       """)
    
#     ans = input("What would you like to do? ")
    
#     # InfoDB lists
#     if ans == "1":

#       def print_data(n):
#         print(InfoDb[n]["Name"])  # print name
#         print("\t", "Birth: ", end="")
#         print(InfoDb[n]["Birth"])
#         print("\t", "Siblings: ", end="")  # \t is a tab indent, end="" make sure no return occurs
#         print(InfoDb[n]["Siblings"])
#         print("\t", "Hobbies: ", end="")
#         print(", ".join(InfoDb[n]["Hobbies"]))  # join allows printing a string list with separator
#         print()

#       # Creating Database
#       InfoDb = []

#       InfoDb.append({  
#                      "Name": "Nathan Shih",  
#                      "Birth": "November 12",
#                      "Siblings": "Yes",
#                      "Hobbies":["Coding", "Fishing", "Driving", "Gaming"]  
#                     })  
      
#       InfoDb.append({  
#                      "Name": "Noah Jeng",  
#                      "Birth": "February 14",
#                      "Siblings": "Yes",
#                      "Hobbies":["Soccer", "Driving", "Gaming", "Sleeping"] 
#                     })
      
#       InfoDb.append({  
#                      "Name": "Isaac Le",  
#                      "Birth": "December 3",
#                      "Siblings": "No",
#                      "Hobbies":["School", "Gaming", "Listening to Music", "Math"] 
#                     })

#       InfoDb.append({  
#                      "Name": "Tanay Rayavarapu",  
#                      "Birth": "October 14",
#                      "Siblings": "Yes",
#                      "Hobbies":["Basketball", "Anime", "YouTube", "Music"] 
#                     })

#       for i in range(len(InfoDb)):
#         print_data(i)


#     # InfoDB loops
#     if ans == "2":
#       InfoDbLoop = []

#       InfoDbLoop.append({  
#                      "Name": "Nathan Shih",  
#                      "Sport": "Tennis",
#                      "Age": "17",
#                      "Hobbies":["Coding", "Fishing", "Driving", "Gaming"]  
#                     })  
      
#       InfoDbLoop.append({  
#                      "Name": "Noah Jeng",  
#                      "Sport": "Soccer",
#                      "Age": "17",
#                      "Hobbies":["Soccer", "Driving", "Gaming", "Sleeping"] 
#                     })
      
#       InfoDbLoop.append({  
#                      "Name": "Isaac Le",  
#                      "Sport": "Soccer",
#                      "Age": "17",
#                      "Hobbies":["School", "Gaming", "Listening to Music", "Math"] 
#                     })

#       InfoDbLoop.append({  
#                      "Name": "Tanay Rayavarapu",  
#                      "Sport": "Swimming",
#                      "Age": "17",
#                      "Hobbies":["Basketball", "Anime", "YouTube", "Music"] 
#                     })

#       def print_data(n):
#         print(InfoDbLoop[n]["Name"])  # print name
#         print("\t", "Sport: ", end="")
#         print(InfoDbLoop[n]["Sport"])
#         print("\t", "Age: ", end="")  # \t is a tab indent, end="" make sure no return occurs
#         print(InfoDbLoop[n]["Age"])
#         print("\t", "Hobbies: ", end="")
#         print(", ".join(InfoDbLoop[n]["Hobbies"]))  # join allows printing a string list with separator
#         print()

#       # For Loop
#       def for_loop():
#         for n in range(len(InfoDbLoop)):
#           print_data(n)

#       # While Loop
#       # while loop contains an initial n and an index incrementing statement (n += 1)
#       def while_loop(n):
#         while n < len(InfoDbLoop):
#           print_data(n)
#           n += 1
#         return

#       # Recursion
#       # recursion simulates loop incrementing on each call (n + 1) until exit condition is met
#       def recursive_loop(n):
#         if n < len(InfoDbLoop):
#           print_data(n)
#           recursive_loop(n + 1)
#         return # exit condition

#       print("THIS IS THE FOR LOOP PRINTING")
#       for_loop()
#       print("THIS IS THE WHILE LOOP PRINTING")
#       while_loop(0)
#       print("THIS IS RECURSION PRINTING")
#       recursive_loop(0)


#     # Fibonacci
#     if ans == "3":
#       try:
#         num = int(input("enter a number for fibonacci:"))
#         assert num > 0 
#         n1, n2 = 0, 1
#         print("Fibonacci Series:", n1, n2, end=" ")
#         for int in range(2, num):
#           n3 = n1 + n2
#           n1 = n2
#           n2 = n3
#           print(n3, end=" ")
#         print()
#       except AssertionError :
#         print("please input a positive value")  

#     # Breakout
#     elif ans == "4":
#       ans = False
#       print("See you later!")
            
#   # END OF WEEK 2 TASKS -------------------------------------------------------

#   elif mm == "3":
#     ans = False
#     print("Bye!")
  
