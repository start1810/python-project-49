import random
from .. import cli


def answer(number):
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer


def condition(checked_number):
    start_text = f'\
Answer "yes" if the number is even, otherwise answer "no".\n\
Question: {checked_number}\n\
Your answer: '
    user_answer = input(start_text)
    return user_answer


def game():
    checked_number = random.randint(0, 1000)
    user_answer = condition(checked_number)
    correct_answer = answer(checked_number)

    winner_text = 'Correct!'
    loser_text = f"\
'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."

    if user_answer == correct_answer:
        print(winner_text)
        return True
    else:
        print(loser_text)
        return False


def main():
    user_name = cli.welcome_user()
    game_points = 0
    game_status = True
    while game_status is True:
        game_status = game()
        game_points += 1
        if game_points == 3:
            print(f"Congratulations, {user_name}!")
            return
        print(f"Let's try again, {user_name}!")


if __name__ == "__main__":
    main()
