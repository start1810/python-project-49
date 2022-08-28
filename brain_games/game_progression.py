import random


def input_data():
    first_member = random.randint(1, 30)
    general_member = random.randint(1, 30)
    progression_length = random.randint(5, 15)
    arithmetic_progression = [first_member]
    progression_index = 1
    while progression_index < progression_length:
        progression_member = arithmetic_progression[progression_index - 1]\
                        + general_member
        arithmetic_progression.append(progression_member)
        progression_index += 1
    selected_index = random.randint(0, progression_length - 1)
    selected_member = arithmetic_progression[selected_index]
    arithmetic_progression[selected_index] = '..'
    data = {'progression': arithmetic_progression,
            'selected_member': selected_member}
    return data


def ask_question(data):
    progression_string = ''
    for elem in data['progression']:
        progression_string += str(elem) + ' '
    start_text = f"\
What number is missing in the progression?\n\
Question: {progression_string}\n"
    return start_text


def get_answer():
    answer = int(input())
    return answer


def counting_answer(data):
    correct_answer = data['selected_member']
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