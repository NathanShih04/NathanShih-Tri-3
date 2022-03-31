# import needed procedures, with ["name", "name.py"]
from procedures import submenus
from procedures.week0 import ship
from procedures.week1 import datalists
from procedures.week2 import lcm
from procedures.week3.gcd import *

main_menu = [
]

sub_menu = [
    ["Tree", "procedures/week0/tree.py"],
    ["Ship", ship.ship]
]

math_sub_menu = [
    ["Factorial", "procedures/week2/factorial.py"],
    ["Least Common Mulitple", lcm.perform],
    ["Palindrome", "procedures/week2/palindrome.py"],
    ["Keypad", "procedures/week0/keypad.py"],
    ["Swap", "procedures/week0/swap.py"],
    ["Fibonacci", "procedures/week1/fibonacci.py"],
  ["Greatest Common Divisor", "procedures/week3/gcd.py"]
]

data_sub_menu = [
    ["Datalist", datalists.main]
]

misc_sub_menu = [
  ["Color Text", "procedures/week3/colors.py"],
  ["Rock, Paper, Scissors", "procedures/week3/rockpaperscissors.py"]
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPick An Option\n{border}"


# menu blueprint
def menu():
    title = "Nathan's Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Patterns", submenu])
    menu_list.append(["Math", math_submenu])
    menu_list.append(["Data", data_submenu])
    menu_list.append(["Miscellaneous", misc_submenu])
    buildMenu(title, menu_list)


def submenuc():
    title = "submenu" + banner
    m = submenus.Menu(title, sub_menu)
    m.menu()


def submenu():
    title = "submenu" + banner
    buildMenu(title, sub_menu)

def math_submenuc():
    title = "submenu" + banner
    m = submenus.Menu(title, math_sub_menu)
    m.menu()

def data_submenuc():
    title = "submenu" + banner
    m = submenus.Menu(title, data_sub_menu)
    m.menu()
  
def misc_submenuc():
    title = "submenu" + banner
    m = submenus.Menu(title, misc_sub_menu)
    m.menu()
  
def math_submenu():
    title = "submenu" + banner
    buildMenu(title, math_sub_menu)

def data_submenu():
  title = "submenu" + banner
  buildMenu(title, data_sub_menu)

def misc_submenu():
  title = "submenu" + banner
  buildMenu(title, misc_sub_menu)
# builds console menu
def buildMenu(banner, options):
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user input
    choice = input("input your choice> ")

    # Process user input
    try:
        choice = int(choice)
        if choice == 0:
            # stops
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:
                exec(open(action).read())
            except FileNotFoundError:
                # check main_menu dictionary
                print(f"file not found!: {action}")
    except ValueError:
        # not a number
        print(f"not a number: {choice}")
    except UnboundLocalError:
        # not one of the numbers listed
        print(f"invalid choice: {choice}")

    buildMenu(banner, options)


if __name__ == "__main__":
    menu()
