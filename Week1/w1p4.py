def is_armstrong(number):
    num_str = str(number)
    num_len = len(num_str)
    total = 0
    for digit in num_str:
        total += int(digit) ** num_len
    if number == total:
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
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
