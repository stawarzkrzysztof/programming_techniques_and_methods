from random import randint
from os import system
from math import sqrt
from math import floor
import time

# operuję na nomenklaturze macierzowej (najpierw rząd, później kolumna)
ROWS = 10
COLUMNS = 45

sonars = 20

chests_coordinates = []
board = [['0' for x in range(COLUMNS+2)] for y in range(ROWS+2)]
instrukcja = """
Na planszy o wymiarach 60 (0-59) na 15 (0-14) do znalezienia są 3 skrzynie, a gracz może w tym celu użyć jedynie 20 sonarów. Wyobraź sobie, że nie widzisz skrzyni ze skarbami. Ponieważ każdy sonar potrafi podać jedynie odległość od skrzyni, lecz nie kierunek, skarb może znajdować się w którymkolwiek miejscu na zatoczonym przez sonar okręgu. Przy użyciu więcej niż jednego sonaru możliwe jest jednak namierzenie skrzyń (ograniczenie miejsc ich zatopienia tylko do punktów przecięcia się okręgów. Umieszczenie sonaru w miejscu gdzie znajduje się skrzynia powoduje, że została ona zabrana przez naszego gracza, a ilość skrzyń do odnalezienie zmniejsza się o 1. Rozszerz wersję gry o 3 poziomy trudności (najłatwiejszy 3 skrzynie, zaawansowany 5 skrzyń, ekspert 8 skrzyń). Maksymalny zasięg sonaru to 5. Użytkownik ma prawo przerwać grę za pomocą polecenia "koniec" oraz wyświetlić instrukcję za pomocą polecenia "instrukcja".

pierwsza wspolrzedna - pionowa (0 - ilosc wierszy)
druga wsporzedna - pozioma  (0 - ilosc kolumn)
"""


def clear():
    system('clear')


def printWelcome():
    print("\n\n\t\t\t\t\t\t\t\t\tPOSZUKIWANIE SKARBU SONAREM\n")


board = [['0' for x in range(COLUMNS+2)] for y in range(ROWS+2)]


def createBoard():
    for x in range(ROWS+2):
        for y in range(COLUMNS+2):
            if (x == 0 and y == 0) or (x == 0 and y == COLUMNS+1) or (x == ROWS+1 and y == 0) or (x == ROWS+1 and y == COLUMNS+1):
                board[x][y] = ""
            else:
                if x == 0 or x == ROWS+1:
                    board[x][y] = str(y-1)
                else:
                    if y == 0 or y == COLUMNS+1:
                        board[x][y] = str(x-1)
                    else:
                        board[x][y] = '.'


def printBoard():
    for x in range(ROWS+2):
        for y in range(COLUMNS+2):
            if (x == 0 and y == 0) or (x == 0 and y == COLUMNS+1) or (x == ROWS+1 and y == 0) or (x == ROWS+1 and y == COLUMNS+1):
                print(board[x][y], end='   ')
            elif x == 0 or x == ROWS+1:  # wypisanie id wiersza
                if (y-1) < 10:
                    print(board[x][y], end='  ')
                else:
                    print(board[x][y], end=' ')
            elif y == 0:  # wypisanie id kolumny
                if (x-1) < 10:
                    print(' ', board[x][y], sep='', end=' ')
                else:
                    print(board[x][y], end=' ')
            elif y == COLUMNS:
                print(board[x][y], end=' ')
            elif y == COLUMNS+1:
                print(board[x][y], end='')
            else:
                print(board[x][y], end='  ')
        print()


def setChestsCoordinates(number_of_chests):

    for _ in range(number_of_chests):
        current_chest = (randint(0, ROWS-1), randint(0, COLUMNS-1))
        while current_chest in chests_coordinates:  # zapewnienie sobie unikalności położenia skrzyń
            current_chest = (randint(0, ROWS-1), randint(0, COLUMNS-1))
        chests_coordinates.append(current_chest)


def playTheGame(sonars_number):
    while sonars_number > 0:
        clear()

        printHowManyLeft(sonars_number)

        if sonars != sonars_number:
            lastSonarRaport(guessed_chest_x, guessed_chest_y, min_distance)

        printBoard()

        sonars_number -= 1
        guessed_chest_x = guessChestX()
        guessed_chest_y = guessChestY()
        while board[guessed_chest_x+1][guessed_chest_y+1] != '.':
            print("Na to pole wrzuciłeś już sonar. Wybierz inne.")
            guessed_chest_x = guessChestX()
            guessed_chest_y = guessChestY()

        krotka = (guessed_chest_x, guessed_chest_y)

        min_distance = 6

        printSinkSonar(guessed_chest_x, guessed_chest_y)

        for i in range(len(chests_coordinates)):
            if krotka == chests_coordinates[i]:
                board[guessed_chest_x+1][guessed_chest_y+1] = "✔︎"
                chests_coordinates.pop(i)
                input(
                    f"\nSkrzynia znaleziona! Naciśnij dowolny klawisz, aby kontynuować. ")
                break
            else:
                distance = floor(sqrt((guessed_chest_x - chests_coordinates[i][0])**2 + (
                    guessed_chest_y - chests_coordinates[i][1])**2))
                if distance < min_distance:
                    min_distance = distance
                if min_distance < 6:
                    board[guessed_chest_x+1][guessed_chest_y +
                                             1] = str(min_distance)
                else:
                    board[guessed_chest_x+1][guessed_chest_y+1] = "✘"

        if len(chests_coordinates) == 0:
            clear()
            printBoard()
            return print("\nODNALAZŁEŚ WSZYSTKIE SKRZYNIE!! WYGRAŁEŚ!!!")
    clear()
    for i in range(len(chests_coordinates)):
        board[chests_coordinates[i][0]+1][chests_coordinates[i][1]+1] = '☹︎'
    printBoard()
    print("Skonczyły ci sie sonary! U lost")
    return print(f"Pozostałe skrzynie były ukryte w: {chests_coordinates}")


def lastSonarRaport(guessed_chest_x, guessed_chest_y, min_distance):
    print("Raport z ostataniego zatopionego sonaru: ")
    if board[guessed_chest_x+1][guessed_chest_y+1] == '✔︎':
        print(
            f"Skrzynia znaleziowa na polu ({guessed_chest_x},{guessed_chest_y}).\n")
    elif board[guessed_chest_x+1][guessed_chest_y+1] == '✘':
        print(
            f"Nie znaleziono skrzyni w zasięgu 5 sonaru ({guessed_chest_x},{guessed_chest_y})\n")
    elif 1 <= int(board[guessed_chest_x+1][guessed_chest_y+1]) <= 5:
        print(
            f"Odnaleziono skrzynie w odległości {min_distance} od sonaru ({guessed_chest_x},{guessed_chest_y})\n")


def printHowManyLeft(sonars_number):
    if len(chests_coordinates) >= 5:
        print(f"Do wyłowienia: {len(chests_coordinates)} skrzyń")
    elif 1 < len(chests_coordinates) < 5:
        print(f"Do wyłowienia: {len(chests_coordinates)} skrzynie")
    elif len(chests_coordinates) == 1:
        print("Do wyłowienia: 1 skrzynia")
    return print(f"Pozostałe sonary: {sonars_number}\n")


def printSinkSonar(x, y):
    print(f"\nZatapiam sonar na polu ({x},{y})...")
    time.sleep(0.5)
    for i in range(3):
        print("...")
        time.sleep(0.5)


def guessChestX():
    guessed_chest_x = input(
        "\nPodaj pierwszą wspołrzędną pola, na którym chcesz zatopić sonar:  ")

    if guessed_chest_x.lower() == "koniec":
        print("The program has finished, bye:)")
        quit()

    while guessed_chest_x.lower() == "instrukcja":
        print(instrukcja)
        input("Nacisnij Enter, aby zakończyć wyświetlanie funkcji.")
        return guessChestX

    try:
        guessed_chest_x = int(guessed_chest_x)
        while guessed_chest_x < 0 or guessed_chest_x >= ROWS:
            print("Nie ma takiej współrzędnej. Spróbuj ponownie.")
            guessed_chest_x = int(
                input("\nPodaj pierwszą wspołrzędną pola, na którym chcesz zatopić sonar:  "))
        return guessed_chest_x

    except:
        print("Nie ma takiej współrzędnej. Spróbuj ponownie.")
        return guessChestX()


def guessChestY():
    guessed_chest_y = input(
        "\nPodaj drugą wspołrzędną pola, na którym chcesz zatopić sonar:  ")

    if guessed_chest_y.lower() == "koniec":
        print("The program has finished, bye:)")
        quit()

    while guessed_chest_y.lower() == "instrukcja":
        print(instrukcja)
        input("Nacisnij Enter, aby zakończyć wyświetlanie funkcji.")
        return guessChestY
    try:
        guessed_chest_y = int(guessed_chest_y)
        while guessed_chest_y < 0 or guessed_chest_y >= COLUMNS:
            print("Nie ma takiej współrzędnej. Spróbuj ponownie.")
            guessed_chest_y = int(
                input("\nPodaj pierwszą wspołrzędną pola, na którym chcesz zatopić sonar:  "))
        return guessed_chest_y

    except:
        print("Nie ma takiej współrzędnej. Spróbuj ponownie.")
        return guessChestX()


def chooseDifLvl():
    lvl = input(
        "\nWybierz poziom trudności:\n1.Easy\n2.Medium\n3.Expert\n\n").lower()

    if lvl.lower() == "koniec":
        print("The program has finished, bye:)")
        quit()

    while lvl.lower() == "instrukcja":
        print(instrukcja)
        input("Nacisnij Enter, aby zakończyć wyświetlanie funkcji.")
        return chooseDifLvl()

    if lvl == "1" or lvl == "easy" or lvl == "1." or lvl == "1.easy" or lvl == "1. easy" or lvl == "1. easy " or lvl == "1.easy ":
        return 3
    elif lvl == "2" or lvl == "medium" or lvl == "2." or lvl == "2.medium" or lvl == "2. medium" or lvl == "2. medium " or lvl == "2.medium ":
        return 5
    elif lvl == "3" or lvl == "expert" or lvl == "3." or lvl == "3.expert" or lvl == "3. expert" or lvl == "3. expert " or lvl == "3.expert ":
        return 8

    print("Nie ma takiego poziomu. Spróbuj ponownie.")
    return chooseDifLvl()


def main():
    clear()
    # print(board)
    printWelcome()
    createBoard()
    setChestsCoordinates(chooseDifLvl())
    playTheGame(sonars)


if __name__ == "__main__":
    main()
