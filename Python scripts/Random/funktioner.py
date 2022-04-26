alias = None
enemy = None
greeting = None

def getInput():
    user = input("What is your name, user? ")
    if user == "" or user == None:
        user = getInput()
    return user

def setUserVars(anAlias, anEnemy, aGreeting):
    global alias, enemy, greeting
    alias = anAlias
    enemy = anEnemy
    greeting = aGreeting

def greetUser():
    return "Greetings {}. {}. Good luck defeating {}!".format(alias, greeting, enemy)

if __name__ == '__main__':
    user = getInput()

    if user == "Oliver Lehman":
        setUserVars("GhostWriter", "The Goverment", "Welcome brother, to the inner circle")
    elif user == "Katniss Everdeen":
        setUserVars("Mockingjay", "President Snow", "May the odds be ever in your favour")
    else:
        setUserVars("Programmer", "The Compiler", "You are the 5%")

    print(greetUser())
