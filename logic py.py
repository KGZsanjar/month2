import random
def start_game(min_number, max_number, attempts, starting_capital):
    secret_number = random.randint(min_number, max_number)
    capital = starting_capital

    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"Попробуйте угадать число в диапазоне от {min_number} до {max_number}.")
    print(f"У вас есть {attempts} попыток, и ваш начальный капитал: {capital}.")

    for attempt in range(1, attempts + 1):
        print(f"\nПопытка {attempt} из {attempts}.")
        try:
            bet = int(input(f"Ваш текущий капитал: {capital}. Введите ставку: "))
            if bet > capital or bet <= 0:
                print(f"Ставка должна быть положительным числом и не превышать ваш капитал ({capital}).")
                continue
        except ValueError:
            print("Введите корректное число для ставки.")
            continue

        try:
            guess = int(input(f"Введите ваше число (от {min_number} до {max_number}): "))
            if guess < min_number or guess > max_number:
                print(f"Число должно быть в диапазоне от {min_number} до {max_number}.")
                continue
        except ValueError:
            print("Введите корректное число.")
            continue

        if guess == secret_number:
            capital += bet  # удваиваем ставку
            print(f"Поздравляем! Вы угадали число {secret_number}. Ваш капитал удвоен до {capital}.")
            break
        else:
            capital -= bet
            print(f"Вы не угадали. Ваше число: {guess}. Загаданное число больше." if guess < secret_number else "меньше.")

        if capital <= 0:
            print("К сожалению, вы потеряли весь свой капитал.")
            break

    else:
        print(f"Игра окончена. Вы не смогли угадать число. Загаданное число было {secret_number}. Ваш итоговый капитал: {capital}.")
