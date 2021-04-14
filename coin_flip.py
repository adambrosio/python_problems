import random

playing = True

choices = ('H','T')
heads_count = 0
tails_count = 0
total_flips = 0

def flip():
    while playing:
        # heads_count = 0
        # tails_count = 0
        player_choice = input("Choose Heads or Tails by entering 'H' or 'T': ")

        if player_choice.upper() not in choices:
            print('Invalid input. Please try again.')
            continue

        toss = random.choice(choices)

        print('\nFlipping...')
        print(f'The flip is: {toss}')

        if player_choice[0].upper() == 'H' and toss == 'H':
            heads_count += 1
            print('\nYou won!')
            break
        elif player_choice[0].upper() == 'T' and toss == 'T':
            tails_count += 1
            print('\nYou won!')
            break
        elif player_choice[0].upper() == 'H' and toss == 'T':
            print('\nYou lost!')
            break
        elif player_choice[0].upper() == 'T' and toss == 'H':
            print('\nYou lost!')
            break
        else:
            print('\nInvalid input. Please try again.')
            continue

while playing:
    print('Welcome to Coin Flip!')
    flip()
    total_flips += 1

    print(f"\nCorrect heads guesses: {heads_count}")
    print(f"Correct tails guesses: {tails_count}")
    print(f"Total # of flips: {total_flips}")

    while True:
        new_game = input("\nWould you like to play again? Enter 'Y' or 'N': ")

        if new_game[0].upper() == 'Y':
            playing = True
        elif new_game[0].upper() == 'N':
            playing = False
            print('Thanks for playing!')
        else:
            print('Invalid input. Please try again.')
            continue
        break