import random

playing = True

choices = ('H','T')
heads_count = 0
tails_count = 0
total_flips = 0

def flip():
    while True:
        player_choice = input("Choose Heads or Tails by entering 'H' or 'T': ")
        toss = random.choice(choices)
        heads_count = 0
        tails_count = 0
        total_flips = 0
        print('Flipping...')
        print(f'\nThe flip is a: {toss}')

        if player_choice[0].upper() == 'H' and toss == 'H':
            heads_count += 1
            total_flips += 1
            print('You won!')
            break
        elif player_choice[0].upper() == 'T' and toss == 'T':
            tails_count += 1
            total_flips += 1
            print('You won!')
            break
        elif player_choice[0].upper() == 'H' and toss == 'T':
            total_flips += 1
            print('You lost!')
            break
        elif player_choice[0].upper() == 'T' and toss == 'H':
            total_flips += 1
            print('You lost!')
            break
        else:
            print('Invalid input. Please try again.')
            continue
        break

while playing:
    print('Welcome to Coin Flip!')
    flip()

    print(f"Correct heads guesses: {heads_count}")
    print(f"Correct tails guesses: {tails_count}")
    print(f"Total flips: {total_flips}")

    new_game = input("Would you like to play again? Enter 'Y' or 'N': ")

    if new_game[0].upper() == 'Y':
        playing = True
        continue
    else:
        print('Thanks for playing!')
        break