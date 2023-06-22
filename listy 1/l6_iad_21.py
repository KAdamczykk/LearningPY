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
    dlugosc_listy = indeks_konca-indeks_poczatku +1
    lista_odwracana = [None]* dlugosc_listy
    lista_odwrotna = [None]* dlugosc_listy
    k= indeks_poczatku
    l = dlugosc_listy-1
    m = indeks_poczatku
    for i in range(len(lista_odwracana)):
        lista_odwracana[i]= lista[k]
        lista_odwrotna[l]=lista_odwracana[i]
        k+=1
        l-=1
    for j in range(len(lista_odwrotna)):
        lista[m] = lista_odwrotna[j]
        m+=1
    return lista

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
    lista_odwrotna = odwroc(suma_list, 2,5)
    print(lista_odwrotna)

if __name__ == "__main__":
    main()