def login(name, password):
    success = False
    file = open('user_details.txt','r')
    for i in file:
        a, b = i.split(',')
        b = b.strip()
        if(a==name and b==password):
            success = True
            break
    file.close()
    if(success):
        print('Login Successfull!')
    else:
        print('wrong username or password')

def register(name, password):
     file = open('user_details.txt','a')
     file.write(name+','+password)
     file.close()

def access(option):
    if (option == 'login'):
        name = input('Enter your username or email: ')
        password = input('Enter your password: ')
        login(name, password)
    else:
        print('Enter your information to register')
        name = input('Enter your username or email: ')
        password = input('Enter your password: ')
        register(name, password)


def begin():
    global option
    option = input('Login or Register (login,reg):')
    if (option != "login" and option != "reg"):
        begin()
begin()
access(option)
