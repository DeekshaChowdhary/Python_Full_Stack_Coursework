# ---------------------- STUDENT RESULT SYSTEM ----------------------

data = {
    'a': {'status': True,  'python': 99, 'mysql': 90, 'django': 97},
    'b': {'status': True,  'python': 90, 'mysql': 70, 'django': 87},
    'c': {'status': True,  'python': 94, 'mysql': 78, 'django': 77},
    'd': {'status': True,  'python': 87, 'mysql': 87, 'django': 45},
    'e': {'status': True,  'python': 34, 'mysql': 41, 'django': 39},
    'f': {'status': False, 'python': None, 'mysql': None, 'django': None},
}

name = input("Enter the student name: ")

if name in data:

    student = data[name]

    if student['status']:

        total = student['python'] + student['mysql'] + student['django']
        avg = total / 3

        if avg >= 90:
            print(f"Congrats {name}, You got First Class")

        elif avg >= 75:
            print(f"Good {name}, Wish you all the best, better luck next time")

        elif avg >= 50:
            print(f"{name}, Need improvement")

        elif avg >= 35:
            print(f"{name},Work hard next time ")

        else:
            print(f"{name}, You have failed, bring your parents")

    else:
        print(f"{name}, You did not attend exam, please bring your parents")

else:
    print(f"{name} data is  not found")
