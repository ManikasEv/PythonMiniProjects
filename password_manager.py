from cryptography.fernet import Fernet


master_pwd = input("What is the master password? ")
def load_key():
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    return key

key = load_key() 
fer = Fernet(key) 

''' generate key for the passwords
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

write_key()'''


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:",user,",","Password:",
                  fer.decrypt(passw.encode()).decode(),"\n")

def add():
    name = input('Account Name: ')
    pwd = input('Password ') 

    #with the with keyword we dont have to close the file
    #w is write
    #r is read
    #a is add something to existing file or create the file and add it

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input(
        "Would you like to add a new password or view existing ones? (view/add or q to quit)").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode.")
        continue