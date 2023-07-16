def main():
    square()

def get_input():
    return input("What number do you want to have squared? ")

def square():
    x = int(get_input())
    print(x ** 2)

main()