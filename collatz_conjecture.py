while True:

    chosen_number = 0
        
    while chosen_number < 1:

        try:
            chosen_number = int(input("Please enter a number greater than 1: "))
        except ValueError:
            print('The number must be an integer!')

    counter = 0

    while chosen_number != 1:

        counter += 1
        if chosen_number % 2 == 0:
            chosen_number = chosen_number / 2
            print(int(chosen_number))
        else:
            chosen_number = (chosen_number * 3) + 1
            print(int(chosen_number))
    print(f'That took {counter} turns!')

    go_again = ''

    while go_again != "y" and go_again != "n":

        go_again = input("would you like to go again? (y/n) ")

    if go_again == "y":
        continue
    else:
        print('Goodbye!')
        break  
