def get_and_greet_name():

    name = input("Input his/her name: ")

    msg1 = f"Hello {name},"
    msg2 = "Welcome to Seoul."

    max_length = max(len(msg1), len(msg2))

    print('-' * (max_length + 2))
    print(msg1)
    print(msg2)
    print('-' * (max_length + 2))

