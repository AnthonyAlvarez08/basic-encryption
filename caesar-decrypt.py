"""
decrypt the messages from the caesar encrypter
"""
SECRET_KEY = 12
alphabet = tuple("abcdefghijklmnopqrstuvwxyz")


def decrypt(message, key):
    # lowercase just for consitency
    message = message.lower()
    temp = ""
    for i in message:
        place = ord(i) - 97 - key

        # when late letters like z or y get added to secret key they might be above 26
        if place < 0:
            place += 26

        # spaces have an ascii value below all letters so this is to aid that
        if place < 0:
            temp += " "
        else: 
            temp += alphabet[place]

    return temp.capitalize()


def main():
    message = input("Enter a message to decrypt:  ")
    print("Decrypting...")
    print("Your decrypted message is: ", decrypt(message, SECRET_KEY))


if __name__ == '__main__':
    main()
