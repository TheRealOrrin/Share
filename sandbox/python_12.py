def main():
    height = int(input("What is the height of the pyramid? "))
    print_pyramid(height)

def print_pyramid(n):
    for h in range(n):
        print("#" * (h + 1))

main()
