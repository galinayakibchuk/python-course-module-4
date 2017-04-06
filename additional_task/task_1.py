# import random
# computer_number = random.randint(1, 10)
# user_number = int(input('Please, enter the guess number:'))
# while user_number != computer_number:
#     if user_number < computer_number:
#         print('a computer number greater')
#     elif user_number > computer_number:
#         print('a computer number less')
#     user_number = int(input('Please, enter the guess number:'))
# print('you are right!')

start = 1
finish = 10
guess = (start + finish)//2
print('My version', guess)
user = input('Ok, Less, Greater?')
while user != 'Ok':
    if user == 'Less':
        finish == guess
    else:
        start == guess
    guess = (start + finish) // 2
    print('My version', guess)
    user = input('Ok, Less, Greater?')

