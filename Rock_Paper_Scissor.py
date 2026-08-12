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
    # Get the index of user input and computer pick from the options list
    user_input_index    = options.index(user_input)
    computer_pick_index = options.index(computer_pick)

    # Use modulus operator to determine the winner 
    if user_input_index == computer_pick_index:
        print("This is Tie!")
    elif (user_input_index - computer_pick_index) % 3 == 1:
        user_wins += 1
        print('You Win!')
    else:
        computer_wins += 1
        print('You Lose!')
print('================================================================')
print(f'You win {user_wins} times.\nComputer win {computer_wins} times.')
print('GoodBye!')
print('================================================================')
