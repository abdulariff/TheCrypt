# Scrambling for Transposition cipher
""" Scramble function for transposition cipher """
def transpose_scramble(plaintext):
    even = [plaintext[i] for i in range(len(plaintext)) if i%2==0]
    odd = [plaintext[i] for i in range(len(plaintext)) if i%2!=0]
    ciphertext = ''.join(odd) + ''.join(even)
    return ciphertext

# Unscrambling it
""" Unscramble method for transposition cipher """
def transpose_unscramble(ciphertext):
    mid = len(ciphertext)//2
    odd = ciphertext[:mid]
    even = ciphertext[mid:]
    
    plaintext = ''
    for i in range(len(odd)):
        plaintext+=even[i] + odd[i]
    if len(odd) < len(even):
        plaintext+=even[-1]
        
    return plaintext

# Implementing substitution cipher in Digital Fortress 
def df_scramble(message,step=2615):
    alphaNum = 'abcdefghijklmnopqrstuvwxyz1234567890'
    len_a = len(alphaNum)
    step = step%len_a # Allows us to restart alphabet again
    message = message.lower()
    ciphertext = ''
    for char in message:
        if char not in alphaNum: # If it's not a letter in the alphabet, maintain it
            ciphertext+=char
        else:
            pos = alphaNum.index(char)
            next = pos + step # Index of what's coming to replace
            next =  next%len_a
            ciphertext+=alphaNum[next]
    return ciphertext.upper()

# Implementing the decryption algorithm
def df_unscramble(ciphertext,scramble_step=2615):
    unscramble_step = -1*scramble_step
    plaintext = df_scramble(ciphertext,unscramble_step)
    return plaintext.upper()


