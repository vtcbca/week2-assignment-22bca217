def replace_vowels(string):
    vowels = "aeiou"
    new_string = ""
    for index, char in enumerate(string):
        if char.lower() in vowels:
            new_string += str(index + 1)
        else:
            new_string += char
    return new_string

string = input("Enter a string: ")
modified_string = replace_vowels(string)
print("Modified String:", modified_string)