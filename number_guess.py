# Number Guessing Game
import random

def number_10():
    number = random.randint(1,10)
    return int(number)
def number_50():
    number = random.randint(1,50)
    return int(number)
def number_100():
    number = random.randint(1,100)
    return int(number)


if __name__ == '__main__':
    print('NUMBER GUESSING GAME')
    print('''
    1) Guess a number between 1 and 10.
    2) Guess a number between 1 and 50.
    3) Guess a number between 1 and 100.
''')
    i = int(input('Enter your choice: '))
    if i == 1:
        user = input('chose a number between 1 and 10 > ')
        if int(user) == int(number_10()):
            print('Congrats! You got it!')
        elif int(user) >= int(number_10()):
            print('Too high!')
        elif int(user) <= int(number_10()):
            print('Too low!')
        else:
            print('Wrong input!')
    elif i == 2:
        user = input('chose a number between 1 and 50 > ')
        if int(user) == int(number_50()):
            print('Congrats! You got it!')
        elif int(user) >= int(number_50()):
            print('Too high!')
        elif int(user) <= int(number_50()):
            print('Too low!')
        else:
            print('Wrong input!')
    elif i == 3:
        user = int(input('chose a number between 1 and 100 > '))
        if int(user) == int(number_100()):
            print('Congrats! You got it!')
        elif int(user) >= int(number_100()):
            print('Too high!')
        elif int(user) <= int(number_100()):
            print('Too low!')
        else:
            print('Wrong input!')
    else:
        print('choose form menu...')







