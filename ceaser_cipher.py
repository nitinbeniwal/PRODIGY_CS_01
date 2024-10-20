# Caesar Cipher implementation in Python

def caesar_cipher(text, shift, mode='encrypt'):
    result_text = ""
   
    if mode == 'decrypt':
        shift = -shift
    
    
    for char in text:
       
        if char.isalpha():
            shift_amount = shift % 26
            base = ord('a') if char.islower() else ord('A')
            result_text += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result_text += char
    return result_text

message = input("Enter your message: ")
shift_value = int(input("Enter the shift value: "))
choice = input("Do you want to (e)ncrypt or (d)ecrypt the message? ")

if choice.lower() == 'e':
    result = caesar_cipher(message, shift_value, mode='encrypt')
    print(f"Encrypted message: {result}")
elif choice.lower() == 'd':
    result = caesar_cipher(message, shift_value, mode='decrypt')
    print(f"Decrypted message: {result}")
else:
    print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
