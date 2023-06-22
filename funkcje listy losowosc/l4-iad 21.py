import random
import math
random.seed(2014)
def print_header():
    print("1 - wylosuj początek przedziału")
    print("2 - wylosuj koniec przedziału")
    print("3 - zapisz wyliczenia do pliku")
    print("4- wczytaj stan z pliku")
    print("5 - wyjdz z programu")
def read_action(wybor_akcji):
    if  wybor_akcji==1 or wybor_akcji==2 or wybor_akcji==3 or wybor_akcji==4 or wybor_akcji==5:
        return wybor_akcji
    else:
        return print_header()
def generate_beginning(order_of_magniture):
    if order_of_magniture==1:
        poczatek_przedzialu = random.randint(1,6)
        return poczatek_przedzialu
    else:
        a= random.randint(1,6)
        poczatek_przedzialu = a*10 + random.randint(1,6)
        return poczatek_przedzialu

def generate_end(order_of_magniture):
    if order_of_magniture==1:
        rzad = 0
        liczba=0
        while rzad <=2:
            if random.random()<0.15 and rzad==0:
                continue
            elif random.random()<0.15 and rzad!=0:
                number = 0
                rzad +=1
                liczba+=0
            elif 0.15<=random.random()<0.2:
                number = 9
                rzad+=1
                liczba += number*10**(2-rzad)
            else:
                number = random.randint(2,8)
                rzad+=1
                liczba += number*10**(2-rzad)
        return liczba
    else:
        rzad = 0
        liczba = 0
        while rzad <= 3:
            if random.random() < 0.15 and rzad == 0:
                continue
            elif random.random() < 0.15 and rzad != 0:
                number = 0
                rzad += 1
                liczba += 0
            elif 0.15 <= random.random() < 0.2:
                number = 9
                rzad += 1
                liczba += number * 10 ** (3 - rzad)
            else:
                number = random.randint(2, 8)
                rzad += 1
                liczba += number * 10 ** (3 - rzad)
        return liczba
def concatenate_abundants_from_range(poczatek_przedzialu, koniec_przedzialu):
    if poczatek_przedzialu == math.nan and koniec_przedzialu== math.nan:
        return poczatek_przedzialu == math.nan, koniec_przedzialu == math.nan
    else:
        suma_zlozen = 0
        nadmiarowe =0
        for i in range(poczatek_przedzialu, koniec_przedzialu + 1):
            for j in range (1,i):
                if i%j==0:
                    suma_zlozen+=j
                    j+=1
                else:
                    j+=1
            if suma_zlozen>i:
                nadmiarowe = nadmiarowe*100 + i
                i+1
                suma_zlozen=0
            else:
                i+=1
                suma_zlozen=0
    return nadmiarowe
def save_file(poczatek_przedzialu, koniec_przedzialu, liczba_zlozona, order_of_magniture):
    if poczatek_przedzialu==math.nan or koniec_przedzialu==math.nan:
        print("Za mało danych")
    else:
        nazwa_pliku = str(input("Podaj nazwe pliku"))
        with open(nazwa_pliku, "w+") as plik:
            plik.write(f"<{poczatek_przedzialu} : {koniec_przedzialu}> => {liczba_zlozona}")
        print(f"<{poczatek_przedzialu} : {koniec_przedzialu}> => {liczba_zlozona}")
def read_from_file():
    nazwa_pliku= str(input("Podaj nazwe pliku"))
    with open(nazwa_pliku, "r") as plik:
        return print(plik.read())


def main():
    if random.random()<0.6:
        order_of_magniture=1
    else:
        order_of_magniture=2
    wybor_akcji = 0
    poczatek_przedzialu = math.nan
    koniec_przedzialu = math.nan
    liczba_zlozona = math.nan
    while wybor_akcji>=0:
        print(print_header())
        wybor_akcji = int(input("Wybierz numer akcji"))
        nr_akcji = read_action(wybor_akcji)
        if nr_akcji == 1:
            poczatek_przedzialu = int(generate_beginning(order_of_magniture))
            koniec_przedzialu=math.nan
            liczba_zlozona=math.nan
            print(f"<{poczatek_przedzialu} : {koniec_przedzialu}> => {liczba_zlozona}")
        elif nr_akcji == 2:
            koniec_przedzialu = int(generate_end(order_of_magniture))
            liczba_zlozona = concatenate_abundants_from_range(poczatek_przedzialu, koniec_przedzialu)
            print(f"<{poczatek_przedzialu} : {koniec_przedzialu}> => {liczba_zlozona}")
        elif nr_akcji==3:
            save_file(poczatek_przedzialu, koniec_przedzialu, liczba_zlozona, order_of_magniture)
        elif nr_akcji==4:
            read_from_file()
        elif nr_akcji ==5:
            print("Wyjscie")
            print(f"<{poczatek_przedzialu} : {koniec_przedzialu}> => {liczba_zlozona}")
            break







if __name__ == '__main__':
    main()