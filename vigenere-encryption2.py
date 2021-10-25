from hashlib import sha1

# encrypts a message given a key
def encrypt(message: str, key: str) -> str:

    # hash the key to make it more secure
    # key = str(sha1(key.encode()).hexdigest())

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

    # hash the key to make it more secure
    # key = str(sha1(key.encode()).hexdigest())

    arr = list(message)

    # make a key generator that loops so I can use it for as long as the message
    key_gen = map(str, key * (len(message) // len(key) + 1))

    # shifts the letters in the message according to the key given
    for i in range(len(arr)):
        arr[i] = chr(ord(arr[i]) - ord(next(key_gen)))

    # collapse the array into a string again
    return ''.join(arr)



# encrypt = input('Hello! would you like to encrypt (e) or decrypt (d) a message?') == 'e'
KEY = 'Im excaping to the one place that hasnt been corrupted by capitalism... Sapce!'
print(encrypt(open('hehe.txt', 'r').read(), KEY))