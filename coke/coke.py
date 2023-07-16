def main():
    due = 50
    while due > 0:
        print("Amount Due:", due)
        due = due - payment()
    print("Change Owed:", abs(due))

def payment():
    while True:
        coin = int(input("Insert Coin: "))
        if coin == 5 or coin == 10 or coin == 25:
            return coin
        else:
            return 0

main()
