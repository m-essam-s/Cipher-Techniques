from math import ceil as _roundUp # ceil is a function that rounds up
class Cipher:
# constructor
    class RailFenceTransposition: # MALAK's Task
        def __init__(self):
            self._key = "" # Key
            self._plainText = "" # Plain text
            self._cipherText = "" # Cipher text
        
        def _encryption(_plainText, _key):
            fence = [[] for _ in range(_key)]
            rail = 0
            direction = 1
            for char in _plainText:
                fence[rail].append(char)
                rail += direction
                if rail == _key - 1 or rail == 0:
                    direction = -direction
            cipherText = ''.join([c for rail in fence for c in rail])
            return cipherText
        
        def _decryption(_cipherText, _key):
            fence = [[] for _ in range(_key)]
            rail = 0
            direction = 1
            for char in _cipherText:
                fence[rail].append(None)
                rail += direction
                if rail ==_key - 1 or rail == 0:
                    direction = -direction
            idx = 0
            for i in range(_key):
                for j in range(len(fence[i])):
                    fence[i][j] = _cipherText[idx]
                    idx += 1
            rail = 0
            direction = 1
            plainText = ''
            for _ in range(len(_cipherText)):
                plainText += fence[rail][0]
                del fence[rail][0]
                rail += direction
                if rail == _key - 1 or rail == 0:
                    direction = -direction
            return plainText

        
    class ColumnarTransposition: # ESSAM's Task
        # constructor
        def __init__(self):
            self._key = "" # Key
            self._plainText = "" # Plain text
            self._cipherText = "" # Cipher text
        
        # Static method to handle the key
        @staticmethod # Static method to handle the key 
        def _keyHandler(_key):
            _keyList = list(_key) # Convert the key to a list
            _handledKey = list(dict.fromkeys(_keyList)) # Remove the duplicates from the key
            if len(_keyList)==len(list(dict.fromkeys(_keyList))): # If the key is unique (Best case scenario)
                return _key
            else: # If the key is not unique (Worst case scenario)
                _upperCasesList = [chr(65 + i) for i in range(26)] # List of upper case alphabets
                _lowerCasesList = [chr(97 + i) for i in range(26)] # List of lower case alphabets
                _spchialCasesList=list("!@#($%<^&*()_+}{:?)>=-`~[]") # List of special characters

                _mixedCases=[] # Empty list of mixed cases
                for i, j, k in zip(_upperCasesList, _spchialCasesList, _lowerCasesList[::-1]): # Loop through the lists
                    if i not in _handledKey and not(len(_handledKey)+len(_mixedCases)>=len(_key)): 
                        _mixedCases.append(i) # Append the upper case character to the mixed cases list if it is not in the handled key and the length of the handled key '+' mixed cases is less than the length of the original key
                    if j not in _handledKey and not(len(_handledKey)+len(_mixedCases)>=len(_key)):
                        _mixedCases.append(j) # Append the special character to the mixed cases list if it is not in the handled key and the length of the handled key '+' mixed cases is less than the length of the original key
                    if k not in _handledKey and not(len(_handledKey)+len(_mixedCases)>=len(_key)):
                        _mixedCases.append(k) # Append the lower case character to the mixed cases list if it is not in the handled key and the length of the handled key '+' mixed cases is less than the length of the original key
                    if len(_handledKey)+len(_mixedCases)>=len(_key): # If the length of the handled key '+' mixed cases is greater than or equal to the length of the original key
                        break # Break the loop
                    
                # Loop through the mixed cases to add fill missing characters in the handled key
                for i in _mixedCases: 
                    if i not in _handledKey:
                        _handledKey.append(i)
                        if len(_handledKey) == len(_key):
                            break    
                        
                return "".join([i for i in _handledKey]) # Return the handled key
        @staticmethod # Static method to encrypt the plain text using the key
        def _encryption(_plainText, _key):

            _key=Cipher.ColumnarTransposition._keyHandler(_key) # Handle the key 

            _noOfColumns = len(_key) # calculate column of the matrix

            # we will use ceil function to calculate the number of rows 
            # for example if the length of the plain text is 10 and the key is 3 
            # the number of rows will be 4 cile(10/3) = ciel(3.333) = 4
            _noOfRows = int(_roundUp(len(_plainText) / _noOfColumns)) # calculate maximum row of the matrix

            _plainTextList=list(_plainText) # Convert the plain text to a list
            _sortedKeyList=sorted(list(_key)) # Sort the key
            # add the padding character '_' in empty
            # the empty cell of the matix 
            _numberOfNulls= int((_noOfRows * _noOfColumns) - len(_plainText)) # Calculate the number of nulls
            _plainTextList.extend('_'*_numberOfNulls) # Extend the plain text list with the nulls
            # create Matrix and insert _plainText and 
            # padding characters row-wise
            matrix = [_plainTextList[i: i + _noOfColumns] for i in range(0, len(_plainTextList), _noOfColumns)] # Create the matrix

            _cipherText = "" # Text after encryption
            _keyIndex = 0 # Track key indices 
            # read matrix column-wise using key
            for _ in range(_noOfColumns): # Loop through the columns
                _currentIndex = _key.index(_sortedKeyList[_keyIndex]) # Get the current index of the key character in the sorted key list
                _cipherText += ''.join([row[_currentIndex] for row in matrix]) # Join the characters in the matrix column-wise using the key
                _keyIndex += 1 # Increment the key index
            return _cipherText # Return the cipher text
        @staticmethod # Static method to decrypt the cipher text using the key 
        def _decryption(_cipherText, _key):

            _key=Cipher.ColumnarTransposition._keyHandler(_key) # Handle the key
            # calculate column of the matrix
            _noOfColumns = len(_key) # calculate column of the matrix
            # calculate maximum row of the matrix
            _noOfRows = int(_roundUp(len(_cipherText) / _noOfColumns)) # calculate maximum row of the matrix
            _sortedKeyList = sorted(list(_key)) # Sort the key
            # Create a null matrix to store the decrypted cipher
            dec_cipher = [] #  empty list
            for _ in range(_noOfRows): # Loop through the rows
                dec_cipher += [[None] * _noOfColumns] # Append the nulls to the matrix

            # Arrange the matrix column wise according 
            # to permutation order by adding into new matrix
            _keyIndex=0 # Track key indices
            _cipherTextIndex = 0 # track cipher text indices
            for _ in range(_noOfColumns): # Loop through the columns
                _currentIndex = _key.index(_sortedKeyList[_keyIndex]) # Get the current index of the key character in the sorted key list

                for j in range(_noOfRows): # Loop through the rows
                    dec_cipher[j][_currentIndex] = _cipherText[_cipherTextIndex] # Add the characters to the matrix
                    _cipherTextIndex += 1 # Increment the cipher text index
                _keyIndex += 1 # Increment the key index

            # convert decrypted msg matrix into a string
            _plainText="" # Text empty Text to store the decrypted _plainText
            _plainText = ''.join(sum(dec_cipher, [])) # Join the characters in the matrix


            null_count = _plainText.count('_') # Count the nulls

            if null_count > 0: # If there are nulls
                return _plainText[: -null_count] # Return the plain text without the nulls (Worst case scenario)
            return _plainText # Return the plain text (Best case scenario)
    
    class doubleColumnarTransposition:
        def __init__(self):
            self._key = "" # Key
            self._plainText = ""
            self._cipherText = ""
        
        @staticmethod
        def _keyHandler(_key):
            pass
        
        @staticmethod
        def _encryption(_plainText, _key):
            pass
        
        @staticmethod
        def _decryption(_cipherText, _key):
            pass
        