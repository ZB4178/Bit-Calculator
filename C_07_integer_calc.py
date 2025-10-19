# Ask user for width and loop until they
# enter a number that is more than zero
def int_check(question, low):

    error = f"Please enter a number that is more than or equal to {low}\n"
    while True:

        try:
            #Ask user for number
            response = int(input(question))

            #Check number is more than zero
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


#calculates how many bits are needed to represent an integer
def integer_calc():
    # ask the user to enter an integer (more than/equal to 0)
    integer = int_check(question="integer: ", low=0)

     # convert the integer to binary and work out number of bits needed
    raw_binary = bin(integer)

    # remove the leady 0b from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)

    # setup answer and return it
    answer = f"{integer} in binary is {binary}. We need {num_bits} to represent it."

    return answer

# main routine goes here
integer_answer = integer_calc()
print(integer_answer)