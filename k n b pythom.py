import random
while True: # обратите внимание на эту строку кода
    user_action = input("Сделайте выбор — камень, ножницы или бумага: ")
    possible_actions = ["камень", "бумага", "ножницы"]
    computer_action = random.choice(possible_actions)
    print(f"\nВы выбрали {user_action}, компьютер выбрал {computer_action}.\n")
    if user_action == computer_action:
        print(f"Оба пользователя выбрали {user_action}. Ничья!!")
    elif user_action == "камень":
        if computer_action == "ножницы":
            print("Камень бьет ножницы! Вы победили!")
        else:
            print("Бумага оборачивает камень! Вы проиграли.")
    elif user_action == "бумага":
        if computer_action == "камень":
            print("Бумага оборачивает камень! Вы победили!")
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
    elif user_action == "ножницы":
        if computer_action == "бумага":
            print("Ножницы режут бумагу! Вы победили!")
        else:
            print("Камень бьет ножницы! Вы проиграли.")
# а также обратите внимание на код ниже
    play_again = "" 
    play_again = input("Сыграем еще? (д/н): ") 
    if play_again.lower() != "д": 
        break 
