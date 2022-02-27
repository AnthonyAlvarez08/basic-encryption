
# encrypts a message given a key
def encrypt(message: str, key: str) -> str:

    arr = list(message)

    # make a key generator that loops so I can use it for as long as the message
    key_gen = map(str, key * (len(message) // len(key) + 1))

    # shifts the letters in the message according to the key given
    for i in range(len(arr)):
        arr[i] = chr(ord(arr[i]) + ord(next(key_gen)))

    # collapse the array into a string again
    return ''.join(arr)


# encrypts a message given a key
def decrypt(message: str, key: str) -> str:

    arr = list(message)

    # make a key generator that loops so I can use it for as long as the message
    key_gen = map(str, key * (len(message) // len(key) + 1))

    # shifts the letters in the message according to the key given
    for i in range(len(arr)):
        arr[i] = chr(ord(arr[i]) - ord(next(key_gen)))

    # collapse the array into a string again
    return ''.join(arr)



key = input('Enter the key you would like to use: ')
option = input('Hello! would you like to encrypt (e) or decrypt (d) a message? ')
while not option in 'eEdD':
    print('Invalid option, please try again')
    option = input('Hello! would you like to encrypt (e) or decrypt (d) a message? ')

text = open(input('Enter the file name of the input file (place in the same directory as this program): '), 'r').read()
print('the result will be output to a file called \'output.txt\'')

with open('output.txt', 'w') as fout:
    if option in 'eE':
        print(encrypt(text, key), file=fout, end='')
    else:
        print(decrypt(text, key), file=fout, end='')