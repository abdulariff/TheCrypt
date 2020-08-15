from cipherswithnum import transpose_scramble, transpose_unscramble, df_scramble, df_unscramble

def encrypt_file(file,cipher):
    # Opening file and saving contents
    with open(file) as f:
        #cont = f.readlines() # Will give us a list
        cont = f.read() # Will give us a string
        #str_cont = ''.join(cont) # Use if you go with cont = f.readlines()
    # Transpose it first
    stage1 = transpose_scramble(cont)
    # DF it next
    final = df_scramble(stage1)

    with open(cipher,'w') as f:
        f.write(final)

def decrypt_file(cipher,decrypted):
    # Opening file and saving contents
    with open(cipher) as f:
        cont = f.read() # Will give us a string

    # Transpose it first
    stage1 = transpose_unscramble(cont)
    # DF it next
    final = df_unscramble(stage1)

    with open(decrypted,'w') as f:
        f.write(final)


#encrypt_file(r'C:\Users\abdul\Desktop\a2.txt',r'C:\Users\abdul\Desktop\a2_enc.txt') # Put in the path to the file you want encrypted
#decrypt_file(r'C:\Users\abdul\Desktop\a2_dec.txt',r'C:\Users\abdul\Desktop\a3_dec.txt') # Put in the location you want for the decrypted file