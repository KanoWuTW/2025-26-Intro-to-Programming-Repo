#asks user's name
name = input("What is your name?")

#asks user's age and if input is not an integer, user has to re-enter
while True:
    try:
        age = int(input("What is your age?"))
        break
    except ValueError:
        print("Please enter an integer!")

#asks user's student status. users can only say true, false, 1, 0, yes, or no; otherwise, re-enter
while True:
    try:
        is_Student = input("Are you a student?")
        if is_Student == "0" or is_Student.lower() == "false" or is_Student.lower() == "no":    #normalises is_Student
            is_Student = False
        elif is_Student == "1" or is_Student.lower() == "true" or is_Student.lower() == "yes":  #normalises is_Student
            is_Student = True
        else:
            # if user enters other answers, throw an exception
            raise ValueError("incorrect input")
        break
    except:
        print("You can only say true, false, 1, 0, yes, or no")

print(f"My name is {name}. I am {age} years old, and my student status is {is_Student}")