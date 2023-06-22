import math
import matplotlib.pyplot as plt
import copy
def trzeci_punkt_trojkata_rownobocznego(p1, p2):
    odleglosc = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    srodek = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
    kat = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
    wynik_x = srodek[0] - odleglosc * 3 ** 0.5 / 2 * math.sin(kat)
    wynik_y = srodek[1] + odleglosc * 3 ** 0.5 / 2 * math.cos(kat)
    return wynik_x, wynik_y
def odleglosc_euklidesowa(x1,x2,y1,y2):
    odl_x = x2 - x1
    odl_y = y2 - y1
    #nowe wspolrzedzne
    nowy_wektor1x = odl_x/3
    nowy_wektor1y = odl_y/3
    ny1 = y1 + nowy_wektor1y
    nx1 = x1 + nowy_wektor1x
    ny2 = y2 - nowy_wektor1y
    nx2 = x2 - nowy_wektor1x
    wynik = [nx1, ny1], [nx2, ny2]
    return wynik

def kolejna_iteracja(lista):
    wynik = []
    n = len(lista)
    assert n >= 2
    for i in range(n-1):
        assert type(lista[i]) is tuple
        x1, y1 = lista[i]
        x2, y2 = lista[i+1]
        p1, p2  = odleglosc_euklidesowa(x1, x2, y1, y2)

        x3, y3 = trzeci_punkt_trojkata_rownobocznego(p1, p2)
        pn1,pn11 = p1[0], p1[1]
        pn2,pn22 = p2[0], p2[1]
        wynik.append((pn1, pn11))
        wynik.append((x3,y3))
    wynik.append((pn2, pn22))
    return wynik
def narysuj_wielokat(lista_wierzcholkow):
    x = []
    y = []
    for p in lista_wierzcholkow:
        x.append(p[0])
        y.append(p[1])
    x.append(lista_wierzcholkow[0][0])
    y.append(lista_wierzcholkow[0][1])
    plt.axis('equal')
    plt.plot(x, y)
    plt.show()

def platek_sniegu_kocha(d):
    x0_1 = 0
    y0_1 = 0
    x0_2 = d
    y0_2 = 0
    l_wierz = [(x0_1,y0_1), (x0_2,y0_2)]
    counter = 5
    for i in range(2):
        nowa_lista = [None]*counter
        k = 0
        j=0
        if k == 0 and i ==0:
            nowa_lista[j] = l_wierz[k]
            k+=1
        elif k ==0 and i >0:
            nowa_lista[j] = l_wierz[k]
            k += 1
        for j in range (4, counter,6):

            if i == 0:
                nowa_lista[j] = l_wierz[k]
                if k < len(l_wierz) - 1:
                    k+=1
            else:

                if j ==len(nowa_lista) -1:
                    nowa_lista[j] = wynik[k]
                else:
                    nowa_lista[j] = wynik[k]
                    k+=1
                    nowa_lista[j+1] = wynik[k]
                    k+=1
                    nowa_lista[j+2] = wynik[k]
                    k+=1

        if i == 0:
            c = kolejna_iteracja(l_wierz)
        else:
            c = kolejna_iteracja(wynik)

        z = 0
        for l in range(1, len(nowa_lista)):
            if nowa_lista[l-1] != None and nowa_lista[l] == None:
                nowa_lista[l] = c[z]
                if z < len(c) - 1:
                    z+=1
        counter += 6
        wynik = copy.deepcopy(nowa_lista)
    return wynik

def main():
    lista = [(1,1), (3,1)]
    print(kolejna_iteracja(lista))
    po_10_iter = platek_sniegu_kocha(200)
    print(po_10_iter)
    narysuj_wielokat(po_10_iter)
if __name__ == '__main__':
    main()