while True:
    starting_number = input("Enter a number: ")
    while int(starting_number) < 1:
        starting_number = input("Please enter a number greater than 1: ")
    n = int(starting_number)
    counter = 0
    while n != 1:
        counter += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n * 3) + 1
    print(counter)
    go_again = input("would you like to go again? (y/n)")
    while go_again != "y" and go_again != "n":
        go_again = input("Try another number? (y/n)")
    if go_again == "y":
        continue
    else:
        break  
