import math
import random
def rzucaj(liczba_kosci):
    suma_oczek = 0
    for i in range (1,liczba_kosci+1):
        liczba = random.randint(1,6)
        print(f"Wyrzuciłeś {liczba}")
        suma_oczek+=liczba
    return suma_oczek
def bonus(suma_oczek):
    bonus=0
    for i in range (2, suma_oczek):
        if suma_oczek%i==0:
            bonus+=1
    return bonus
def zapisz_do_pliku(sciezka, nr_gracza, liczba_kosci, bonus, suma ):
    with open(sciezka, "a") as file:
        file.write(f"Gracz {nr_gracza}, liczba kości: {liczba_kosci}, bonus: {bonus}, suma: {suma}")
        file.write("\n")
def main():
    random.seed(1354)
    liczba_wygrywająca = random.randint(10,50)
    suma_oczek_1 = 0
    suma_oczek_2 = 0
    parametr=1
    tura_1 =True
    tura_2 = False
    sciezka= "gramad2020.txt"
    while parametr>=0:
        if tura_1:
            print(f"Liczba wygrywająca {liczba_wygrywająca}")
            print(f"Suma gracza 1 wynosi {suma_oczek_1}")
            print(f"Suma gracza 2 wynosi {suma_oczek_2}")
            print("Tura gracza 1")
            liczba_kosci = int(input("Podaj liczbe kości, którymi rzucasz"))
            if not (liczba_kosci ==1 or liczba_kosci ==2 or liczba_kosci==3):
                print("Błędna wartość, tracisz ruch!")
                tura_1 =False
                tura_2 =True
            else:
                los = rzucaj(liczba_kosci)
                suma_oczek_1+=los
                bonusowe_oczka = bonus(los)
                print(f"Bonus: {bonusowe_oczka}")
                suma_oczek_1+=bonusowe_oczka
                zapisz_do_pliku(sciezka, 1, liczba_kosci, bonusowe_oczka, suma_oczek_1)
                tura_1 = False
                tura_2 = True

        elif tura_2:
            print(f"Liczba wygrywająca {liczba_wygrywająca}")
            print(f"Suma gracza 1 wynosi {suma_oczek_1}")
            print(f"Suma gracza 2 wynosi {suma_oczek_2}")
            print("Tura gracza 2")
            liczba_kosci = int(input("Podaj liczbe kości, którymi rzucasz"))
            if not (liczba_kosci ==1 or liczba_kosci ==2 or liczba_kosci==3):
                print("Błędna wartość, tracisz ruch~!")
                tura_1 =True
                tura_2 =False
            else:
                los = rzucaj(liczba_kosci)
                suma_oczek_2+=los
                bonusowe_oczka = bonus(los)
                print(f"Bonus: {bonusowe_oczka}")
                suma_oczek_2+=bonusowe_oczka
                zapisz_do_pliku(sciezka, 2, liczba_kosci, bonusowe_oczka, suma_oczek_1)
                tura_1 =True
                tura_2 =False
        if suma_oczek_1>=liczba_wygrywająca and suma_oczek_2<liczba_wygrywająca:
            print("Wygrał gracz 1")
            with open(sciezka, "a") as file:
                file.write("Wygrał gracz 1")
            break
        elif suma_oczek_1<liczba_wygrywająca and suma_oczek_2>=liczba_wygrywająca:
            print("Wygrał gracz 2")
            with open(sciezka, "a") as file:
                file.write("Wygrał gracz 2")
            break
        elif suma_oczek_1>=liczba_wygrywająca and suma_oczek_2>=liczba_wygrywająca:
            if suma_oczek_1>suma_oczek_2:
                print("Wygrał gracz 1")
                with open(sciezka, "a") as file:
                    file.write("Wygrał gracz 1")
                break
            elif suma_oczek_1<suma_oczek_2:
                print("Wygrał gracz 2")
                with open(sciezka, "a") as file:
                    file.write("Wygrał gracz 2")
                break
            else:
                print("Remis")
                with open(sciezka, "a") as file:
                    file.write("Remis")
                break

if __name__ == "__main__":
    main()