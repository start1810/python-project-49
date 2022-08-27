import random


def input_data():
    gcd = random.randint(1,50)
    simple_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    first_number = gcd * simple_numbers.pop(random.randint(0, len(simple_numbers)-1))\
                       * simple_numbers.pop(random.randint(0, len(simple_numbers)-1))
    second_number = gcd * simple_numbers.pop(random.randint(0, len(simple_numbers)-1))
    data = {'first_number': first_number,\
            'second_number': second_number,\
            'gcd': gcd}
    return data


def ask_question(data):
    start_text = f"\
Find the greatest common divisor of given numbers.\n\
Question: {data['first_number']}  {data['second_number']}\n"
    return start_text


def get_answer():
    answer = int(input())
    return answer

def counting_answer(data):
    return data['gcd']


def check_answer(correct_answer, answer):
    if correct_answer == answer:
        print()
        return True
    else:
        return False


def game():
    data = input_data()
    print(ask_question(data))
    answer = get_answer()
    correct_answer = counting_answer(data)
    result = check_answer(correct_answer, answer)
    win_text = 'Correct!'
    lose_text = f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
    if result == True:
        print(win_text)
    else:
        print(lose_text)
    return result


