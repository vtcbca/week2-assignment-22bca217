def print_substring(string, start, end):
    substring = string[start:end]
    print("Substring:", substring)

string = input("Enter a string: ")
start = int(input("Enter the starting index: "))
end = int(input("Enter the ending index: "))

print_substring(string, start, end)
