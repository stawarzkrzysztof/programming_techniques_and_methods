from random import randint

MAX_TRIES = 6

MIN_NUMBER = 1
MAX_NUMBER = 100

best_try = MAX_TRIES+1 
game_number = 0

def printWelcome():
    print(f"\n\n\t\t\t\tZGADNIJ JAKA TO LICZBA?\n\nGra {game_number}.")
    
    #jesli gra ponownie, i udalo mu sie zgadnac w poprzedniej, wypisz najlepszą próbę
    if game_number > 1 and best_try < MAX_TRIES+1: 
        print(f"\nDo tej pory najszybciej udało Ci zgadnąć w następującej ilości prób: {best_try}")
    print(f"\nChcesz poczuć się jak jasnowidz?\nSpróbuj zatem zgadnąć, o jakiej liczbie myślę (z zakresu od {MIN_NUMBER} do {MAX_NUMBER} włącznie).\nUWAGA! TWOJA MAKSYMALNA ILOŚĆ PRÓB, W ILU MOŻESZ ZGADNĄĆ TO: {MAX_TRIES}")


def guessTheNumber(drawn):
    #zgadywanie liczby
    for current_try in range(1, MAX_TRIES+1):
        try:
            guessed = int(input("Wpisz liczbę:  "))
            if guessed == drawn:
                print(f"\nGRATULACJE!! Udało ci się zgadnąć moją liczbę ({drawn})!\nIlośc wykorzystanych prób: {current_try}\n")
                return current_try
            printHigherOrLower(guessed, drawn, current_try)
        except:
            print("\nZły typ danych: podana wartość nie jest liczbą, spróbuj ponownie.\n")
            return guessTheNumber(drawn)
            

def printHigherOrLower(guessed, drawn, current_try):
    if current_try == MAX_TRIES: #gdy osiągnął maksymalną ilość prób, przegrywa
        return gameOver(drawn)
    if guessed < drawn:
        return print(f"\nNiestety, liczba, o któtej myślę jest WIĘKSZA niż {guessed}. Spróbuj ponownie: (Pozostałe próby: {MAX_TRIES-current_try})")
    return print(f"\nNiestety, liczba, o któtej myślę jest MNIEJSZA niż {guessed}. Spróbuj ponownie (Pozostałe próby: {MAX_TRIES-current_try})")


def askToPlayAgain():
    question = input("Czy chcesz zagrać jeszcze raz? Wpisz 'Tak', aby zagrać ponownie lub wpisz 'Koniec', aby zakończyć działanie programu: ").lower()
    if question == 'tak':
        return 'tak'
    elif question == "koniec":
        return 'koniec'
    print("\nZłe polecenie, wpisz ponownie!")
    return askToPlayAgain()
    

def gameOver(drawn):
    print(f"\nNiestety, wykorzystałeś wszystkie dostępne próby. Moją liczbą było: {drawn}")
    print("""  
     G G G G      A      M       M  E E E
     G           A A     M M   M M  E
     G   G G    A   A    M   M   M  E E
     G     G   A A A A   M       M  E
     G G G G  A       A  M       M  E E E

         O O   V       V  E E E  R R R
       O     O  V     V   E      R    R
      O       O  V   V    E E    R R R
       O     O    V V     E      R   R
         O O       V      E E E  R    R\n
            
    """)


def printThanks():
    print("\nDzięki za grę. Do następnego!")

#main
again = 'tak' #pierwszy raz zagra na pewno
while again == 'tak': #dopoki gracz chce grać w gre
    game_number += 1
    printWelcome()
    final_tries = guessTheNumber(randint(MIN_NUMBER, MAX_NUMBER))
    if final_tries != None and best_try > final_tries: #jeżeli gracz wygrał, sprawdzamy czy pobił rekord
        best_try = final_tries
    again = askToPlayAgain() #zapytanie czy chcesz ponownie zagrać
printThanks()
