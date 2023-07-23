def main():

    groceries = {}

    while True:
        try:
            item = input("").upper()
        except EOFError:
            break
        if item in groceries.keys():
            groceries[item] += 1
        else:
            new_item = {f"{item}" : 1}
            groceries.update(new_item)

    print_groceries(groceries)

def print_groceries(to_print):
    print()
    x = list(to_print.keys())
    x.sort()
    for n in x:
        print(to_print[n], n)

main()