def podaj():
    k = int(input("Podaj maksymalny element multizbioru "))
    if k<=0:
        raise ValueError
    multizbior = [None]*k
    for i in range (len(multizbior)):
        x = int(input(f"Podaj liczebność liczby {i} "))
        multizbior[i]=x
    return multizbior
def lista(multizbior):
    lista = []
    for i in range (len(multizbior)):
        lista += [i]*multizbior[i]
    return lista
def dodaj(zbior, element):
    if element<len(zbior):
        zbior[element] +=1
        return zbior
    else:
        nowy_zbior = [0]*(element+1)
        for i in range (len(nowy_zbior)):
            if i<len(zbior):
                nowy_zbior[i]= zbior[i]
            else:
                nowy_zbior[element]=1
                return nowy_zbior
def przeciecie(zbiorA,zbiorB):
    mniejszy_zbior = min(len(zbiorA),len(zbiorB))
    przeciety = []
    for i in range(mniejszy_zbior):
        przeciety += [min(zbiorA[i], zbiorB[i])]
        #wyrzuc zera jeszcze
    return przeciety
def roznica(zbior_a,zbior_b):
    roznica = []
    mniejszy_zbior = min(len(zbior_a),len(zbior_b))
    for i in range (mniejszy_zbior):
        if zbior_a[i]>zbior_b[i]:
            roznica += [(zbior_a[i]-zbior_b[i])]
        else:
            roznica+=[0]
            #wyrzuc zera jeszcze
    return roznica
def main():
    #multizbior = podaj()
    multizbior = [0,3,0,3]
    print(multizbior)
    wylistowany_multizbior = lista(multizbior)
    print(wylistowany_multizbior)
    multizbior_po_dodaniu = dodaj(multizbior, 5)
    nowy_zbior = lista(multizbior_po_dodaniu)
    print(nowy_zbior)
    zbior_a = [0,3,0,4,0,1]
    zbior_b = [1,2,2,4,1]
    print(przeciecie(zbior_a,zbior_b))
    print(roznica(zbior_a,zbior_b))
if __name__ == "__main__":
    main()