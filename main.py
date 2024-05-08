from TranspositionCiphers.TranspositionCipher import Cipher

def _performColumnarTransposition(): # OMER's Task
    columnar_transpose=Cipher.ColumnarTransposition() # Create an object of the TranspositionCipher class
    print("Columnar Transposition Cipher Technique")
    print("You've Three Options:")
    print("1. Uniqueness of the or key Handling repeating characters in the key")
    print("2. An integer key in the range of 1 t 9")
    print("3. A uniqueness integer key such as 123456789 or 987654321 the length of the key must be in the range of 0 to 9")
    choice = int(input("Enter the option you want to use: "))
    if choice == 1:
        # Option 1: Handle repeating characters in the key
        PlainText = input("Enter the plain text: ")
        key = input("Enter the key: ")
        if len(key) != len(list(dict.fromkeys(key))):
            print("The key is not unique.")
            print("But it can handle repeating characters.")
            choice=input("Do you want to continue? (y/n): ")
            if choice.lower() != "y":
                exit()
            print("The key after handling: ",columnar_transpose._keyHandler(key))
            
    elif choice == 2:
        # Option 2: An integer key in the range of 1 to 9
        PlainText = input("Enter the plain text: ")
        while True:
          try:
            key = int(input("Enter the key: "))  
            if key<0 or key > 9:
              print("You have entered wrong key.")
              print("The key must be an integer from 1 to 9.")
              choice=input("Do you want to exit? (y/n): ")
              if choice.lower() == "y":
                exit()
            else:
              key = ''.join([str(i) for i in range(key+1)])
              break
          except ValueError:
            print("Invalid input. Please enter an integer.")
            choice=input("Do you want to exit? (y/n): ")
            if choice.lower() == "y":
                exit()    

    elif choice == 3:
        # Option 3: A uniqueness integer key in the range of 0 to 9
        PlainText = input("Enter the plain text: ")
        while True:
            try:
                key = int(input("Enter the key: "))
                if len(str(key)) != len(list(dict.fromkeys(str(key)))):
                    print("Invalid input. The key should be in range from 0 to 9 and unique.")
                    choice=input("Do you want to exit? (y/n): ")
                    if choice.lower() == "y":
                        exit()
                else:    
                    key = str(key)
                    break
            except ValueError:
                print("Invalid input. Please enter an integer.")
                choice=input("Do you want to exit? (y/n): ")
                if choice.lower() == "y":
                    exit()  


    CipherText = columnar_transpose._encryption(PlainText, key)  # Encrypt the plain text
    print("Encrypted Message: ", CipherText)  # Print the encrypted message
    print("Decrypted Message: ", columnar_transpose._decryption(CipherText, key))  # Print the decrypted message



def _performRailFenceTransposition(): # MALAK's Task
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

if __name__ == "__main__": # main 
    
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
    