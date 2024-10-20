README for the GitHub Repository:
markdown
Copy code
# Caesar Cipher in Python

## Overview
This repository contains a Python program that implements the **Caesar Cipher**, a simple yet classic encryption technique. The Caesar Cipher shifts each letter in a message by a given shift value, allowing for **encryption** and **decryption** of text.

## Features
- **Encrypt** text with a specified shift value.
- **Decrypt** text using the same shift value to retrieve the original message.
- Handles both **uppercase** and **lowercase** letters, preserving their cases.
- Keeps **non-alphabet characters** (like punctuation and spaces) unchanged.
- **User-friendly input**: easily specify the message, shift value, and encryption mode.

## How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/nitinbeniwal/PRODIGY_CS_01.git

   cd caesar-cipher-python

Run the caesar_cipher.py file:

bash

Copy code

python caesar_cipher.py

Follow the prompts:


Enter your message.
Specify the shift value.
Choose (e)ncrypt to encrypt or (d)ecrypt to decrypt the message.

Example
Encryption:
Input:
Message: my name is nitin
Shift: 3
Mode: encrypt
Output: pb qdph lv qlwln


Decryption:
Input:
Message: pb qdph lv qlwln
Shift: 3
Mode: decrypt
Output: my name is nitin


Code Explanation
The caesar_cipher function takes three parameters: text (the message), shift (the shift value), and mode (either 'encrypt' or 'decrypt').
Uses the ord() and chr() functions to shift characters while maintaining their case.
For decryption, the shift is reversed automatically.
Supports alphabetic characters while preserving non-alphabetic characters as they are.


Requirements
Python 3.x


License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

Acknowledgments
This project was built as part of my learning journey in Python programming and basic cryptography.

