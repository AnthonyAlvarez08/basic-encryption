"""
This will be a caesar cipher program
It is a simple encryption method that is easy to crack
works perfectly!
"""
alphabet = tuple("abcdefghijklmnopqrstuvwxyz")

# cannot be changed once compiled
SECRET_KEY = 12

def encrypt(message, key):
    # lowercase just for consitency
    message = message.lower()
    temp = ""
    for i in message:
        place = ord(i) - 97 + key

        # when late letters like z or y get added to secret key they might be above 26
        if place >= 26: place -= 26

        # spaces have an ascii value below all letters so this is to aid that
        if place < 0:
            temp += " "
        else:
            temp += alphabet[place]

    return temp.capitalize()

def main():
    message = input("Enter a message to encrypt:  ")
    print("Encrypting...")
    print("Your encrypted message is: ", encrypt(message, SECRET_KEY))


if __name__ == '__main__':
    main()