print('''
  ___   __   ____  ____  ____  ____     ___  __  ____  _  _  ____  ____ 
 / __) / _\ (  __)/ ___)(  __)(  _ \   / __)(  )(  _ \/ )( \(  __)(  _ \
( (__ /    \ ) _) \___ \ ) _)  )   /  ( (__  )(  ) __/) __ ( ) _)  )   /
 \___)\_/\_/(____)(____/(____)(__\_)   \___)(__)(__)  \_)(_/(____)(__\_)
''')

mode = (input("Enter Operation (ENCRYPT/DECRYPT")).lower()

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']


def encrypt(message, counter, alphabets):
    message = list(message)
    encr_msg = []
    for i in message:
        if i in alphabets:
            index = alphabets.index(i)
            encrypt_index = index + counter
            if encrypt_index > 25:
                rotation_count = encrypt_index - 25
                encr_msg.append(alphabets[rotation_count])

            else:
                encr_msg.append(alphabets[encrypt_index])
        else:
            encr_msg.append(i)
    encr_msg = ("".join(encr_msg)).title()
    return encr_msg


def decrypt(coded_msg, decode_counter, alphabets):
    coded_msg = list(coded_msg)
    deciphr = []
    for i in coded_msg:
        if i in alphabets:
            index = alphabets.index(i)
            decrypt_index = index - decode_counter
            if decrypt_index < 0:
                rotation_count = 25 + decrypt_index
                deciphr.append(alphabets[rotation_count])
            else:
                deciphr.append(alphabets[decrypt_index])
        else:
            deciphr.append(i)
    deciphr = (''.join(deciphr)).title()
    return deciphr


if mode == "encrypt":
    message = (input("Enter your Message ")).upper()
    counter = int(input("Enter Secret Cipher Counter"))
    print(f"Encrypted MSG::{encrypt(message, counter, alphabets)}")
elif mode == 'decrypt':
    coded_msg = input("Enter your Coded Message").upper()
    decode_counter = int(input("Enter the Decode Counter "))
    print(f"Decrypted Code: {decrypt(coded_msg, decode_counter, alphabets)}")
