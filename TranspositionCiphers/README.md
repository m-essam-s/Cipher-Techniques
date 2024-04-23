# Transposition Cipher Implementation

This Python script implements a transposition cipher encryption and decryption algorithm. Transposition cipher is a method of encryption where the positions of the characters in the plaintext are shifted according to a specific key.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Functionality](#functionality)
- [Example](#example)
- [License](#license)

## Introduction

The transposition cipher implemented in this script works by rearranging the characters of the plaintext based on a given key. The key is used to determine the order in which the columns of the matrix are read during encryption and decryption.

## Usage

To use the transposition cipher, you can directly call the `_encryption` and `_decryption` functions provided in the script.

```python
# Example usage
PlainText = "My name is Mohamed Essam Saeid, I'm a software engineer at KSIU"
key = "HackingIsFun"

# Encrypt plaintext
encrypted_message = _encryption(PlainText, key)
print("Encrypted Message:", encrypted_message)

# Decrypt ciphertext
decrypted_message = _decryption(encrypted_message, key)
print("Decrypted Message:", decrypted_message)
```

## Functionality

- `_keyHandler(_key)`: This function handles the key provided for encryption and decryption. It ensures uniqueness of characters and fills in missing characters as needed.
- `_encryption(_plainText, _key)`: This function encrypts the given plaintext using the transposition cipher algorithm.
- `_decryption(_cipherText, _key)`: This function decrypts the given ciphertext using the transposition cipher algorithm.

## Example

Suppose we have the following plaintext and key:

```python
PlainText = "My name is Mohamed Essam Saeid, I'm a software engineer at KSIU"
key = "HackingIsFun"
```

The encrypted message would be:

```
Encrypted Message: HswkcseaaraMo  afeMmeaniEanIS  nIoseg,SIat Sdssmr Iutekn   lm' w
```

And after decryption, we would obtain the original plaintext:

```
Decrypted Message: My name is Mohamed Essam Saeid, I'm a software engineer at KSIU
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
