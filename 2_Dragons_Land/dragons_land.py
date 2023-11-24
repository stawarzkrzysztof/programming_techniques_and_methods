from random import randint
from random import uniform
from random import shuffle
from os import system
import dragons

# 0 -> smok zły
# 1 -> smok dobry

# szansa na bycie dobrym smokiem od (drugiej rundy w zwyż); podana W PROCENTACH! (liczba całkowita, nie musi być podzielna przez 10)
GOOD_ODDS = 30  # %
NUMBER_OF_ROUNDS = 10  # ilość rund
ascii_dragons = dragons.ascii_dragons  # ascii art smokow
treasure = dragons.treasure[0]  # grafika widoczna po wygranej'''


def clear():
    system('clear')


def printWelcome():
    print("\t\t\t\t\t\t\tSMOCZA KRAINA\n\nWitaj w Smoczej Krainie, poszukiwaczu przygód.\nZapewne poszukujesz skarbu? Droga do niego nie jest usłana różami. Czeka Cię 10 spotkań z potwornymi, ziejącymi ogniem SMOKAMI.\nWchodząć do pierwszego korytarza, napotkasz dwie bestie. Jedną miłą i uprzjemą, która przepuści Cię dalej. Natomiast druga pożera w całości.\nStaniesz przed wyborem, któremu smokowi chcesz zaufać.\nJeśli Ci się uda, w następnej rundzie będziesz miał do czynienia z o jednym więcej smokiem, niż w rundzie poprzedniej.\nNa końcu korytarza czeka Cię ogromny skarb, który sprawi, że nie będziesz musiał pracować do końca swych dni.\nPowodzenia, podróznku...\n\n")


def summonDragons(round_number):
    # w pierwszej rundzie zapewniamy 50%
    if round_number == 1:
        good_or_bad = randint(0, 1)
        dragons = {'SMOK1': good_or_bad, 'SMOK2': 1-good_or_bad}
        return dragons  # słownik z przygotowanymi smokami na konkretną runde

    good_dragons_counter = 0
    while good_dragons_counter == 0:
        dragons = {}

        for id in range(round_number+1):  # w n-tej rundzie pojawi się n+1 smokow
            # id smoka w danej rundzie (np. SMOK1)
            dragon_name = 'SMOK'+str(id+1)

            # prawdopodobieństwo ustawia się w linijce #8
            if round(uniform(0.0, 10.0), 1) <= GOOD_ODDS/10:
                dragons[dragon_name] = 1
                good_dragons_counter += 1
            else:
                dragons[dragon_name] = 0

    return dragons  # słownik z przygotowanymi smokami na konkretną runde


def lost(choosen_dragon):

    if choosen_dragon == 0:
        return True

    return False


def dragonsLand():
    shuffle(ascii_dragons)
    counter = 0  # licznik przechodzący po całej tablicy ascii_dragons'''

    for round_number in range(1, NUMBER_OF_ROUNDS+1):
        # stwórz słownik ze smokami na obecną rundę
        dragons = summonDragons(round_number)

        if round_number > 1:  # jeśli przeszedł rundę, wyświetl tekst motywujący
            clear()
            print(
                "Gratulacje, udało Ci się przejść do kolejnej rundy.\nCiekawe, jak teraz sobie poradzisz...")

        print(f"\nRunda {round_number}.\n")
        keys = list(dragons.keys())

        for key in range(len(keys)):  # wypisanie smoków
            print('\n\t\t', keys[key], ascii_dragons[counter % 65], sep='')
            counter += 1
        print(dragons)

        choosen_dragon = input(
            "\nWpisz nazwę smoka, któremu chcesz zaufać (według wzoru: SMOKn, gdzie n to numer smoka):\n").upper()
        while choosen_dragon not in dragons:
            print("Nie ma takiego smoka. Spróbuj ponownie.")
            choosen_dragon = input(
                "\nWpisz nazwę smoka, któremu chcesz zaufać (według wzoru: smokn, gdzie n to numer smoka):\n").upper()

        if lost(dragons[choosen_dragon]):  # sprawdzenie, czy przegrał
            return gameOver()

    return youWon()


def youWon():
    clear()
    print("\nGratulacje podróżniku, udało ci się ominąć wszystkie nieprzyjazne bestie. Oto Twoja nagroda - pieniądze potrzebne na opłacenie waruku:)\n")
    print(treasure)


def gameOver():
    clear()
    print("\nNiestety, pożarł Cię zły smok:(")
    print("""  
    GGGGG      A     M      M  EEEEE
    G         A A    M M  M M  E
    G GGG    A   A   M  MM  M  EEE
    G   G   AAAAAAA  M      M  E
    GGGGG  A       A M      M  EEEEE

       O    V       V EEEEE  R R 
     O   O   V     V  E      R  R
    O     O   V   V   EEE    R R
     O   O     V V    E      R   R
       O        V     EEEEE  R     R
            
    """)


def askToPlayAgain():
    answear = input(
        "\nCzy chcesz zagrać jeszcze raz? Wpisz 'Tak', aby zagrać ponownie lub wpisz 'Koniec', aby wyjść z gry:  ").lower()
    while answear != "tak" and answear != "koniec":
        print("Nie znam takiego polecenia. Czy mógłbyś wpisać je ponownie?")
        return askToPlayAgain()
    return answear


def printThanks():
    return input("\nDzięki za grę. Do następnego!\nNaciśnij Enter, aby zakończyć działanie programu")


# main
again = "tak"
while again == 'tak':  # pierwszy raz zagra po odpaleniu kodu, a później może decydować
    clear()
    printWelcome()
    dragonsLand()  # właściwa gra
    again = askToPlayAgain()
printThanks()
