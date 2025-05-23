import random

correct_answers = 0
errors = 0

while errors < 3:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    expression = f"{num1} + {num2} = "
    user_answer = input(expression)

    correct_result = num1 + num2

    try:
        answer = int(user_answer)

        if answer == correct_result:
            print("Правильно!\n")
            correct_answers += 1
        else:
            print("Ответ неверный.\n")
            errors += 1

    except ValueError:
        print("Нужно ввести число!\n")
        errors += 1

print(f"Игра окончена. Правильных ответов: {correct_answers}")
