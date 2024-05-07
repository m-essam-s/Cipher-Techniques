from TranspositionCiphers.TranspositionCipher import Cipher
'''
OMER SAMEH TASKs:
1. Complet the Implementation of _performColumnarTransposition function
this function should take the plain text and the key as input from the user and then:
    a. Check the uniqueness of the key or handle repeating characters in the key.
    b. Check if the key is an integer in the range of 1 to 9.
    c. Check if the key is a unique integer key such as 123456789 or 987654321, the length of the key must be in the range of 0 to 9.
    d. Encrypt the plain text using the Columnar Transposition Cipher technique.
    e. Print the encrypted message.
    f. Decrypt the encrypted message using the Columnar Transposition Cipher technique.
2. Test the Columnar Transposition Cipher technique, and.
3. make sure it works correctly.
4. Debug and test the whole program, !!!!!! after malak khaled end her task.
5. PLEASE DON'T FORGET TO ADD COMMENTS TO THE CODE.
6. PLEASE DON'T TOUCH THE CODE OF THE ColumnarTransposition() class in the TranspositionCipher.py file.

Malak Khaled Task:
1. Implement the Rail Fence Transposition Cipher technique in the RailFenceTransposition class.
2. Implement the _performRailFenceTransposition function to perform the Rail Fence Transposition Cipher technique.
3. Test the Rail Fence Transposition Cipher technique, and.
4. make sure it works correctly.
(Done)..........................

Best of luck.
'''
def _performColumnarTransposition(PlainText, key): # OMER SAMEH TASK: please debug and test this function and make sure it works correct logic and after malak finish her task please debug and test the whole program
    columnar_transpos=Cipher.ColumnarTransposition() # Create an object of the TranspositionCipher class
    print("Columnar Transposition Cipher Technique")
    print("You've Three Options:")
    print("1. Uniqueness of the or key Handling repeating characters in the key")
    print("2. An integer key in the range of 1 t 9")
    print("3. A uniqueness integer key such as 123456789 or 987654321 the length of the key must be in the range of 0 to 9")
    choice = int(input("Enter the option you want to use: "))
    if choice == 1:
        PlainText = input("Enter the plain text: ")
        # "My name is Mohamed Essam Saeid, I'm a software engineering student at KSIU" # Plain text
        key = input("Enter the key: ")
            #"HackingIsFun" # Key
        if not isinstance(PlainText, str) or not isinstance(key, str):
            print("The plain text and the key must be a string")
            exit()
        if len(key) != len(list(dict.fromkeys(key))):
            print("The key is not unique.")
            print("But it can handle repeating characters.")
            chois=input("Do you want to continue? (y/n): ")
            if chois.lower() != "y":
                exit()
            print("The key after handling: ",columnar_transpos._keyHandler(key))
            
    elif choice == 2:
        PlainText = input("Enter the plain text: ")
        
        Wrong_key = 0
        while True:
            key = int(input("Enter the key: "))    
            try:
                key = int(key)
            except ValueError:
                if Wrong_key == 3:
                    print("You have entered wrong key 3 times.")
                    exit()
                Wrong_key += 1
                print("The key must be an integer")
                print("You have", Wrong_key, " times.")

    elif choice == 3:
        PlainText = input("Enter the plain text: ")
        # "My name is Mohamed Essam Saeid, I'm a software engineering student at KSIU" # Plain text
        key = input("Enter the key: ")
            #"HackingIsFun" # Key
        if not isinstance(PlainText, str) or not isinstance(key, int):
            print("The plain text must be a string and the key must be an integer")
            exit()
        if len(str(key)) != len(list(dict.fromkeys(str(key)))):
            print("The key is not unique.")
            print("But it can handle repeating characters.")
            chois=input("Do you want to continue? (y/n): ")
            if chois.lower() != "y":
                exit()
            print("The key after handling: ",columnar_transpos._keyHandler(str(key)))
        if len(str(key)) < 0 or len(str(key)) > 9:
            print("The key must be in the range of 0 to 9")
            exit()
        key = str(key)
    
    CipherText = columnar_transpos._encryption(PlainText, key)  # Encrypt the plain text
    print("Encrypted Message: ", CipherText)  # Print the encrypted message
    print("Decrypted Message: ", columnar_transpos._decryption(CipherText, key))  # Print the decrypted message


def _performRailFenceTransposition(): # MALAK KHALED TASK
    rail_fence=Cipher.RailFenceTransposition() # Create an object of the RailFenceTransposition class
    print("1:encrypt  2:decrypt")
    choice =input("Enter your choice (1 or 2): ") 
    if choice == '1':
        print("Encryption Selected: Rail Fence Cipher")
        msg = input("Enter your message: ").strip()
        key = int(input("Enter The Depth (a single number): "))
        print("Encrypted Message:", rail_fence._encryption(msg, key))

    elif choice == '2':
        print("Decryption Selected: Rail Fence Cipher")
        CI = input("Enter your Cipher Text: ").strip()
        key = int(input("Enter The Depth (a single number): "))
        print("Decrypted Message:", rail_fence._decryption(CI, key))

    
    


if __name__ == "__main__":
    columnar_transpos=Cipher.ColumnarTransposition() # Create an object of the TranspositionCipher class
    real_fence_transpos=Cipher.RailFenceTransposition() # Create an object of the RailFenceTransposition class
    
    print("Only Columnar Transposition, and Rail Fence Transposition are available now.")
    print("1. Columnar Transposition\n2. Rail Fence Transposition")
    choice = int(input("Enter the cipher technique you want to use: "))
    wrong_choice = 0
    while True:    
        if choice == 1:
            _performColumnarTransposition()
        elif choice == 2:
            _performRailFenceTransposition()
        else:
            print("Invalid choice")
            wrong_choice += 1
            if wrong_choice == 3:
                print("You have entered wrong choice 3 times.")
                print("Exiting the program...")
                exit()
    
    
    
    