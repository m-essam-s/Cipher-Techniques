from TranspositionCiphers.TranspositionCipher import Cipher

def _performColumnarTransposition(): # OMAR's Task
    columnar_transpose=Cipher.ColumnarTransposition() # Create an object of the TranspositionCipher class
    
    print("You've Three Options:")
    print("\t1. Uniqueness of the or key Handling repeating characters in the key")
    print("\t2. An integer key in the range of 1 t 9")
    print("\t3. A uniqueness integer key such as 123456789 or 987654321 the length of the key must be in the range of 0 to 9")
    print("\t4. Main Menu")
    print("\t5. Exit")
    
    choice = int(input("Enter the option you want to use: "))
    if choice == 1:
        print("Option 1: Uniqueness of the key")
        print("\t1. Encryption")
        print("\t2. Decryption")
        print("\t3. Previous Menu")
        print("\t4. Main Menu")
        print("\t5. Exit")
        _op = input("Enter your choice: ")
        
        if _op == '1':
            print("Option 1: Encryption")
            plain_text = input("Enter the plain text: ")
            key = input("Enter the key: ")
            print(f"Encrypted Message: {columnar_transpose._encryption(plain_text, key)}")
        
        elif _op == '2':
            print("Option 2: Decryption")
            cipher_text = input("Enter the cipher text: ")
            key = input("Enter the key: ")
            print(f"Decrypted Message: {columnar_transpose._decryption(cipher_text, key)}")
            
        elif _op == '3':
            print("Returning to the previous menu...")
            _performColumnarTransposition()
        
        elif _op == '4':
            print("Returning to the main menu...")
            main()
        
        elif _op == '5':
            print("Exiting the program...")
            exit()
            
    elif choice == 2:
        # Option 2: An integer key in the range of 1 to 9
        def key_checker():
            try:
                _key = int(input("Enter the key: "))  
                if _key<0 or _key > 9:
                    print("You have entered wrong key.")
                    print("The key must be an integer from 1 to 9.")
                    _key = key_checker()
                else:
                    _key = ''.join([str(i) for i in range(_key+1)])
            except ValueError:
                print("Invalid input.")
                print("Please enter an integer (0:9).")
                _key = key_checker()
                
            return _key
            
        print("Option 2: An integer key in the range of 1 to 9")
        print("\t1. Encryption")
        print("\t2. Decryption")
        print("\t3. Previous Menu")
        print("\t4. Main Menu")
        print("\t5. Exit")
        _op = input("Enter your choice: ")
        
        if _op == '1':
            print("Encryption Selected: Columnar Transposition Cipher")
            plain_text = input("Enter the plain text: ")
            key = key_checker ()
            print(f"Encrypted Message: {columnar_transpose._encryption(plain_text, key)}")
        
        elif _op == '2':
            print("Decryption Selected: Columnar Transposition Cipher")
            cipher_text = input("Enter the cipher text: ")
            key = key_checker ()
            print(f"Decrypted Message: {columnar_transpose._decryption(cipher_text, key)}")
        
        elif _op == '3':
            print("Returning to the previous menu...")
            _performColumnarTransposition()
        
        elif _op == '4':
            print("Returning to the main menu...")
            main()
        
        elif _op == '5':
            print("Exiting the program...")
            exit()


    elif choice == 3:
        
        def _key_checker():
            try:
                _key = int(input("Enter the key: "))
                if len(str(_key)) != len(list(dict.fromkeys(str(_key)))):
                    print("Invalid input. The key should be unique.")
                    _key=_key_checker()
                else:
                    return str(_key)
            except ValueError:
                print("Invalid input. Please enter an integer.")
                _key=_key_checker()
            return _key
        
        print("Option 3: A uniqueness integer key in the range of 0 to 9")
        print("\t1. Encryption")
        print("\t2. Decryption")
        print("\t3. Previous Menu")
        print("\t4. Main Menu")
        print("\t5. Exit")
        _op = input("Enter your choice: ")
        
        if _op == '1':
            print("Encryption Selected: Columnar Transposition Cipher")
            plain_text = input("Enter the plain text: ")
            key = _key_checker()
            print(f"Encrypted Message: {columnar_transpose._encryption(plain_text, key)}")
            
        elif _op == '2':
            print("Decryption Selected: Columnar Transposition Cipher")
            cipher_text = input("Enter the cipher text: ")
            key = _key_checker()
            print(f"Decrypted Message: {columnar_transpose._decryption(cipher_text, key)}")
        
        elif _op == '3':
            print("Returning to the previous menu...")
            _performColumnarTransposition()
        
        elif _op == '4':
            print("Returning to the main menu...")
            main()
        
        elif _op == '5':
            print("Exiting the program...")
            exit()
    
    elif choice == 4:
        print("Returning to the main menu...")
        main()
     
    elif choice == 5:
        print("Exiting the program...")
        exit()
    
    else:
        print("Invalid choice")
        print("Please enter a valid choice.")
        _performColumnarTransposition()


def _performRailFenceTransposition(): # MALAK's Task
    rail_fence=Cipher.RailFenceTransposition() # Create an object of the RailFenceTransposition class
    
    print("You've four Options:")
    print("\t1:Rail Fence Encryption\n\t2:Rail Fence Decryption\n\t3:Main Menu\n\t4:Exit")
    choice =input("Enter your choice: ") 
    if choice == '1':
        print("Encryption Selected: Rail Fence Cipher")
        plain_text = input("Enter your message: ")
        depth = int(input("Enter The Depth (a single number): "))
        print(f"Encrypted Message: {rail_fence._encryption(plain_text, depth)}")
        exit()
    
    elif choice == '2':
        print("Decryption Selected: Rail Fence Cipher")
        cipher_text = input("Enter your Cipher Text: ")
        depth = int(input("Enter The Depth (a single number): "))
        print(f"Decrypted Message: {rail_fence._decryption(cipher_text, depth)}")
        exit()
    
    elif choice == '3':
        print("Returning to the main menu...")
        main()
            
    elif choice == '4':
        print("Exiting the program...")
        exit()
    
    else:
        print("Invalid Choice")
        print("Please enter a valid choice.")
        _performRailFenceTransposition()

def main():
    print("Only Columnar Transposition, and Rail Fence Transposition are available now.")
    print("\t1. Columnar Transposition\n\t2. Rail Fence Transposition\n\t3. Exit")
    
    try:    
        choice = int(input("Enter the cipher technique you want to use: "))
        
        if choice == 1:
            print("-------Columnar Transposition Cipher Technique-------")
            _performColumnarTransposition()
        elif choice == 2:
            print("-------------Rail Fence Cipher Technique-------------")
            _performRailFenceTransposition()
        elif choice == 3:
            print("Exiting the program...")
            exit()
        else:
            print("Invalid choice")
            print("Please enter a valid choice.")
            main()
            
    except ValueError:
        print("Invalid input. Please enter an integer.")
        main()
        
if __name__ == "__main__": # main 
    main()
    
