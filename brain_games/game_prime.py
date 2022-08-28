import random


def input_data():
    checking_number = random.randint(1,1000)
    data = checking_number
    return data


def ask_question(data):
    start_text = f'\
Answer "yes" if given number is prime. Otherwise answer "no".\n\
Question: {data}\n'
    return start_text


def get_answer():
    answer = input()
    return answer

def counting_answer(data):
    prime_digits = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, \
                    53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, \
                    109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, \
                    173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, \
                    233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, \
                    293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, \
                    367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, \
                    433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, \
                    499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, \
                    577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, \
                    643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, \
                    719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, \
                    797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, \
                    863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, \
                    947, 953, 967, 971, 977, 983, 991, 997}
    len_prime_digits = len(prime_digits)
    prime_digits.add(data)
    if len_prime_digits == len(prime_digits):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
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
    lose_text = f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
    if result == True:
        print(win_text)
    else:
        print(lose_text)
    return result