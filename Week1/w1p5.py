def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count

string = input("Enter a string: ")
vowel_count = count_vowels(string)
print(f"The number of vowels in the string is: {vowel_count}")
