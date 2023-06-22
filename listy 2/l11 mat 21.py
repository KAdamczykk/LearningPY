import csv
def wczytaj_csv(nazwa_pliku):
    """ funkcja wczytuje dane z pliku .csv """
    data = []
    with open(nazwa_pliku) as f:
        for row in csv.reader(f):
            data.append([float(row[i]) if i == 0 else row[i]
                                          for i in range(len(row))])
    return data
def sprawdz_poprawnosc(y):
    if y == []:
        return False
    dlugosc_osobnej_listy = len(y[0])
    for i in range (len(y)):
        if not type(y[i]) is list:
            return False
        dlugosc_listy = len(y[i])
        if dlugosc_listy != dlugosc_osobnej_listy:
            return False
    for j in range(len(y[0])):
        for k in range(len(y)):
            if k == 0:
                base_type = type(y[k][j])
            else:
                x = type(y[k][j])
                if not x == base_type:
                    return False
    return True
def kategorie(y,i):
    m = len(y[0])
    assert 0 <= i < m
    if not type(y[0][i]) is str:
       raise Exception
    unikatowa = []
    for j in range(len(y)):
        x = y[j][i]
        if not x in unikatowa:
            unikatowa.append(x)
    return unikatowa
def grupuj(y,by):
    unikat = kategorie(y,by)
    ilosc_wart_unikatowych = len(unikat)
    wynik = []
    for i in range (ilosc_wart_unikatowych):
        u = []
        x = None
        p = None
        f = True
        for j in range(len(y)):
            x = y[j][by]
            for r in range(len(wynik)):
                if x in wynik[r]:
                    continue
                else:
                    f = False
                    p=j
                    break
            if not f:
                break
            if len(wynik) == 0:
                p = j
                break
        if x == None or p == None:
            return wynik
        for q in range(p, len(y)):
            if x in y[q]:
                z = []
                for k in range(len(y[0])):
                    z.append(y[q][k])
                u.append(z)
        wynik += u
    return wynik, unikat
def policz(y_grupy, f, i, ind):
    unikat = kategorie(y_grupy,ind)
    start = y_grupy[0][ind]
    wynik = []
    cos = []
    for j in range(len(y_grupy)):
        if y_grupy[j][ind] != start:
            start = y_grupy[j][ind]
            x = f(cos)
            cos = []
            wynik.append(x)
        else:
            cos.append(y_grupy[j][i])
    x = f(cos)
    wynik.append(x)
    return unikat, wynik
def main():
    zbior_danych = wczytaj_csv('tips.csv')
    print(zbior_danych)
    x = [['a', 2.5, 'r', 4.0], ['k', 4.0, 'w', 0.0], ['t', 3.7, 'q', 7.4]]
    print(sprawdz_poprawnosc(zbior_danych))
    print(kategorie(zbior_danych, 2))
    y = [
    [1.01, 'Female', 'No'],
    [1.66, 'Male', 'No'],
    [3.5, 'Male', 'No'],
    [3.31, 'Male', 'No'],
    [3.61, 'Female', 'No'],
    [4.71, 'Male', 'No']
    ]

    print(grupuj(zbior_danych,2))
    a, unikat = grupuj(y,1)
    print(a)
    print(kategorie(a,1))

    print(policz(a, sum, 0, 1))
    b,unikat = grupuj(zbior_danych,3)
    print(b)
    wart, wynik = policz(b, lambda x: sum(x) / len(x), 0, 3)

    print(wart, wynik)
if __name__ == '__main__':
    main()
