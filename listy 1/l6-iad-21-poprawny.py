import random
def losuj_litery(dlugosc):
    lista = [None]*dlugosc
    for i in range (len(lista)):
        liczba = random.randint(97, 122)
        litera = chr(liczba)
        lista[i] = litera
    return lista
def polacz_ze_zwijaniem(pierwsza, druga):
    size_A = len(pierwsza)
    size_B = len(druga)
    nowa_dlugosc = 2 * max(size_A, size_B)
    polowa_dlugosci = nowa_dlugosc//2
    nowa_lista_A = [None]*polowa_dlugosci
    nowa_lista_B = [None]*polowa_dlugosci
    k=0
    l=0
    for  i in range (len(nowa_lista_A)):
        if k > len(pierwsza)-1:
            k=0
        nowa_lista_A[i]= pierwsza[k]
        k+=1
    for j in range (len(nowa_lista_B)):
        if l > len(druga)-1:
            l=0
        nowa_lista_B[j]= druga[l]
        l+=1
    nowa_lista = nowa_lista_A+nowa_lista_B
    return nowa_lista
def odwroc(lista, indeks_poczatku, indeks_konca):
    print("[", end="")
    k=0
    for i in range (len(lista)):
        if i <indeks_poczatku:
            print(f"'{lista[i]}',", end=" ")
        elif indeks_poczatku <= i <= indeks_konca:
            indeks = indeks_konca-k
            print(f"'{lista[indeks]}',", end=" ")
            k+=1
        else:
            if i == len(lista)-1:
                print(f"'{lista[i]}'", end="")
            else:
                print(f"'{lista[i]}',", end=" ")
    print("]")
def przesun_w_lewo(lista, wartosc):
    print("[", end="")
    for i in range(wartosc, len(lista)):
        print(f"'{lista[i]}',", end=" ")
    for j in range(wartosc):
        if j == wartosc - 1:
            print(f"'{lista[j]}'", end="")
        else:
            print(f"'{lista[j]}',", end=" ")
    print("]")
def mod26(tab):
    for k in range(len(tab)):
        if k == 0:
            stare = tab[k]
            x = ord(tab[k])
            y = ord(tab[k + 1])
            z = (x + y) % 26
            nowy = chr(97 + z)
            tab[k] = nowy
        elif k == len(tab) - 1:
            x = ord(tab[k])
            w = ord(stare)
            z = (x + w) % 26
            nowy = chr(97 + z)
            tab[k] = nowy
        else:
            w = ord(stare)
            x = ord(tab[k])
            y = ord(tab[k + 1])
            z = (w + x + y) % 26
            nowy = chr(97 + z)
            stare = tab[k]
            tab[k] = nowy
    return tab

def main():
    random.seed(2014)
    dlugosc_bazowa = int(input("Podaj długość bazową od 5 do 15 "))
    if dlugosc_bazowa<5 or dlugosc_bazowa>15:
        raise  ValueError
    wylosowana_lista_A = losuj_litery(dlugosc_bazowa)
    print(f"Wylosowano: {wylosowana_lista_A}")
    dlugosc_drugiej = int(input("Podaj dlugosc drugą od 5 do 15 "))
    if dlugosc_drugiej<5 or dlugosc_drugiej>15:
        raise  ValueError
    wylosowana_lista_B = losuj_litery(dlugosc_drugiej)
    print(f"Wylosowano: {wylosowana_lista_B}")
    suma_list = polacz_ze_zwijaniem(wylosowana_lista_A,wylosowana_lista_B)
    print(suma_list)
    odwroc(suma_list, 2,5)
    przesun_w_lewo(wylosowana_lista_A, 3)
    m = ['a', 'b', 'c', 'd']
    print(f"Lista przed mod26: {m}")
    mod26(m)
    print(m)
if __name__ == "__main__":
    main()