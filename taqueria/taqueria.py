def main():

    take_order()

def take_order():
    menu = {
        "baja taco"         : 4.00,
        "burrito"           : 7.50,
        "bowl"              : 8.50,
        "nachos"            : 11.00,
        "quesadilla"        : 8.50,
        "super burrito"     : 8.50,
        "super quesadilla"  : 9.50,
        "taco"              : 3.00,
        "tortilla salad"    : 8.00
    }

    total = 0.00

    while True:
        try:
            price = menu[input("Item: ").lower()]
            total = total + price
            print(f"Total: ${total:.2f}")
        except KeyError:
            pass
        except EOFError:
            print()
            break

main()