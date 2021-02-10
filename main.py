from random import randint

number = randint(1, 10 )
# hack patch =print(number)
while True:
    try:
        guess=int(input("what is the number:"))
        if 0<guess<10:
            if guess == number:
                print(number)
                print("born to be a genius!")
                break
        else:
            print("hey bozo i said number between 1 to 10")
            continue
    except ValueError:
        print("enter a valid number!")
        continue
# this game is about if the number = input then it will say you are the genius and will end the game.
