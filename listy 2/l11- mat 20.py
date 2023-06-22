import math
PRZYKLADOWE_DANE = [
        (1, 10), (12, 30), (15, 25), (26, 29), (7, 21), (32, 38)
    ]
N = 40
def wypisz_os(x_max, krok):
    print('0', end='')
    i = krok
    while i <= x_max:
        print(f'{i:.>{krok}d}', end='')
        i += krok
    print('.' * (x_max - i))
def wypisz_przedzialy(przedzialy, x_max=N, krok=5):
    assert isinstance(przedzialy, list), "Podany obiekt nie jest listą."
    wypisz_os(x_max, krok)
    for i in range(len(przedzialy)):
        if not (isinstance(przedzialy[i], tuple) or isinstance(przedzialy[i], list)):
            print(f'Przedział {i} nie jest listą/krotką.')
        elif len(przedzialy[i]) != 2:
            print(f'Przedział {i} nie ma długości 2.')
        elif not (0 <= przedzialy[i][0] < przedzialy[i][1] <= x_max):
            print(f'Nieprawidłowe końce przedziału: "{przedzialy[i]}"')
        else:
            a, b = przedzialy[i]
            print(' ' * a + '#' * (b - a + 1) + ' ' * (x_max - b), end='')
            print(f' [{a:2d}, {b:2d}], dlugosc={b - a + 1}')
def kurczenie(przedzialy, k, d):
    wynik = []
    for i in range(len(przedzialy)):
        a, b = przedzialy[i]
        x = a + k
        y = b - k
        if y-x+1 >= d:
            wynik.append((x,y))
    return wynik
def odleglosc(p1, p2):
    a, b = p1
    c, d = p2
    if c < b:
        return 0
    else:
        odl = c - b
        return odl
def znajdz_bliskie(lista_p, k):
    wynik = []
    for i in range(len(lista_p)):
        a, b = lista_p[i]
        przedzial = a, b
        u = []
        for j in range(len(lista_p)):
            c, d = lista_p[j]
            przedzial2 = c, d
            if przedzial == przedzial2:
                continue
            odl = odleglosc(przedzial, przedzial2)
            if 0 <odl <=k:
                z = True
                for l in range(len(wynik)):
                    if wynik == []:
                        break
                    e,f,g = wynik[l]
                    if (e == przedzial and f ==  przedzial2) or (f == przedzial and e == przedzial2):
                        z= False
                        break
                if z:
                    u.append((przedzial))
                    u.append((przedzial2))
                    u.append(odl)
                    wynik.append(u)
                    break
                else:
                    continue
    return wynik
def wypisz_podzielone_przedzialy(lista_w):
    for i in range(len(lista_w)):
        a, b, c = lista_w[i]
        przedzial = [a,b]
        wypisz_przedzialy(przedzial, N)
def main():
    wypisz_przedzialy(PRZYKLADOWE_DANE, N)
    kurcz_liste = kurczenie(PRZYKLADOWE_DANE, 2,3)
    wypisz_przedzialy(kurcz_liste)
    print(odleglosc((5, 10), (13, 15)),
    odleglosc((5, 10), (11, 15)),
    odleglosc((5, 10), (10, 15)),
    odleglosc((5, 10), (7, 15)))
    podzialy = znajdz_bliskie(PRZYKLADOWE_DANE, 3)
    print(znajdz_bliskie(PRZYKLADOWE_DANE, 3))
    wypisz_podzielone_przedzialy(podzialy)
if __name__ == '__main__':
    main()