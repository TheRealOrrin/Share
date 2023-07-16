input = input("Input: ")
forbidden_letters = ["a", "e", "i", "o", "u"]

for letter in input:
    if letter.lower() in forbidden_letters:
        input = input.replace(letter, "")
    else:
        continue

print("Output:", input)
