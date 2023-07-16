def main():
    print_column()

def print_column():
    height = get_height()
    width = get_width()
    for _ in range(height):
        print("o" * width)

def get_height():
    while True:
        h = int(input("What's the height? "))
        if h > 0:
            break
    return h

def get_width():
    while True:
        w = int(input("What's the width? "))
        if w > 0:
            break
    return w

main()