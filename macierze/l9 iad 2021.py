import csv
def wczytaj_dane(sciezka):
    M = []
    f = open(sciezka)
    for row in csv.reader(f):
        for i in range(len(row)):
            row[i] = int(row[i]) # konwersja z str na int
        list.append(M, row) # == A.append(row)
    f.close()
    return M
def wypisz(dane):
    kolumny = len(dane[0])
    wiersze = len(dane)
    for i in range (-1, wiersze):
        for j in range(-1, kolumny):
            if i == - 1:
                if j ==-1:
                    print("   ", end=" ")
                elif j==kolumny-1:
                    print(f"{j}")
                else:
                    print(f"{j}", end = " ")
            else:
                if j ==-1:
                    print(f"{i}:", end="  ")
                elif j == kolumny-1:
                    print(f"{dane[i][j]}")
                else:
                    print(f"{dane[i][j]}", end=" ")
def szukaj_bezpiecznych_danych(dane, lista):
    kolumny = len(dane[0])
    wiersze = len(dane)
    counter = 0
    for i in range(wiersze):
        for j in range(kolumny):
            z =True
            if not j in lista:
                continue
            else:
                if dane[i][j]==1:
                    z= False
                    break
        if z:
           counter+=1
    wynikowa = [None]*counter
    k=0
    for i in range(wiersze):
        for j in range(kolumny):
            z =True
            if not j in lista:
                continue
            else:
                if dane[i][j]==1:
                    z= False
                    break
        if z:
           wynikowa[k] =i
           if k<len(wynikowa):
                k+=1

    return wynikowa
def dodaj_nowe_danie(dane, lista):
    kolumny = len(dane[0])
    wiersze = len(dane)+1
    M = [[0]*kolumny for a in range(wiersze)]
    k=0
    for i in range(wiersze):
        for j in range(kolumny):
            if i == wiersze-1:
                if j in lista:
                    M[i][j]=1
                else:
                    M[i][j]=0
            else:
                M[i][j]=dane[i][j]
    return M
def usun_najgorsze(dane, k):
    kolumny = len(dane[0])
    wiersze = len(dane)
    counter=0
    for i in range(wiersze):
        suma = 0
        for j in range(kolumny):
            suma+=dane[i][j]
        if suma>=k:
            continue
        else:
            counter+=1
    wynikowa= [[0]*kolumny for a in range(counter)]
    t=0
    for i in range(wiersze):
        suma = 0
        for j in range(kolumny):
            suma+=dane[i][j]
        if suma>=k:
            continue
        else:
            for z in range(kolumny):
                wynikowa[t][z] = dane[i][z]
            if t<counter-1:
                t+=1
    return wynikowa
def zapisz_informacje(dane,sciezka):
    kolumny = len(dane[0])
    wiersze = len(dane)
    max_suma = 0
    for i in range(wiersze):
        suma = 0
        for j in range(kolumny):
            suma+=dane[i][j]
        if suma>max_suma:
            max_suma = suma
    liczba_dan_al = [0]*(max_suma+1)
    for i in range(wiersze):
        suma = 0
        for j in range(kolumny):
            suma+=dane[i][j]
        liczba_dan_al[suma] += 1
    with open(sciezka, "w") as file:
        file.write(f"Liczba dań: {wiersze} \n")
        file.write(f"Max liczba alergenow w daniu: {max_suma} \n")
        for k in range(max_suma+1):
            file.write(f"liczba dan z {k} alergenami: {liczba_dan_al[k]} \n")

def main():
    M = wczytaj_dane("alerg.csv")
    print(M)
    wypisz(M)
    print(szukaj_bezpiecznych_danych(M, [0,5,10]))
    dane = dodaj_nowe_danie(M,[1,2,3,8] )
    wypisz(dane)
    usuniete = usun_najgorsze(dane, 5)
    wypisz(usuniete)
    zapisz_informacje(usuniete, "zapis-alergeny.txt")
if __name__ == '__main__':
    main()

