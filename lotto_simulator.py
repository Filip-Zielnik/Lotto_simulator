from random import shuffle


def user_numbers():
    """
    User chooses six numbers from 1 to 49.
    :return: Sorted user chosen numbers
    """
    user_list = []
    while len(user_list) < 6:
        try:
            user_number = int(input("Select number: "))
            if user_number not in user_list and user_number in range(1, 49):
                user_list.append(user_number)
            else:
                print("Incorrect number!")
        except ValueError:
            print("It's not a number!")
    return sorted(user_list)


def computer_numbers():
    """
    Computer chooses six random numbers from 1 to 49.
    :return: Sorted numbers choosen by computer
    """
    computer_list = list(range(1, 50))
    shuffle(computer_list)
    return sorted(computer_list[:6])


def lotto():
    """
    Compares how many user's numbers matches with computer's numbers.
    :return: Number of hit numbers
    """
    set_1 = user_numbers()
    print("Your numbers:")
    print(*set_1, sep=", ")
    set_2 = computer_numbers()
    print("Lotto numbers:")
    print(*set_2, sep=", ")
    hit = 0
    for i in set_1:
        if i in set_2:
            hit += 1
    if hit == 6:
        result = f"Congratulation You hit {hit} numbers!"
    elif hit == 5:
        result = f"Congratulation You hit {hit} numbers!"
    elif hit == 4:
        result = f"Congratulation You hit {hit} numbers!"
    elif hit == 3:
        result = f"Congratulation You hit {hit} numbers!"
    elif hit == 2:
        result = f"Unfortunately You hit only {hit} numbers."
    elif hit == 1:
        result = f"Unfortunately You hit only {hit} number."
    else:
        result = f"Unfortunately You hit {hit} numbers."
    print(result)


lotto()
