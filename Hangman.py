def hangman(word):
    wrong = 0
    stages = ["",
              "________      ",
              "|       |     ",
              "|       |     ",
              "|       0     ",
              "|      /|\    ",
              "|      / \    ",
              "|             ",
              ]
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print("Welcom to the penalty!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Enter a letter: "
        guess = input(msg)
        if guess in rletters:
            cind = rletters.index(guess)
            board[cind] = guess
            rletters[cind] = "$"
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You have won! It was made the word: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        #print("\n".join(stages[0: e]))
        print("You lose! It is made a word: {}.".format(word))

hangman("cat")
