def main():
    print_level(get_percentage("Fraction: "))

def get_percentage(fraction):
    while True:
        try:
            level = input(fraction).split("/")
            x = int(level[0])
            y = int(level[1])
            z = round((x / y) * 100)
            if x > y:
                raise ValueError
            return z
        except (ValueError, ZeroDivisionError):
            pass

def print_level(n):
    if n < 2:
        print("E")
    elif n > 98:
        print("F")
    else:
        print(f"{n}%")
main()