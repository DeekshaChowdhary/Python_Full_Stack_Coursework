# ---------------------- PASSWORD VALIDATION ----------------------

password = input("Enter the password: ")

check = set()

if len(password) >= 8:

    for i in password:
        if i.islower():
            check.add('l')   # lowercase
        elif i.isupper():
            check.add('u')   # uppercase

        elif i.isdigit():
            check.add('n')   # number

        else:
            check.add('s')   # special character

    if len(check) == 4:
        print("Strong Password")
    else:
        print("Weak Password")

else:
    print("Weak Password")
