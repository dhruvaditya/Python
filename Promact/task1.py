def Converter(char, key, mode):
    #char.isprintable() is a method in Python that belongs to the str class. It is used to check if all characters in a given string are printable. The method returns True if all characters in the string are printable, and False otherwise.
    if char.isprintable():
        # we have to shift the char ASCII value by the key
        if mode == "encrypt":
            #ord(char) :- retrieves the ASCII value of the character . the ord() function returns an integer representing the unicode code  point of the given unicode character
            encrypted_char = chr((ord(char) - 32 + key) % 95 + 32)
            #subtraction of 32 is done to shift the ASCII value to the range of 0 to 94 . printable ASCII Range(32 to 126)
            #+key is added to shift the ASCII value by the specified key
            #%95 is used to wrap around the shifted ASCII values within the range of 0 to 94.
            #+32 is added again to shift the ASCII values back to the original printable ASCII range(32 to 126)
        elif mode == "decrypt":
            encrypted_char = chr((ord(char) - 32 - key) % 95 + 32)
            #Inverse is used to decrypt
        else:
            raise ValueError("Invalid mode. Use 'encrypt' or 'decrypt'.")

        return encrypted_char
    else:
        # If the character is not printable, leave it unchanged
        return char


def process_message(message, key, mode):
    #empty string to store the final result
    result = ""
    for char in message:
        #function is called by passing the necessary parameters as shown
        result += Converter(char, key, mode)
    return result


def main():
    # Input will be asked from the user to perform the task
    message = input("Enter the message: ")
    key = int(input("Enter the key (an integer): "))
    mode = input("Enter the mode (encrypt / decrypt): ").lower()#lower converts all the characters to lower_case


    # Process the message based on the chosen mode either encryption or decryption
    result = process_message(message, key, mode)

    # final result printed
    print(f"{mode.capitalize()}ed Message:", result)

#initial starting point of code
if __name__ == "__main__":
    #main function called
    main()
