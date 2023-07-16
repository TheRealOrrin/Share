def main():
    do_math()

def do_math():
    x, y = get_value()
    print(x + y)

def get_value():
    x = int(input("What's x? "))
    y = int(input("What's y? "))
    return(x, y)

main()