secret = 'zainab'
turns = len(secret)
guesses = ''
intro = "Let's play Guess the Word\nYou have " + str(
    turns) + " turns to guess the word!\n"
print(intro, '_ ' * len(secret))


def ifWon(missed):
    global preMiss
    if missed != preMiss:
        preMiss = missed
    else:
        return True


missed = 0
preMiss = missed

while turns > 0:
    guess = input('\nGuess a letter: ').lower()
    #reduce turns on wrong guess
    if guess not in secret:
        turns -= 1
    guesses += guess
    for letter in secret:
        if letter in guesses:
            print(letter, '', end='')
        else:
            print('_ ', end='')
            missed += 1
    #check if secret is already guessed
    if ifWon(missed):
        print('\nCongratulations! YOU WON !!!')
        break
    print('\nYou have only', turns, 'turns left')
print('\nEnd of Game')

#check out the live preview of this game on https://replit.com/@Zainab-Fahim/HangMan?v=1
