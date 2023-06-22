import copy
def znajdz_piwersze_powtorzenie_k(t,k):
    assert len(t)>=2 *k
    pomocnicza1 = [None]*k
    pomocnicza2 = [None] * k
    for i in range(len(t)):
        z = True
        if i < k:
            pomocnicza1[i] = t[i]
        elif k<=i<2*k:
            pomocnicza2[i-k] = t[i]
        else:
            for j in range (k):
                if pomocnicza1[j] != pomocnicza2[j] and i < len(t)-1:
                    z = False
                    pomocnicza1.pop(0)
                    pomocnicza1.append(pomocnicza2[0])
                    pomocnicza2.pop(0)
                    pomocnicza2.append(t[i])
                    break
            if z:
                return pomocnicza1
    return []
def najdluzsze_powtorzenie(t):
    dlugosc_max = 0
    k = len(t)//2
    for x in range(k):
        y = znajdz_piwersze_powtorzenie_k(t,k)
        if y == []:
            continue
        else:
            dlugosc_max = len(y)
    return dlugosc_max
def usun_powtorzenia(t,k):
    x = znajdz_piwersze_powtorzenie_k(t,k)
    if x == []:
        return t
    else:
        nowa = copy.copy(x)
        i = k
        while i< len(t)-1:
            z = True
            for j in range(k):
                if t[i+j] != x[j]:
                    nowa.append(t[i])
                    i+=1
                    z = False
                    break
            if z:
                i+=k
        if not z:
            nowa.append(t[len(t)-1])
    odwr = []
    for m in range (len(x)-1, -1, -1):
        odwr.append(x[m])
    wynik = copy.copy(x)
    n = k
    while n < len(nowa) - 1:
        z = True
        for p in range(k):
            if nowa[n + p] != odwr[p]:
                wynik.append(nowa[n])
                n += 1
                z = False
                break
        if z:
            n += k
    if not z:
        wynik.append(t[len(t) - 1])


    return wynik
def main():
    test = [0, 1, 2, 3, 1, 2, 3, 5, 2, 3, 5]
    print(znajdz_piwersze_powtorzenie_k(test,3))
    test2 = [1, 2, 1, 2, 3, 2, 1, 2, 3]
    print(najdluzsze_powtorzenie(test2))
    test3 =  [1, 2, 3, 4, 1, 2, 3, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1]
    print(usun_powtorzenia(test3, 4))
if __name__ == '__main__':
    main()
