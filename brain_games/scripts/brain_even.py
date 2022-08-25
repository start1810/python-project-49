import random
from .. import cli

def answer(number):
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer

def brain_even():
    checked_number = random.randint(0,1000)
    start_text =f'\
Answer "yes" if the number is even, otherwise answer "no".\n\
Question: {checked_number}\n\
Your answer: '
    user_answer = input(start_text)
    correct_answer = answer(checked_number)

    winner_text = 'Correct!'
    loser_text = f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."

    if user_answer == correct_answer:
        print(winner_text)
        return True
    else:
        print(loser_text)
        print("let's try again, ")
        return False


def main():
    user_name = cli.welcome_user()
    game_points = 0
    game_status = True
    while game_status == True:
        game_status = brain_even()
        game_points +=1
        if game_points == 3:
            print(f"Congratulations, {user_name}")
            break


if __name__ == "__main__":
    main()

    
    



    
    

