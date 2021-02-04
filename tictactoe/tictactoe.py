# write your code here


def show_field(str_):
    print("---------")
    i, j = 0, 0
    list_ = list(str_)
    while i < 3:
        print("|", end="")
        count = 0
        while j < 9:
            if count == 3:
                break
            print(" " + list_[j], end="")
            j += 1
            count += 1
        print(" |")
        i += 1
    print("---------")


def check_win(str_, ch):
    # lists of indexes where "X" or "O" wins
    list_ = [[0, 1, 2], [8, 7, 6], [0, 4, 8], [2, 4, 6], [0, 3, 6], [2, 5, 8], [1, 4, 7], [3, 4, 5]]
    count = 0
    for group in list_:
        if str_[group[0]] == ch and str_[group[1]] == ch and str_[group[2]] == ch:
            count += 1
    return count


def is_impossible(str_):
    x = str_.count("X")
    y = str_.count("O")
    return True if x >= y + 2 or y >= x + 2 else False


def to_analyze(str_):
    x = check_win(str_, "X")
    o = check_win(str_, "O")
    if is_impossible(str_) or (o == 2 or x == 2) or o == x == 1:
        print("Impossible")
    elif x > o:
        print("X wins")
    elif o > x:
        print("O wins")
    elif (str_.count("X") + str_.count("O")) < 9:
        print("Game not finished")
    elif x == o == 0:
        print("Draw")


def enter_char(string, x, y):
    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
        if x < 1 or x > 3 or y < 1 or y > 3:
            print("Coordinates should be from 1 to 3!")
            return False
        elif string[(x - 1) * 3 + (y - 1)] != "_":
            print("This cell is occupied! Choose another one!")
            return False
        else:
            return True
    else:
        print("You should enter numbers!")
        return False


def main():
    string = "_________"
    show_field(string)
    # to_analyze(string)
    char = "X"
    while True:
        row, column = input("Enter the coordinates: ").split()
        if enter_char(string, row, column):
            string = string[:(int(row) - 1) * 3 + (int(column) - 1)] + char + \
                     string[(int(row) - 1) * 3 + (int(column) - 1) + 1:]
            show_field(string)
            to_analyze(string)
            if check_win(string, char) == 1:
                # print(char, "wins")
                break
            if char == "X":
                char = "O"
            elif char == "O":
                char = "X"
            if string.count("X") + string.count("O") == 9:
                break


main()

