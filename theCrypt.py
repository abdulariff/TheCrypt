from tkinter import *
from scramble_text import encrypt_file,decrypt_file
base = Tk()
base.title('The Crypt')
base.geometry('500x300')
base['background'] = '#26718F'


def encrypt():
    # Creating the window
    enc = Toplevel()
    enc.title('Encrypt')
    enc.geometry('500x250')

    # Entry for path of plaintext file
    Label(enc,text='Please input the path of the file you want to encrypt').pack()
    file = Entry(enc,width=80)
    file.pack()

    # Entry for path of new ciphertext file
    Label(enc,text='Please input the path where you want to store the cipher').pack()
    encrypted = Entry(enc,width=80)
    encrypted.pack()

    # Encrypt file after pressing Encrypt button
    Button(enc,text= 'Encrypt',command=lambda:encrypt_file(file.get(),encrypted.get())).pack()



def decrypt():
    # Creating the window
    dec = Toplevel()
    dec.title('Decrypt')
    dec.geometry('500x250')

    # Entry for path of ciphertext file
    Label(dec,text='Please input the path of the file you want to decrypt').pack()
    cipher = Entry(dec,width=80)
    cipher.pack()

    # Entry for path of new decrypted file
    Label(dec,text='Please input the path of the file you want to decrypt').pack()
    decrypted = Entry(dec,width=80)
    decrypted.pack()

    # Decrypt file after pressing Decrypt button
    Button(dec,text='Decrypt',command=lambda:decrypt_file(cipher.get(),decrypted.get())).pack()


Label(base,text='Welcome to The Crypt').grid(row=0,column=7)
Button(base,text='Encrypt a text file',width=15,height=10,command= lambda:encrypt()).grid(row=9,column=6,padx=20,pady=20)
Button(base,text='Decrypt a text file',width=15,height=10,command=lambda:decrypt()).grid(row=9,column=11,padx=20,pady=20)
base.mainloop()
