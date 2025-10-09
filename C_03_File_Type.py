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


# main routine starts here
while True:
    file_type = get_filetype()

    # if user chose 'i', ask if they want image or integer
    if file_type == "i":

        want_image = input("Press <enter> for an integer or any key for an image")
        if want_image.lower() == "":
            file_type = "integer"
        else:
            file_type = "image"
            
    print(f"You chose {file_type}")

    if file_type == "xxx":
        break