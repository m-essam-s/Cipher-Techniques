from TranspositionCiphers.TranspositionCipher import Cipher

if __name__ == "__main__":
    
    PlainText = "My name is Mohamed Essam Saeid, I'm a software engineering student at KSIU" # Plain text
    key = "HackingIsFun" # Key
    tc=Cipher.ColumnarTransposition() # Create an object of the TranspositionCipher class
    
    if not isinstance(PlainText, str) or not isinstance(key, str): # If the plain text or the key is not a string
        print("The plain text and the key must be a string") # Raise a type error
        exit() # Exit the program
        
    if len(key) != len(list(dict.fromkeys(key))): # If the key is not unique
        print("The key is not unique.")
            
        print("But it can handle repeating characters.")
        chois=input("Do you want to continue? (y/n): ") # Ask the user if they want to continue
        if chois.lower() != "y": # If the user does not want to continue
            exit()
        print("The key after handling: ",tc._keyHandler(key))
    
    
    
    
    CipherText=tc._encryption(
        PlainText, 
        key) # Encrypt the plain text
    print(
        "Encrypted Message: ",
          CipherText) # Print the encrypted message
    print(
        "Decrypted Message: ",
        tc._decryption(
            CipherText, 
            key)) # Print the decrypted message
    # print("key after handling: ",_keyHandler(key)) # Handle the key
    # print("sorted key: ",sorted(list(_keyHandler(key)))) # Sort the key
    