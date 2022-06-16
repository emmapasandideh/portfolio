#emma
import random
import os
import hangman
#danica
schedule = """
+------------------------------+"
|                              |
|           schedule           |
|                              |
|  --------------------------  |
|  |  1  |     english      |  |
|  --------------------------  |
|  |  2  |       math       |  |
|  --------------------------  |
|  |  3  |     history      |  |
|  --------------------------  |
|  |  4  |    geography     |  |
|  --------------------------  |
|  |  5  | computer science |  |
|  --------------------------  |
|                              |
+------------------------------+"""
# emma
current_location = "foyer"
inventory = []
original_order = []
tries = 0
os.system("cls")
name = input("Please enter your name: ")
os.system("cls")
print(f"""Ms.Dharmai: \"Welcome, {name}, to St.Robert Catholic High School.
            Your mission is to impress all of your teachers so you can graduate.
            Now, dont be late, its almost 8:30. Here is your schedule.\"""")
print(schedule)
print()
input("press ENTER TO continue") 
print()
os.system("cls")
while True:
    if current_location == "foyer":
        os.system("cls")
        print("You are currently in the foyer.")
        print()
        print("Options:")
        print("- [G]raduate")
        print("- [E]xplore the first floor hallway")
        print()
        choice = input("Choice: ").lower()
        if choice == "g":
            os.system("cls")
            print("Ms.Dharmai: \"To graduate, pass all of your classes and decode the letters your teachers have bestowed upon you.\"")
            print()
            if inventory == []:
                print ("Your Letters: You have not received any letters. Try again later.")
            else:
                print("Your letters:")
                for letter in inventory:
                    text = f"""
                        +---+
                        | {letter} |
                        +---+"""
                    print(text, end="")
                    print()
            if "L" in inventory:
                print()
                if tries == 0:
                    for letter in inventory:
                        original_order += letter
                print("Reorder the following letters:")
                print()
                for i in range(len(inventory)):
                    print(f"Order: {i+1}, Original letter: {inventory[i]}")
                    letter = input("Reordered Letter: ").upper()
                    inventory[i] = letter
                    print()
                if inventory == ["L", "E", "A", "R", "N"]:
                    for letter in inventory:
                        text = f"""
                        +---+
                        | {letter} |
                        +---+"""
                        print(text, end="")
                    print()
                    print()
                    print(f"Ms.Dharmai: \"Congratulations, {name}, you have now graduated at St. Robert.\"")
                    print(f"Ms.Dharmai: \"I wish you success in all your future endeavours.\"")
                    print()
                    print("Mission Complete! We hope you enjoyed this journey with us. Goodbye!")
                    input("press ENTER to view game credits")
                    os.system("cls")
                    print("""
                    Emma: Base of the Game, Foyer, First Floor Hallway, English Class
                    Danica: Math Class, Computer Science Class, Schedule
                    Natalie: Second Floor Hallway, Geography Class, History Class, Art Class
                    """)
                    input("Press ENTER to exit the game")
                    os.system("cls")
                else:
                    print()
                    print("Sorry, that is not the correct word. Try again later.")
                    for i in range(len(original_order)):
                        inventory[i] = original_order[i]
                    tries += 1
                    input("press ENTER to continue")
            else:
                print()
                print(f"Ms.Dharmai: \"Not now {name}, you cannot graduate. Please do better in class.")
                print()
                input("press ENTER TO CONTINUE")      
        elif choice == "e":
            current_location = "first floor hallway"
        else:
            print("Please enter a valid letter option.")
            print()
            input("press ENTER TO CONTINUE")
            os.system("cls")
    if current_location == "first floor hallway":
        os.system("cls")
        print("You are standing in the first floor hallway. What do you want to do?")
        print()
        print("Options:")
        print("- [L]ook at your schedule.")
        print("- Go to the [F]ront Foyer.")
        print("- Go to [M]ath Class")
        print("- Go to [E]nglish Class.")
        print("- Go to [C]omputer Science Class.")
        print("- Go to the [S]econd Floor.")
        print()
        choice = input("Choice: ").lower()
        os.system("cls")
        if choice == "l":
            print(schedule)
            print()
            input("press ENTER TO CONTINUE")
        elif choice == "f":
            current_location = "foyer"
        elif choice == "m":
            current_location = "math class"
        elif choice == "e":
            current_location = "english class"
        elif choice == "c":
            current_location = "computer science"
        elif choice == "s":
            current_location = "second floor hallway"
        else: 
            print("Please enter a valid letter option.")
            print()
            input("press ENTER TO CONTINUE")
    if current_location == "english class":
        if "N" not in inventory:
            os.system("cls")
            print("You are sitting at a table in Ms.Kurtz's English classroom.") 
            print("What do you do next?:")
            print("Options:")
            print("- [S]croll around on Instagram.")
            print("- [C]hat with your classmates.")
            print("- [T]alk to Ms.Kurtz.")
            choice = input("Choice: ").lower()
            os.system("cls")
            if choice == "s":
                print("Bad Idea. Ms.Kurtz catches you on your phone and kicks you out into the hallway.")
                print()
                input("press ENTER TO CONTINUE")
                current_location = "first floor hallway"
            elif choice == "c":
                print("They ask you to skip class with them. Are you down for it?")
                print()
                choice = input("Choice (Y/N): ").lower()
                os.system("cls")
                if choice == "y":
                    result = random.randrange(4)
                    if result == 1:
                        print("Luckily, she didn't notice you were gone and rounded your grade up so you could pass!")
                        print("Here is a letter \"N\" for passing the course.")
                        inventory.append("N")
                        for i in range(len(inventory)):
                            text = f"""
                            +---+
                            | {inventory[i]} |
                            +---+"""
                            print(text, end="")
                        print()
                        print("Although, you better go to your next class to avoid any suspicion.")
                        print()
                        input("press ENTER TO CONTINUE")
                        current_location = "foyer"
                    else:
                        print("Ms. Kurtz sends your parents a very angry email about your absence.")
                        print("They track you down and send you back to school.")
                        print()
                        input("press ENTER TO CONTINUE")
                        current_location = "foyer"
                elif choice == "n":
                    print(f"Smart move, {name}. Attendance is very important.")
                    print()
                    input("press ENTER TO CONTINUE")
                else:
                    print("Please enter a valid letter option.")
                    print()
                    input("press ENTER TO CONTINUE")
            elif choice == "t":
                print(f"Ms.Kurtz:\"So you want to pass my class, {name}?\"")
                print(f"Ms.Kurtz:\"How about a good ol' game of hangman and then I'll decide.\"")
                print()
                choice = input("Choice (Y/N): ").lower()
                if choice == "n":
                    print("Ms.Kurtz: \"Suit yourself then...Now go and sit at your assigned seat!\"")
                    print()
                    input("press ENTER TO CONTINUE")
                elif choice == "y":
                    print()
                    print("Ms.Kurtz: \"Then here it is!\"")
                    print()
                    input("press ENTER TO CONTINUE")
                    win = hangman.run()
                    if win == True:
                        print("Here is a letter \"N\" which will be useful to you later.")
                        inventory.append("N")
                        for i in range(len(inventory)):
                            text = f"""
                            +---+
                            | {inventory[i]} |
                            +---+"""
                            print(text, end="")
                        print()
                        input("press ENTER TO CONTINUE")
                        current_location = "first floor hallway"
                    elif win == False:
                        print("Get out of my classroom!")
                        print()
                        input("press ENTER TO CONTINUE")
                        current_location = "first floor hallway"
                else:
                    print("Please enter a valid letter option.")
                    print()
                    input("press ENTER TO CONTINUE")
        elif "N" in inventory:
                print("Ms: Kurtz: \"What are you doing in my classroom again? Out!\"")
                print()
                input("press ENTER TO CONTINUE")
                current_location = "first floor hallway"
        else: 
            print("Please enter a valid letter option.")
            print()
            input("press ENTER TO CONTINUE") 
    #danica
    if current_location == "math class":
        os.system("cls")
        if 'N' not in inventory:
            print("You're not supposed to be here! Stick to your schedule please!")
            print()
            input("press ENTER to continue")
            current_location = "first floor hallway"
        elif 'A' in inventory:
            print('You have already passed this class.')
            print()
            input("press ENTER to continue")
            print()
            current_location = "first floor hallway"
        else:
            print("""you are now in the math classroom
            Ms.Giang: so you want to pass my class huh?
            Ms.Giang: answer this question and then i'll decide
            Ms.Giang: what is 5 x 8? """)
            math_question = input()
            while math_question != "40":
                os.system('cls')
                print('what is 5 x 8?')
                print('try again')
                math_question = input()
            if math_question == "40":
                os.system('cls')
                print("Ms.Giang: fine i will let you pass. be on your way.")
                inventory.append('A')
                print()
                input("press ENTER to continue")
                os.system('cls')
                print("you have obtained the letter 'A'. you will need this for later")
                print()
                input('press ENTER to return to the hallway')
                current_location = "first floor hallway"
    if current_location == "computer science":
        if 'R' not in inventory:
            print("You're not supposed to be here! Stick to your schedule please!")
            print()
            input("press ENTER to continue")
            current_location = "first floor hallway"
        elif 'L' in inventory:
            print('you have already passed this class')
            print()
            input("press ENTER to continue")
            current_location = "first floor hallway"
        else:
            print("""you are now in the computer science classroom
            teacher: to pass you must answer this question
            teacher: what symbol is used to find modulus in python?""")
            cs_question = input()
            while cs_question != "%":
                os.system('cls')
                print("what symbol is used to find modulus in python?")
                print('try again')
                cs_question = input()
            if cs_question == "%":
                os.system('cls')
                print("teacher: well i guess you do know your stuff. now get out of here")
                inventory.append('L')
                print()
                input("press ENTER to continue")
                os.system('cls')
                print("you have obtained the letter 'L'. you will need this for later")
                print()
                input("press ENTER to return to the hallway")
                current_location = "first floor hallway"
    # natalie
    while current_location == "second floor hallway":
        print("You are in the second floor hallway.")
        print("Pick an option:")
        print("[L]ook at your schedule.")
        print("Go to [G]eography Class")
        print("Go to [H]istory Class")
        print("Go to [A]rt Class")
        print("Go to the [F]irst Floor.")
        choice = input().lower()
        print()
        os.system("cls")
        if choice == "l":
            print(schedule)
            input("press ENTER to return to continue")
        if choice == "g":
            current_location = "geography class"
            print("You are now in Geography Class")
            if 'N' not in inventory:
                print("You're not supposed to be here! Stick to your schedule please!")
                print()
                input("press ENTER to continue")
                current_location = "second floor hallway"
            elif "R" in inventory:
                print("You already passed this class. Go back to the hallway")
                input("Press ENTER to continue:")
                current_location = "second floor hallway"
            else:
                print("You walk into the class room and Ms Mammoliti says:")
                print(" 'If you want to graduate, answer the question'")
                answer_1 = input("Question: Which country has a blue flag with a yellow cross?: ").lower()
               
                while answer_1 != 'sweden':
                    print("Wrong answer, please try again")
                    answer_1 = input("Question: Which country has a blue flag with a yellow cross?: ")
                if answer_1 == 'sweden':
                 os.system("cls")
                 print("Congratulations! You can move on to the next room")
                 inventory.append("R")
                 print("You have obtianed the letter 'R'. You will need this for later")
                 print(f"Here are your letters so far: {inventory})")
                 input("Press ENTER to continue:")
                 current_location = "second floor hallway"
        print()
        os.system("cls")
        if choice == "h":
            current_location = "history class"
            print("You are now in History Class")
            if 'A' not in inventory:
                print("You're not supposed to be here! Stick to your schedule please!")
                print()
                input("press ENTER to continue")
                current_location == "second floor hallway"
            elif "E" in inventory:
                print("You already passed this class, go back to hallway!")  
                input("Press ENTER to continue:")
                current_location = "second floor hallway"
            else:
                print("You walk in and you see the teacher teaching a lesson.")
                print("The teacher asks 'Why are you in my class, I dont apprciate being interrupted during my lesson.'")
                print("The teacher gives you two options:")
                print("Answer a question on [C]anadian history")
                print("Answer a question on [Am]merican history")
                choice = input().lower()
                os.system('cls')
 
                if choice == 'c':
                    print("The teacher reads out the question:")
                    print("What year was the Canadian flag made?")
                    print("Options:")
                    print("1955")
                    print("1965")
                    print("1970")
                    answer_2 = input("Enter answer here:")
                    while answer_2 != '1965':
                        print("Wrong answer, try again")
                        print("What year was the Canadian flag made?")
                        print("Options:")
                        print("1955")
                        print("1965")
                        print("1970")
                        answer_2 = input("Enter answer here:")
                    if answer_2 == '1965':
                        os.system("cls")
                        print("Congratulations")
                        inventory.append("E")
                        print("You have obtianed the letter 'E'. You will need this for later")
                        print(f"Here are your letters so far: {inventory})")
                        input("Press ENTER to continue:")
                        current_location = "second floor hallway"
                if choice =='am':
                    print("Teacher reads out a question:")
                    print("Who was the first president on Mount Rushmore?")
                    print("Theodore Rosevelt")
                    print("Thomas Jefferson")
                    print("George Washington")
                    print("Abraham Lincoln")
                    print("")
                    answer_3 = input("Write answer here:").lower()
                    while answer_3 != 'george washington':
                        print("Wrong Answer, Try again!")
                        answer_3 = input("Write answer here:").lower()
                    if answer_3 == 'george washington':
                        os.system("cls")
                        print("Congratulations, You know your American history.")
                        inventory.append("E")
                        print("You have obtianed the letter 'E'. You will need this for later")
                        print(f"Here are your letters so far: {inventory})")
                        input("Press ENTER to continue:")
                        current_location = "second floor hallway"      
        print()
        os.system("cls")
        if choice == "a":
            current_location = "Art Class"
            print("You are now in Art Class")
            print("Oh no! You are in wrong class")
            print("The teacher kicks you out")
            input("Press ENTER to continue")
            current_location = "second floor hallway"
        if choice == "f":
            current_location = "first floor hallway"
        print()
        os.system('cls')
