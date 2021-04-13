import random

playing = True

choices = ('H','T')
heads_count = 0
tails_count = 0

def flip():
    while True:
        player_choice = input("Choose Heads or Tails by entering 'H' or 'T': ")
        
        toss = random.choice(choices)

        if player_choice[0].upper() == 'H' and toss == 'H':
            heads_count += 1
            print('You won!')
        elif player_choice[0].upper() == 'T' and toss == 'T':
            tails_count += 1
            print('You won!')
        elif player_choice[0].upper() == 'H' and toss == 'T':
            print('You lost!')
        elif player_choice[0].upper() == 'T' and toss == 'H':
            print('You lost!')
        else:
            print('Invalid input. Please try again.')
            continue
        break

while playing:
    print('Welcome to Coin Flip!')
