def digit_sum(number):
    total = 0
    for digit in str(number):
        total += int(digit)
    return total

number = int(input("Enter a number: "))
sum_of_digits = digit_sum(number)
print(f"The sum of the digits of {number} is: {sum_of_digits}")
