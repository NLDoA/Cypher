shift = range(26)

def user_info():
    info = input("Press 'e' to encrypt or 'd' to decrypt: ").lower()
    if info in ('e', 'd'):
        return info

def user_message():
    code = input("What is your message?: ")
    return code

def user_shift():
    while True:
        shift = int(input("What is your shift number?: "))
        if shift == int(shift):
            return shift

def codemessage(shift, message):
    length = len(message)
    length = length - 1
    
    for letter in message:
        newmessage =  chr(ord(message)+ shift)

    return newmessage

#MAIN PROGRAM
choice = user_info()
message = user_message()
shifting = user_shift()
print (shifting);
encrypt = codemessage(shifting, message)
print (encrypt);