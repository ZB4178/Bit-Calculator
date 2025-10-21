# generates headings (eg: ----- heading -----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# displays instructions
def instructions():
    statement_generator(statement="Instructions", decoration="-")

    print('''
- Type in the file type you want converted
- It will convert Text, Images and Integers
- It will loop, so when finished type "xxx"
    ''')



# ask users for file type (integer / image / text / xxx)
def get_filetype():

    while True:
        response = input("File type: ").lower()

        # check for 'i' or the exit code
        if response == "xxx" or response =="i":
            return response

        # check if it's an integer
        elif response in ['integer', 'int']:
            return "integer"

        # check if it's an image
        elif response in ['image', 'picture', 'img', 'p']:
            return "image"

        # check if it's text
        elif response in ['text', 'txt', 't']:
            return "text"

        # if the response is invalid output n error
        else:
            print("Please input a valid file type")


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
def image_calc():
    # get the image dimensions
    width = int_check("width: ", low=1)
    height = int_check("Height: ", low=1)

     # calculate the number of pixels and multiply by 24 to get the number of bits
    num_pixels = width * height
    num_bits= num_pixels * 24

    # setup answer and return it
    answer = (f"Number of pixels: {width} x {height} = {num_pixels} "
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer


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

# Calculates numbers of bits needed to represent text in ascii
def calc_text_bits():

    # Get text from user
    response=input("Enter some text: ")

    # Calculate bits needed
    num_chars=len(response)
    num_bits=num_chars*8

    # Setup answer and return it
    answer = (f"{response} has {num_chars} characters."
              f"\nWe need {num_chars} x 8 bits to represent it, which is {num_bits} bits")

    return answer



# main routine starts here

# display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()


while True:
    file_type = get_filetype()

    if file_type == "xxx":
        break

    # if user chose 'i', ask if they want image or integer
    if file_type == "i":

        want_image = input("Press <enter> for an integer or any key for an image")
        if want_image.lower() == "":
            file_type = "integer"
        else:
            file_type = "image"

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        integer_answer = integer_calc()
        print(integer_answer)
    else:
        text_answer = calc_text_bits()
        print(text_answer)

