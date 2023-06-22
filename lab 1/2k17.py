import math
def main():
    rok = int(input("Rok urodzenia"))
    if rok <= 1900:
        raise ValueError

    miesiac = int(input("Miesiąc urodzenia"))
    if miesiac < 1 or miesiac > 12:
        raise ValueError
    dzien = int(input("Dzień urodzenia"))
    if dzien<1:
        raise ValueError
    if miesiac == {1,3,5,7,8,10,12}:
        dzien <=31
    elif miesiac == {4,6,9,11}:
        dzien <=30
    elif miesiac == 2 and rok%4==0 and rok%100!=0:
        dzien <=29
    elif miesiac ==2 and rok%400==0:
        dzien<=29
    else:
        dzien<=28
    print(f"Rok urodzenia{rok}")
    print(f"Miesiąc urodzenia{miesiac}")
    print(f"Dzień urodzenia {dzien}")


    if miesiac == {4,5}:
        print("Urodziłeś się na wiosne")
    elif miesiac == 3 and dzien>=21:
        print("Urodziłeś się na wiosne")
    elif miesiac == 6 and dzien <=21:
        print("Urodziłeś się na wiosne")
    elif miesiac == {7,8}:
        print("Urodziłeś się w lato")
    elif miesiac == 6 and dzien >= 22:
        print("Urodziłeś się w lato")
    elif miesiac==9 and dzien <=22:
        print("Urodziłeś się w lato")
    elif miesiac =={10,11}:
        print("Urodziłeś się na jesień")
    elif miesiac == 9 and dzien >=23:
        print("Urodziłeś się na jesień")
    elif miesiac == 12 and dzien<=21:
        print("Urodziłeś się na jesień")
    else:
        print("Urodziłeś się na zime")
    Y = rok
    if Y >= 2000:
        y = Y - 2000
        c = 20
    else:
        y = Y - 1900
        c = 19
    if miesiac >=3:
        m = miesiac -2
    elif miesiac == {1,2} :
        m = miesiac + 10
    dzien_uro = (dzien + math.floor(2.6 * m - 0.2) + y + math.floor(y / 4) + math.floor(c / 4) - 2 * c) % 7


    print(f"Urodziłeś się w {dzien_uro} dzień tygodnia")
    rok_ref = int(input("Rok referencyjny"))
    if rok_ref <= 1900:
        raise ValueError

    miesiac_ref = int(input("Miesiąc referencyjny"))
    if miesiac_ref < 1 or miesiac_ref > 12:
        raise ValueError
    dzien_ref = int(input("Dzień referencyjny"))
    if dzien_ref < 1:
        raise ValueError
    if miesiac_ref == {1, 3, 5, 7, 8, 10, 12}:
        dzien_ref <= 31
    elif miesiac_ref == {4, 6, 9, 11}:
        dzien_ref <= 30
    elif miesiac_ref == 2 and rok_ref % 4 == 0 and rok_ref % 100 != 0:
        dzien_ref <= 29
    elif miesiac_ref == 2 and rok_ref % 400 == 0:
        dzien_ref <= 29
    else:
        dzien_ref <= 28
    if rok_ref < rok:
        raise ValueError
    if rok_ref == rok and miesiac_ref < miesiac:
        raise ValueError
    if rok_ref == rok and miesiac_ref == miesiac and dzien_ref < dzien:
        raise ValueError






if "__main__" == __name__:
     main()