
import time

def message():
    msg= input('enter a message : ')
    alphabet= 'abcdefghijklmnopqrstuvwxyz'
    key= 3
    encrypt=' '
    decrypt=' '
    for char in msg:
            position= alphabet.find(char)
            position_1= (position+ 3)%26
            encrypt +=alphabet[position_1]

    print(encrypt)
    print("Would you like to decrypt the encrypted message\n press enter to decrypt, press quit to exit")

    time.sleep(2)
    choice = input(">. ")

    if choice == 'enter':
            
        for char in encrypt:
            positon= alphabet.find(char)
            positon_1= (positon- 3 )%26
            decrypt +=alphabet[positon_1]
        time.sleep(5)
        print(msg)
    elif choice == "quit":
         print("THANKS FOR QUITTING👏")
    else :
         print("Kindly go through the instruction \r")
    # print(msg)

if __name__ =='__main__':
    message() 
