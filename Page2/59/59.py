from time import time


def generate_passwords():
    passwords = []

    for char1 in range(ord('a'), ord('z') + 1):
        for char2 in range(ord('a'), ord('z') + 1):
            for char3 in range(ord('a'), ord('z') + 1):
                passwords.append(str(chr(char1) + chr(char2) + chr(char3)))

    return passwords


def decipher_message(cipher, k):
    current_key_chat = 0

    deciphered_msg = ''

    for char in cipher:
        deciphered_msg += chr(int(char) ^ ord(k[current_key_chat]))
        current_key_chat = (current_key_chat + 1) % len(k)

    return deciphered_msg


elapsed_time = time()

possible_keys = generate_passwords()

opened_f = open('cipher.txt', 'r')
cipher_chars = opened_f.readline().split(',')

# Key found using text analysis of results of this loop. I don't know what is considered a 'common' word.
'''
for key in possible_keys:
    deciphered_message = decipher_message(cipher_chars, key)

    if deciphered_message.__contains__('the'):
        print(key)
        print(deciphered_message)
'''

deciphered_message = decipher_message(cipher_chars, 'god')

sum_of_ascii_codes = 0

for char in deciphered_message:
    sum_of_ascii_codes += ord(char)

print(sum_of_ascii_codes)
elapsed_time = time() - elapsed_time
print('Time: ' + str(elapsed_time))

