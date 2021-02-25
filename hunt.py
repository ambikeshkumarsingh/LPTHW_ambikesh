print("Before starting this game let's know you. What's your name sweetheart?")
name = input(">")
print(f"Hi {name},let's start the game. Cool !!!")
print("""Choose from the following options:-
      1. To kill a bear .
      2. To kill a lion.
      3. To kill a human.
      4. To kill a Zombie.""")

choice=input(">")
if choice=="1":
    choice= "Bear"
    print("""What is your level of experince in gaming?
    1. Newbie.
    2. Intermediate.
    3. Pro.
    4. Legend.
    5. Ultra Legend.""")

    level= input(">")
    if level == "1":
        level= Newbie
        print(f"Sorry {name} ,{level} level users can't kill bear. Go play more games sucker!!!")
    elif level =="2" :
        level= "Intermediate"
        print("""What kind of weapon do you have?
        1. Stick
        2. knife
        3. Gun
        4. Rocket Launcher""")
        weapon = input(">")
        if weapon == "1":
            weapon="Stick"
            print(f"""No {name}, Since you are {level} level gamer , you can't kill bear with {weapon}.
            Go ask some big weapon from your mom and say hi to her """)
        elif weapon =="2":
            weapon="knife"
            print(f"""Since you are {level} level gamer and you have only {weapon} as a weapon.
            We need to practice a little bit.
            1. for practice
            2. for continuing without practice""")
            practice=input(">")
            #print(" Test ")
            if practice == "1":
                print(f"Welcome in practice session of {choice} hunting")
                print(f""" Read the following Instructions and then choose the correct answer:-
                Step 1: if {choice} sees you first you have to run.
                Step 2: If you see {choice} first you have to keep wait for him to sleep. """
                )
                print(f" Now {name},answer the following question so that we know you are paying attention")
                print(f"""Question : let's say you don't see the {choice} at first .
                What do you do?
                1. Run
                2. Kill him
                3. Hide and Wait.""")
                response= input(">")
                if response == "3":
                    print(" You are doing good. To continuing the training press 1")
                    press= input (">")
                    if press == "1":
                        print(f"{name}, let's continue our training.")
                    else:
                        print(f"See you next time {name}")
                else:
                    print(f"{choice} killed you. You have to pay the attention a little bit bitch!!!")


            else:
                print(f"{name} !!! {choice} killed you. You know what I think you need to do practice")
