import random
user_wins = 0 
computer_wins = 0
options = ['rock','paper','scissor']
while True:
    user_input = input("Type Rock / Paper / Scissor or Q to Quit the game: ").lower()
    if user_input == 'q':
        break
    elif user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print(f"computer picked {computer_pick}.")
    # Determine the winner
    if user_input == 'rock' and computer_pick == 'scissor':
        print("You won!")
        user_wins += 1
    elif user_input == 'paper' and computer_pick == 'rock':
        print("You won!")
        user_wins += 1
    elif user_input == 'scissor' and computer_pick == 'paper':
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("It's a tie!")
    else:
        print("You lost!")
        computer_wins += 1

print('================================================================')
print(f'You win {user_wins} times.\nComputer win {computer_wins} times.')
print('GoodBye!')
print('================================================================')
