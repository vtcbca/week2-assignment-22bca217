def is_palindrome(number):
    reverse = int(str(number)[::-1])
    if number == reverse:
        return True
    else:
        return False

def validate_integer_input():
    while True:
        try:
            number = int(input("Enter an integer number: "))
            return number
        except ValueError:
            print("Invalid input. Please enter an integer number.")

number = validate_integer_input()
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

