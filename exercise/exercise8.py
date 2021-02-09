while True:
    check = input("would you like to play? yes/no: ")
    if check == "yes":
        input1 = input()
        input2 = input()
        if input1 == input2:
            print("tie")
        else:
            if input1 == "rock" and input2 == "scissors":
                print("player 1 wins")
            elif input1 == "paper" and input2 == "rock":
                print("player 1 wins")
            elif input1 == "scissors" and input2 == "paper":
                print("player 1 wins")
            else:
                print("player 2 wins")
    if check == "no":
        print("bye");
        break