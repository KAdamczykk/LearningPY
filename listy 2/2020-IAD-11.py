#import numpy
#from PIL import Image
#import math

'''
Funkcja znajduje pierwsze powtórzenie o długości k w zadanym ciągu.
Jeżeli takie powtórzenie nie istnieje, należy zwrócić pustą listę []

Przykład: wywołanie znajdz_pierwsze_powtorzenie_k([1, 2, 1, 2, 3, 1, 2, 3, 4, 2, 3, 4], 3)
powinno zwrócić listę [1, 2, 3]
'''
def znajdz_pierwsze_powtorzenie_k(ciag, k):
    return []

'''
Funkcja znajduje długość najdłuższego powtórzenia w zadanym ciągu.
Jeśli nie ma powtórzeń, należy zwrócić 0.

Przykład; wywołanie najdluzsze_powtorzenie([1, 2, 1, 2, 3, 2, 1, 2, 3])
powinno zwrócić liczbę 4
'''
def najdluzsze_powtorzenie(ciag):
    return 0

'''
Funkcja zwraca nowy ciąg powstały przez usuwanie powtórzeń o długości k z zadanego ciągu tak długo, jak to możliwe. 
Uwaga: tak jak w przykładzie, przy każdym usuwaniu pozostawiamy jedną kopię powtarzającego się fragmentu.

Przykład: wywołanie usun_powtorzenia_k([1, 2, 3, 4, 1, 2, 3, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1], 4)
powinno zwrócić listę [1, 2, 3, 4, 3, 2, 1]
'''
def usun_powtorzenia_k(ciag, k):
    return []


def mainA():
    print("\n***************************************** ETAP 1 *****************************************\n")
    maleTesty1 = []
    maleTesty1.append(([1, 2, 3, 4, 5, 6], 3, []))
    maleTesty1.append(([1, 2, 3, 4, 2, 3, 4, 5, 3, 4, 5], 3, [2, 3, 4]))
    maleTesty1.append(([1, 2, 2, 2, 4, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2], 5, [1, 2, 2, 2, 1]))
    maleTesty1.append(([1, 2, 3, 4, 1, 2, 3, 3, 2, 1, 3, 3, 2, 1, 1, 3, 2, 1, 1], 4, [3, 3, 2, 1]))
    for (ciag, k, wynik) in maleTesty1:
        print("Ciag:            ", ciag)
        print("Wynik:           ", znajdz_pierwsze_powtorzenie_k(ciag, k))
        print("Oczekiwany wynik:", wynik, end="\n\n")


    print("\n***************************************** ETAP 2 *****************************************\n")
    maleTesty2 = []
    maleTesty2.append(([1, 2, 3, 4, 5, 6], 0))
    maleTesty2.append(([1, 2, 3, 4, 2, 3, 4, 5, 3, 4, 5], 3))
    maleTesty2.append(([1, 2, 2, 2, 4, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2], 5))
    maleTesty2.append(([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4], 5))
    maleTesty2.append(([1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 3], 10))
    for (ciag, wynik) in maleTesty2:
        print("Ciag:            ", ciag)
        print("Wynik:           ", najdluzsze_powtorzenie(ciag))
        print("Oczekiwany wynik:", wynik, end="\n\n")


    print("\n***************************************** ETAP 3 *****************************************\n")
    maleTesty3 = []
    maleTesty3.append(([0, 1, 2, 2, 0, 1, 2, 3, 1, 2, 3, 4, 2, 3, 4], 3, [0, 1, 2, 2, 0, 1, 2, 3, 4]))
    maleTesty3.append(([1, 2, 3, 4, 5, 6], 3, [1, 2, 3, 4, 5, 6]))
    maleTesty3.append(([1, 2, 3, 4, 2, 3, 4, 5, 3, 4, 5], 3, [1, 5, 3, 4, 5]))
    maleTesty3.append(([1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7], 4, [1, 2, 3, 4, 5, 6, 7]))
    maleTesty3.append(([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 3, 2, 2, 2, 2, 3], 5, [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3]))
    for (ciag, k, wynik) in maleTesty3:
        print("Ciag:            ", ciag)
        print("Wynik:           ", usun_powtorzenia_k_slow(ciag, k))
        print("Oczekiwany wynik:", wynik, end="\n\n")



    print("\n******************************** KONTROLA CZASU DZIAŁANIA ********************************\n")
    print("Etap 1:")
    duzeTesty1 = []
    duzeTesty1.append(([3] * 15000 + [2] * 2000 + [1] * 3999 + [3] * 19999 + ([1] * 4000 + [2] * 2000 + [3] * 4000) * 2 + [1] * 4000 + [2] * 2000 + [1] * 3999 + [3] * 19999, 10000))
    duzeTesty1.append(((([1] * 9999) + [2]) * 7 + [1]*10000 + [2] + (([1] * 9999) + [2]) * 3, 5000))
    for (ciag, k) in duzeTesty1:
        print("Test wydajności... ", end="")
        wynik = znajdz_pierwsze_powtorzenie_k(ciag, k)
        if len(wynik) == k:
            print("zakończony.")
        else:
            print("błąd!!!")

    print("Etap 2:")
    duzeTesty2 = []
    duzeTesty2.append(((([1] * 499) + [2]) * 7 + [1]*500 + [2] + (([1] * 499) + [2] ) * 3, 1501))
    duzeTesty2.append(([1] * 1000 + [2] * 2000 + [1] * 500 + [2] * 3000, 2500))
    for (ciag, k) in duzeTesty2:
        print("Test wydajności... ", end="")
        wynik = najdluzsze_powtorzenie(ciag)
        if wynik == k:
            print("zakończony.")
        else:
            print("błąd!!!", wynik)


    print("Etap 3:")
    duzeTesty3 = []
    duzeTesty3.append(([3] * 15000 + [2] * 2000 + [1] * 3999 + [3] * 19999 + ([1] * 4000 + [2] * 2000 + [3] * 4000) * 2 + [1] * 4000 + [2] * 2000 + [1] * 3999 + [3] * 19999, 10000, 70996))
    duzeTesty3.append(((([1] * 9999) + [2]) * 7 + [1]*10000 + [2] + (([1] * 9999) + [2]) * 3, 5000, 105001))
    K = 5000
    tab = list(range(K))
    for i in range(K // 5):
        tab.append(i + K - 1)
        tab += list(range(i, i + K))
    duzeTesty3.append((tab, K, 2 * K + K // 5))
    for (ciag, k, dl) in duzeTesty3:
        print("Test wydajności... ", end="")
        wynik = usun_powtorzenia_k(ciag, k)
        if len(wynik) == dl:
            print("zakończony.")
        else:
            print("błąd!!!", len(wynik), "vs.", dl)

if __name__ == "__main__":
    mainA()