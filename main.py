# Neel Patel

# encoder stores the encoded password to a new variable
def encode(password):
    new_password = ""

    # encode password
    for num in password:
        new_password += str((int(num) + 3) % 10)

    # return password
    return new_password

# decodes a password
# def decode(new_password):


def main():
    run = True
    while run:
        # print menu options
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")

        # ask for user input
        user_input = int(input("Please enter an option: "))

        # encode password
        if user_input == 1:
            password = input("Please enter your password to encode: ")
            new_password = encode(password)
            print("Your password has been encoded and stored!\n")

        # decode password
        elif user_input == 2:
            decode = decode(new_password)
            print(f"The encoded password is {new_password}, and the original password is {decode}.\n")

        elif user_input == 3:
            run = False


if __name__ == "__main__":
    main()