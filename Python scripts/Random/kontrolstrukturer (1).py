alias = None
enemy = None
greeting = None

user = input("What is your name, user? ")

if user == "Bruce Wayne":
    alias = "Batman"
    enemy = "The Joker"
    greeting = "You are the hero Gotham deserves, but not the one it needs right now."
elif user == "Peter Parker":
    alias = "Spiderman"
    enemy = "Doc. Octopus"
    greeting = "Just our freindly naborhood Spiderman"
elif user == "Katniss Everdeen":
    alias = "Mockingjay"
    enemy = "President Snow"
    greeting = "May the odds be ever in your favour!"
else:
    alias = "programmer"
    enemy = "the compiler"
    greeting = "You are the 1%."

print("Greetings {}. {} Good luck defeating {}.".format(alias, greeting, enemy))
