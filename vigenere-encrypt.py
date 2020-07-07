"""
Vigenere cipher program
it is many caesar ciphers with different keys based on a keyword
a = 0, b = 1, ..., z = 25
it is much more safer that caesar cipher, immune to brute force and frequency analysis
Works!!!
"""

SECRET_KEY = "turtle"
alphabet = tuple("abcdefghijklmnopqrstuvwxyz")
shifts = {f"{alphabet[i]}": i for i in range(len(alphabet))}

# works
def letter_shift(letter, key):
    result = ord(letter) - 97 + shifts[key]
    if result >= 26: result -= 26
    if result < 0: return letter
    return alphabet[result]

# works
def encrypt(message, key):
    message.lower()
    words = list(message.split())
    result = ""; key *= 25; counter = 0

    # encrypt one word at a time
    for z in words:
        for i in z:
            result += letter_shift(i, key[counter])
            counter += 1
        result += " "

    return result.capitalize().strip()


def main():
    message = input("enter a message to encrypt:  ")
    print("Encrypting...")
    print("Your encrypted message is: ", encrypt(message, SECRET_KEY))

if __name__ == '__main__':
    main()
