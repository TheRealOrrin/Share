def main():

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

    while True:
        date = input("Date: ").strip()

        if "," in date:
            try:
                m, d, y = date.split()
                d = d.strip(",")
                d = int(d)
                if m in months and 0 < d < 32:
                    m = months.index(m) + 1
                    print(y, f"{m:02}", f"{d:02}", sep = "-")
                    break
            except ValueError:
                pass

        elif "/" in date:
            try:
                m, d, y = date.split("/")
                m = int(m)
                d = int(d)
                if 0 < m < 13 and 0 < d < 32:
                    print(y, f"{m:02}", f"{d:02}", sep = "-")
                    break
            except ValueError:
                pass

main ()