import random
import time

def get_user_choice() -> str:
    """
    get choice from user until got a valid choice
    :return:  str - 'rock', 'paper', 'scissors'
    """
    user_choice = input('pick your choice: ')
    if user_choice == '1':
        user_choice = 'rock'
    elif user_choice == '2':
        user_choice = 'paper'
    else:
        user_choice = 'scissors'
    return user_choice


def get_random_computer_choice() -> str:
    """
    random 1 options from 'rock', 'paper', 'scissors'
    :return:  str - 'rock', 'paper', 'scissors'
    """
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    return computer_choice

def print_user_choice_icon_and_delay(choice, how_long_sleep) -> None:
    """
    print the user choice + icon and sleep 2-3
    :param choice:  str - 'rock', 'paper', 'scissors'
    :param how_long_sleep:  how long sleep in seconds
    :return: None
    """
    print ('*' * 40)
    time.sleep(how_long_sleep)
    print (f'your choice is: {choice}')


def print_computer_choice_icon(computer_choice) -> None:
    """
    print computer choice + icon
    :param choice:  str - 'rock', 'paper', 'scissors'
    :return:
    """
    print ('*' * 40)
    print(f'the computer choice is: {computer_choice}')


def get_game_result(user_choice, computer_choice) -> str:
    """
    :param user_choice:  str - 'rock', 'paper', 'scissors'
    :param computer_choice: str - 'rock', 'paper', 'scissors'
    :return: str winner - 'user', 'draw', 'computer'
    """
    if user_choice == computer_choice:
        return 'Draw!'

    elif user_choice == 'paper' and computer_choice == 'rock':
        return 'User wins!'

    elif user_choice == 'scissors' and computer_choice == 'paper':
        return 'User wins!'

    elif user_choice == 'rock' and computer_choice == 'scissors':
        return 'User wins!'

    else:
        return 'Computer Wins!'



def print_result_and_icon(get_result) -> None:
    """
    👋 💥🤝✅
    Print result with icon
    :param get_result: str winner - 'user', 'draw', 'computer'
    :return: None
    """
    if get_result.upper() == 'User Wins!'.upper():
        print ('User wins!💥')
    elif get_result.upper() == 'Computer Wins!'.upper():
        print ('Computer Wins!✅')
    else:
        print ('Draw!🤝')

# Icons for each choice
ICONS = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️",
}

print("🎮 Rock–Paper–Scissors")
print('1 for 🪨', '\n' '2 for 📄', '\n''3 for ✂️')

user_choice = get_user_choice()
print_user_choice_icon_and_delay(user_choice, 2)
computer_choice = get_random_computer_choice()
print_computer_choice_icon(computer_choice)
get_result = get_game_result(user_choice, computer_choice)
print_result_and_icon(get_result)