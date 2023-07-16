def main():
    word = input("camelCase: ")
    print("snake_case: " + make_snake(word))

def make_snake(w):
    length = len(w)
    for letter in range(length):
        if letter == 0:
            continue
        if w[letter].isupper():
            w = w.replace(w[letter], "_" + w[letter].lower())
    return w

main()