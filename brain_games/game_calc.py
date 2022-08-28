import random


def input_data():
    data = {'first_number': random.randint(1, 100),
            'second_number': random.randint(1, 100),
            'operation': random.choice(['*', '+'])}
    return data


def ask_question(data):
    start_text = f"\
What is the result of the expression?\n\
Question: {data['first_number']} {data['operation']} {data['second_number']}\n"
    return start_text


def get_answer():
    answer = int(input())
    return answer


def counting_answer(data):
    if data['operation'] == '*':
        correct_answer = data['first_number'] * data['second_number']
    elif data['operation'] == '+':
        correct_answer = data['first_number'] + data['second_number']
    return correct_answer


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
    lose_text = f"\
'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
    if result is True:
        print(win_text)
    else:
        print(lose_text)
    return result
