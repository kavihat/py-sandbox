# Program to print the count of a number as well as the number when an input number is given.
# It should be done without converting input to string or by using any string functions


count = 1
reversed_num = 0
user_input = int(input("Enter you input"))
while user_input:
    first_digit = user_input % 10
    user_input = int(user_input / 10)
    second_digit = user_input % 10
    if first_digit == second_digit:
        count = count + 1
    else:

        if count < 10:
            partial_output = first_digit * 10 + count
            reversed_num = reversed_num * 100 + partial_output

        else:
            partial_output = count * 10 + first_digit
            reversed_num = reversed_num * 1000 + partial_output

        count = 1

final_output = 0
while reversed_num > 0:
    Reminder = reversed_num % 10
    final_output = final_output * 10 + Reminder
    reversed_num = int(reversed_num / 10)

print(final_output)
