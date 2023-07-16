def main():

    meal_time = input("What time is it? ")
    hour = convert(meal_time)

    if 7 <= hour <= 8:
        print("breakfast time")
    elif 12 <= hour <= 13:
        print("lunch time")
    elif 18 <= hour <= 19:
        print("dinner time")

def convert(time):
    hrs, part2 = time.split(":")
    hrs = float(hrs)

    if part2.endswith("p.m."):
        hrs += 12
        mins = part2.split(" ").pop(0)
    elif part2.endswith("a.m."):
        mins = part2.split(" ").pop(0)
    else:
        mins = part2

    mins = float(mins) / 60

    return hrs + mins

if __name__ == "__main__":
    main()