from string import ascii_uppercase
from string import ascii_lowercase
upper = ascii_uppercase
lower = ascii_lowercase
def inputshift():
    while True:
        shift = int(input('How much shift do you want?(1-25)'))
        if 1 <=shift <= 25:
            return shift
        else:
            print('That is not a valid amount of shift')
def inputmessage():
    message=input('Enter the message you would like to cipher:')
    return message
def encrypt(message,shift):
    crypted_message = []
    for letter in message:
        if letter.isupper() == True:
            crypted_message.append(upper[(upper.index(letter) +shift) % len(upper)])    
        elif letter.islower() == True:
            crypted_message.append(lower[(lower.index(letter) +shift) % len(lower)])
        else:
            crypted_message.append(letter)
    return crypted_message        
def main():
    message = inputmessage()
    shift = inputshift()
    encrypted_message = encrypt(message,shift)
    print(''.join(encrypted_message))
main()
