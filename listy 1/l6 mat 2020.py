import random
def losuj_liste(p):
    i = 0
    lista = [2*random.randint(5,20) for i in range (p)]
    return lista
def rzucaj(lista, nr):
    l = lista[nr]
    losy = [None]*l
    for i in range(len(losy)):
        k = random.randint(1,6)
        losy[i] = k
    return losy
def oblicz_kroki(rzuty):
    ilosc_krokow = 0
    for i in range(len(rzuty)):
        if rzuty[i]%2==0:
            ilosc_krokow+=rzuty[i]
        if i ==1 and rzuty[i]%2==1:
            ilosc_krokow-=rzuty[i]
        elif rzuty[i]%2==1 and rzuty[i-1]%2 == 1:
            k = random.randint(1,6)
            if k%2==0:
                ilosc_krokow+=k
            else:
                ilosc_krokow-=k
    return ilosc_krokow
def sprawdz(ilosc_krokow, n ):
    if ilosc_krokow >= n:
        return True
    else:
        return  False
def main():
    random.seed(9876)
    n = 30
    p = 12
    nr = 0
    lista_bool = [None]*p
    lista_krokow = [None]*p
    while nr <p:
        print(f"Proba nr {nr+1}")
        ilosci_rzutow = losuj_liste(p)
        rzuty = rzucaj(ilosci_rzutow, nr)
        print(f"Rzuty {rzuty}")
        ilosc_krokow = oblicz_kroki(rzuty)
        print(f"Wykonując {ilosci_rzutow[nr]} rzutów udało się wykonać {ilosc_krokow} kroków, pozostało{n-ilosc_krokow}")
        lista_bool[nr] = sprawdz(ilosc_krokow, n)
        lista_krokow[nr] = ilosc_krokow
        nr+=1
    print(f"W próbach {nr} otrzymano \n {lista_krokow} \n {lista_bool}")

if __name__ == "__main__":
     main()