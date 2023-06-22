def wczytaj(sciezka):
    l =[]
    with open(sciezka, "r") as f:
        for linia in f:
            a = int(linia)
            if a>=0:
                l.append(a)
    return l
def sprawdz_poprawnosc(y):
    if not type(y) is list:
        return False
    if y ==[]:
        return False
    for i in range(len(y)):
        if y[i]<0:
            return False
    return True
def podziel(y):
    pomocnicza = []
    wynik = []
    for i in range (len(y)):
        if i ==0:
            pomocnicza.append(y[i])
        elif y[i-1]<y[i]:
            pomocnicza.append(y[i])
        else:
            wynik.append(pomocnicza)
            pomocnicza = [y[i]]
            if i == len(y) - 1:
                wynik.append(pomocnicza)
    return wynik
def wypisz(x):
    for i in range (len(x)):
        j =0
        print(f'x{i}:', end="  ")
        while j < len(x[i])-1:
            print(f'{x[i][j]}', end= "  ")
            j+=1
        if j == len(x[i])-1:
            print(f'{x[i][j]}')

def zlacz_posortowane(x):
    nowa = []
    for i in range (len(x)):
        for j in range (len(x[i])):
            nowa.append(x[i][j])
    nowwa = sorted(nowa)
    return nowwa
def main():
    sciezka = "dane.txt"
    m = wczytaj(sciezka)
    print(m)
    lista1 =[]
    k = 0
    print(sprawdz_poprawnosc(lista1), sprawdz_poprawnosc(m), sprawdz_poprawnosc(k))
    print(podziel([1, 2, 1, 3, 4, 2, 4, 6, 8, 1, 0]))
    print(podziel(m))
    z = podziel([1, 2, 1, 3, 4, 2, 4, 6, 8, 1, 0])

    wypisz(z)
    print(zlacz_posortowane(z))
if __name__ == '__main__':
    main()
