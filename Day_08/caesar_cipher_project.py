#caesar cipher
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

write = input("type encode to 'encrypt' , type decode to 'decrypt'").lower()
print(write)
massage = input("type your massage").lower()
print(massage)
shift_no = int(input("type the shift number"))
print(shift_no)



def encrypt(orignal_text , shift_amount):
    cipher_text=""
    for letter in alphabet:
        shift_position = alphabet.index(letter)+shift_amount
        cipher_text += alphabet[shift_position]
    print(f"here is the encoded text {cipher_text}")

encrypt(orignal_text=massage, shift_amount= shift_no)