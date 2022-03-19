alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text, num_shift, cipher_direction):
    end_text = ""
    for char in start_text:
        pos = alphabet.index(char)
        if cipher_direction == "encode":
            new_pos = pos + num_shift
        elif cipher_direction == "decode":
            new_pos = pos - num_shift
        new_char = alphabet[new_pos]
        end_text += new_char
    print(f"The {cipher_direction}d text is {end_text}")

caesar(start_text=text, num_shift=shift, cipher_direction=direction)
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for char in plain_text:
#         pos = alphabet.index(char)
#         new_pos = pos + shift_amount
#         new_char = alphabet[new_pos]
#         cipher_text += new_char
#     print(f"The encoded text is {cipher_text}")
#
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for char in cipher_text:
#         pos = alphabet.index(char)
#         new_pos = pos - shift_amount
#         new_char = alphabet[new_pos]
#         plain_text += new_char
#     print(f"The encoded text is {plain_text}")
#
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)


