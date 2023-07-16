def main():
    size = int(input("What's the size of the square? "))
    print_square(size)

def print_square(s):
    for _ in range(s):
        print("." * s)

main()