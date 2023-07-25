def main():
    date = get_date()
    print_date(date)

def get_date():
    while True:
        try:
            x = input("Date: ")
            x = process_date(x)
            if x == False:
                raise ValueError
            else:
                return x
        except ValueError:
            pass

def process_date(y):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    if "," in y:
        y = y.split(" ")
        y[1] = y[1].strip(",")
        if y[0] in months and 0 < int(y[1]) < 32:
            y[0] = months.index(y[0]) + 1
            return y
        else:
            return False
    elif "/" in y:
        y = y.split("/")
        if 0 < int(y[0]) < 13 and 0 < int(y[1]) < 32:
            return y
        else:
            return False
    else:
        return False

def print_date(v):
    d = int(v[1])
    m = int(v[0])
    y = int(v[2])

    print(y, f"{m:02}", f"{d:02}", sep="-")

main ()