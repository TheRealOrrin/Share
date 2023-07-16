def main():
    text = input("Type something with an emoticon: ")
    print(convert_emoticon(text))

def convert_emoticon(sentence):
    return sentence.replace(":)", "🙂").replace(":(", "🙁")

main()