def main():
    item = input("Item: ").lower()
    print_calories(item)

def print_calories(fruit_item):
    fruits = [
        {"fruit" : "apple",             "calories" : "130"},
        {"fruit" : "avocado",           "calories" : "50"},
        {"fruit" : "banana",            "calories" : "110"},
        {"fruit" : "cantaloupe",        "calories" : "50"},
        {"fruit" : "grapefruit",        "calories" : "60"},
        {"fruit" : "grapes",            "calories" : "90"},
        {"fruit" : "honeydew melon",    "calories" : "50"},
        {"fruit" : "kiwifruit",         "calories" : "90"},
        {"fruit" : "lemon",             "calories" : "15"},
        {"fruit" : "lime",              "calories" : "20"},
        {"fruit" : "nectarine",         "calories" : "60"},
        {"fruit" : "orange",            "calories" : "80"},
        {"fruit" : "peach",             "calories" : "60"},
        {"fruit" : "pear",              "calories" : "100"},
        {"fruit" : "pineapple",         "calories" : "50"},
        {"fruit" : "plums",             "calories" : "70"},
        {"fruit" : "strawberries",      "calories" : "50"},
        {"fruit" : "sweet cherries",    "calories" : "100"},
        {"fruit" : "tangerine",         "calories" : "50"},
        {"fruit" : "watermelon",        "calories" : "80"}
    ]

    for fruit in fruits:
        if fruit_item == fruit["fruit"]:
            print("Calories: ", fruit["calories"])
        else:
            continue
    print(end = "")

main()