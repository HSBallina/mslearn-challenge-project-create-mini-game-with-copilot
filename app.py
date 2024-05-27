import random
import time

score = {'user': 0, 'computer': 0}
winning_combinations = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]
number_of_rounds = 0

def rock_paper_scissors():
    global number_of_rounds
    # rest of your code
    number_of_rounds += 1
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = input('Enter your choice (rock, paper, scissors): ')
    while user_choice not in choices:
        print('Invalid choice. Please try again.')
        user_choice = input('Enter your choice (rock, paper, scissors): ')
    print('Your choice:', user_choice)
    print('Computer choice:', computer_choice)
    time.sleep(1)
    if user_choice == computer_choice:
        print('Draw!')
    elif (user_choice, computer_choice) in winning_combinations:
        print('You win!')
        score['user'] += 1
    else:
        print('I win!')
        score['computer'] += 1
    print('Score:', score['user'], '-', score['computer'])

rock_paper_scissors()

while True:
    play_again = input('Do you want to play again? (yes/no): ')
    if play_again == '[y]es' or play_again == 'y' or play_again == '':
        rock_paper_scissors()
    else:
        print('Number of rounds:', number_of_rounds)
        print('Final score:', score['user'], '-', score['computer'])
        break

