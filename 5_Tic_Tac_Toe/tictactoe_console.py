import random
from os import system

BOARD_DIM = 3

board = [[0 for x in range(BOARD_DIM)] for y in range(BOARD_DIM)]

board_transformation = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}

suma_kol = suma_rzad = suma_przek1 = suma_przek2 = 0


def clear():
    system('clear')


def printInstructionBoard():
    print("\nTak wygląda plansza pomocnicza:")
    for i in range(BOARD_DIM):
        for j in range(BOARD_DIM):
            print(3*i+j+1, end=' ')
        print()
    print()


def playersMove(chosen_square):
    print("Ruch użytkownika:")
    wybrany_x = board_transformation[chosen_square][0]
    wybrany_y = board_transformation[chosen_square][1]
    while board[wybrany_x][wybrany_y] != 0:
        print("\nTo miejsce jest okupowane")
        return playersMove(int(input("Wybierz pole od 1 do 9: ")))
    board[wybrany_x][wybrany_y] += 1
    printBoard()


def computersMove():
    print("Ruch komputera:")
    computers_x = random.randint(0, 2)
    computers_y = random.randint(0, 2)
    while board[computers_x][computers_y] != 0:
        computers_x = random.randint(0, 2)
        computers_y = random.randint(0, 2)
    board[computers_x][computers_y] += -1
    printBoard()


def printBoard():
    print()
    for i in range(BOARD_DIM):
        for j in range(BOARD_DIM):
            if board[i][j] == 0:
                print('-', end=' ')
            elif board[i][j] == 1:
                print('X', end=' ')
            elif board[i][j] == -1:
                print('O', end=' ')
        print()
    print()


def zeroInBoard():
    for i in range(BOARD_DIM):
        for j in range(BOARD_DIM):
            if board[i][j] == 0:
                return True
    return False


def isTheGameFinished():
    if checkRowOrCol() or checkDiagonal():
        return True
    return False


def checkRowOrCol():
    global suma_kol
    global suma_rzad

    for i in range(BOARD_DIM):
        suma_rzad = suma_kol = 0

        for j in range(BOARD_DIM):
            suma_rzad += board[i][j]
            suma_kol += board[j][i]

        if abs(suma_rzad) == 3 or abs(suma_kol) == 3:
            return True

    return False


def printWhoWon():
    if suma_kol == 3 or suma_rzad == 3 or suma_przek1 == 3 or suma_przek2 == 3:
        print("Wygral użytkownik")
    elif suma_kol == -3 or suma_rzad == -3 or suma_przek1 == -3 or suma_przek2 == -3:
        print("Wygral komputer")
    else:
        print("Remis")


def checkDiagonal():
    global suma_przek1
    global suma_przek2

    suma_przek1 = suma_przek2 = 0

    for i in range(BOARD_DIM):
        for j in range(BOARD_DIM):
            if i == j:
                suma_przek1 += board[i][j]
            if i+j == BOARD_DIM-1:
                suma_przek2 += board[i][j]

    if abs(suma_przek1) == 3 or abs(suma_przek2) == 3:
        return True
    return False


def playerStarts():
    coinflip = random.randint(0, 1)
    if coinflip:
        print("Zaczyna użytkownik")
        return True
    print("Zaczyna komputer")
    return False


def ticTacToe():

    if not playerStarts():
        computersMove()

    while zeroInBoard():
        playersMove(int(input("Wybierz pole od 1 do 9: ")))
        if isTheGameFinished():
            break

        computersMove()
        if isTheGameFinished():
            break


def askIfWannaPlayAgain():
    return input("Chcesz zagrać jeszcze raz? Wpisz 'Tak', aby zagrać ponownie lub 'Koniec', aby zakończyć działanie programu:  ").lower()


def printThanks():
    print("Dzięki za grę. Do następnego!")


def main():
    clear()
    printInstructionBoard()
    ticTacToe()
    printWhoWon()
    #again = askIfWannaPlayAgain()


if __name__ == "__main__":
    main()
