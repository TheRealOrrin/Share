def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if check_start(s) and check_length(s) and check_numbers(s) and check_firstnum(s) and check_punctuation(s):
        return True
    else:
        return False

def check_start(s):
    if len(s) > 1:
        if s[0].isalpha() and s[1].isalpha():
            return True
        else:
            return False
    else:
        return False

def check_length(s):
     length = len(s)
     if 2 <= length <= 6:
        return True
     else:
          return False

def check_numbers(s):
    for letter in range(len(s)):
        if s[letter].isnumeric():
            if s.find(s[letter]) < len(s) - 2:
                return False
        else:
            continue
    return True

def check_firstnum(s):
    for letter in range(len(s)):
        if s[letter] == "0":
            if s[letter - 1].isnumeric():
                return True
            else:
                return False
    return True

def check_punctuation(s):
    for char in range(len(s)):
        if s[char].isalnum():
            continue
        else:
            return False
    return True

main()