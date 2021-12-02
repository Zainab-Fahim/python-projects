def printToppings(toppingsList):
    if len(toppingsList) == 0:
        print("No toppings added")
    else:
        print("The toppings on your pizza are:")
        for i in range(len(toppingsList)):
            print(f'\t{toppingsList[i]}')


def order():
    global q, toppingAvail, toppingsList, operations, intro
    while q == False:
        print(intro)
        while toppingAvail:
            opp = input(operations).lower()
            if opp == 'a':
                topping = input("Type in a topping to add: ")
                toppingsList.append(topping)
                printToppings(toppingsList)
            elif opp == 'r':
                topRemove = input("What topping would you like to remove: ")
                toppingsList.remove(topRemove)
                printToppings(toppingsList)
            elif opp == 'o':
                printToppings(toppingsList)
                print("Thanks for your order!")
                q = True
                return True
            elif opp == 'q':
                q == True
                return True
            elif opp == 's':
                toppingsList.clear()
                order()
            else:
                print("I'm not sure what you said, please try again.")
    else:
        print("No toppings available")


toppingAvail = True
q = False
toppingsList = []

intro = "Welcome to Cavendish Pizzeria - choose your toppings.\n\nWhen prompted, enter first letter or full word of operation.\n ---- Operations ----\na   Add a topping\nr   Remove a topping\no   Order the pizza\nq   Quit\ns   Start over"
operations = "What would you like to do?\nadd, remove, order, quit, startover: "

while True:
    if order():
        break
""" 
OUTPUT:
Welcome to Cavendish Pizzeria - choose your toppings.

When prompted, enter first letter or full word of
operation.
 ---- Operations ----
a   Add a topping
r   Remove a topping
o   Order the pizza
q   Quit
s   Start over
What would you like to do?
add, remove, order, quit, startover: a
Type in a topping to add: mushrooms
The toppings on your pizza are:
        mushrooms
What would you like to do?
add, remove, order, quit, startover: a
Type in a topping to add: pineapples
The toppings on your pizza are:
        mushrooms
        pineapples
What would you like to do?
add, remove, order, quit, startover: uvwxyz
I'm not sure what you said, please try again.
What would you like to do?
add, remove, order, quit, startover: a
Type in a topping to add: bacon
The toppings on your pizza are:
        mushrooms
        pineapples
        bacon
What would you like to do?
add, remove, order, quit, startover: r
What topping would you like to remove: pineapples
The toppings on your pizza are:
        mushrooms
        bacon
What would you like to do?
add, remove, order, quit, startover: o
The toppings on your pizza are:
        mushrooms
        bacon
Thanks for your order!

 """
