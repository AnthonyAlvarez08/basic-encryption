"""
decrypts text from my vigenere-encrypter
"""
SECRET_KEY = "turtle"
alphabet = tuple("abcdefghijklmnopqrstuvwxyz")
shifts = {f"{alphabet[i]}": i for i in range(len(alphabet))}

def letter_shift(letter, key):
    letter = letter.lower()
    result = ord(letter) - 97 - shifts[key]
    if result < 0:
        result += 26
    if result < 0:
        return letter
    return alphabet[result]

def decrypt(message, key):
    message.lower()
    words = list(message.split())
    result = ""
    key *= 25
    counter = 0

    # encrypt one word at a time
    for z in words:
        for i in z:
            result += letter_shift(i, key[counter])
            counter += 1
        result += " "

    return result.capitalize().strip()


def main():
    message = input("enter a message to decrypt:  ")
    print("Decrypting...")
    print("Your decrypted message is: ", decrypt(message, SECRET_KEY))


if __name__ == '__main__':
    main()
