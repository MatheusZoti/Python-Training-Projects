from time import sleep

def start_game():
    print('Welcome to my Yorick mid-lane guide!!!')
    sleep(2)
    print('First things first... You need to understand that')
    sleep(1)
    print('.\n.\n.\n')
    sleep(1)
    print('Yorick smash...!')
    sleep(3)
    print("Ok... What is the first item you buy?")
    print("1: Corrupted Potion;")
    print("2: Long Sword;")
    print("3: Doran's Shield;")
  
    player_response = input("Answer with 1, 2 or 3.")

    if player_response == "1":
        print('Good choice, this will help you a lot if you use it wisely.')
        sleep(2)
        restart_game()
    elif player_response == "2":
        print('Only buy it if you know you can win early.')
        sleep(2)
        restart_game()
    elif player_response == "3":
        print('You lost the game')
        sleep(1)
        print('Game will start again.........')
        sleep(2)
        start_game()
    else:
        print('Invalid choice.')
        sleep(1)
        print('Game will start again.........')
        sleep(2)
        start_game()

def restart_game():
    player_response = input("Wanna play again? (y/n)")

    if player_response.lower() == "y":
        start_game()
    elif player_response.lower() == "n":
        exit()
    else:
        print("Invalid Answer. Please enter 'y' or 'n'.")
        sleep(1)
        restart_game()

start_game()