choice = input("Do you want to encrypt (e) or decrypt (d)? ")
if choice == "e":
    phrase = input("Input a phrase to encrypt: ")

    ascii_phrase = [ord(c)for c in phrase]
    ascii_phrase2 = []

    for number in ascii_phrase:
        ascii_phrase2.append(number+3)

    encrypted = [chr(c) for c in ascii_phrase2]
    encrypted_str = ""
    for letter in encrypted:
        encrypted_str += letter
    print(encrypted_str)

if choice =="d":
    phrase = input("Input a phrase to decrypt: ")

    ascii_phrase = [ord(c)for c in phrase]
    ascii_phrase2 = []

    for number in ascii_phrase:
        ascii_phrase2.append(number-3)

    decrypted = [chr(c) for c in ascii_phrase2]
    decrypted_str = ""
    for letter in decrypted:
        decrypted_str += letter
    print(decrypted_str)





