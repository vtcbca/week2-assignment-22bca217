def replace_vowels(string):
    vowels = "aeiou"
    new_string = ""
    for index, char in enumerate(string):
        if char.lower() in vowels:
            new_string += str(index)
        else:
            new_string += char
    return new_string

string = input("Enter a string: ")  # User input: Amit
modified_string = replace_vowels(string)
print("Modified String:", modified_string)  # Output: "0m2t"
