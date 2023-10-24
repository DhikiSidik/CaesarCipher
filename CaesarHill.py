alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
          'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z']

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Ini teks setelah dienkripsi: {cipher_text}")

def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"Ini teks setelah didekripsi: {plain_text}")

what_to_do = input("Tuliskan 'E' jika Anda ingin mengenkripsi pesan, dan tuliskan 'D' jika Anda ingin mendekripsi pesan:\n")
text = input("Tuliskan pesan:\n")
shift = int(input("Masukkan shift key:\n"))

if what_to_do == "E":
    encryption(plain_text=text, shift_key=shift)
elif what_to_do == "D":
    decryption(cipher_text=text, shift_key=shift)
