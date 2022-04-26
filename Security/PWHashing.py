import bcrypt

password = input("Please enter your password: ").encode("utf-8")

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(hashed)

if bcrypt.checkpw(password, hashed):
    print('It Matches!')
else:
    print("Doesn't Match!")
