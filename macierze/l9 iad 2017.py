import csv
import math
def distance(u,v):
    assert len(u) == len(v)
    m = len(v)
    suma = 0
    for i in range(m):
        dzialanie = (u[i]-v[i])**2
        suma+=dzialanie
    wynik = math.sqrt(suma)
    return wynik
def nearest_neighbor_class(A, c, z):
    min_odleglosc = float('inf')
    min_el = None
    for i in range (len(A)):
        odleglosc = distance(A[i],z)
        if odleglosc<min_odleglosc:
            min_odleglosc = odleglosc
            min_el = i
    return c[min_el]
def knn(A,c,Z):
    lista = [None]*(len(Z))
    for i in range(len(Z)):
        wart_i = nearest_neighbor_class(A,c,Z[i])
        lista[i] = wart_i
    return lista
def sprawdz(test, wyn):
    TN = 0
    FP = 0
    FN = 0
    TP = 0
    for i in range(len(test)):
        if test[i] == 0 and wyn[i] == 0:
            TN+=1
        elif test[i] == 0 and wyn[i] ==1:
            FP+=1
        elif test[i] == 1 and wyn[i] == 0:
            FN +=1
        elif test[i] == 1 and wyn[i] == 1:
            TP += 1
    dokladnosc = round((TP + TN)/(TP+TN+FN+FP), 2)
    precyzja = round((TP)/(TP+FP), 2)
    czulosc = round((TP)/(TP+FN), 2)
    miara = round((2*TP)/(2*TP+FN+FP),2)
    return TN, FP, FN, TP, dokladnosc, precyzja, czulosc, miara
def zapisz_do_pliku(sciezka, TN, FP, FN, TP, dokladnosc, precyzja, czulosc, miara):
    with open (sciezka, "w") as f:
        f.write(f"  |   0   |   1  \n")
        f.write("--------------- \n")
        f.write(f"0 |  {TN}   |   {FP}  \n")
        f.write(f"1 |   {FN}   |  {TP}  \n")
        f.write(f"Dokładność: {dokladnosc} \n")
        f.write(f"Precyzja: {precyzja} \n")
        f.write(f"Czułość: {czulosc} \n")
        f.write(f"Miara: {miara}")
def main():
    A = []
    f = open("train_wine.csv", "r")  # r=do odczytu
    for row in csv.reader(f):
        for i in range(len(row)):
            row[i] = float(row[i])  # konwersja z str na float
        list.append(A, row)  # == A.append(row)
    f.close()
    print(A)
    c = []
    with open("train_class.txt","r") as g:
        for j in g:
            k=float(j)
            c+=[k]
    print(c)
    assert len(A[0])==2
    assert len(A)==len(c)
    assert 0 in c or 1 in c
    Z = []
    g = open("test_wine.csv", "r")  # r=do odczytu
    for row in csv.reader(g):
        for j in range(len(row)):
            row[j] = float(row[j])  # konwersja z str na float
        list.append(Z, row)  # == Z.append(row)
    g.close()
    print(Z)
    wyn = knn(A,c,Z)
    test = []
    with open("test_class.txt","r") as h:
        for z in h:
            w=float(z)
            test+=[w]
    print(test)
    TN, FP, FN, TP, dokladnosc, precyzja, czulosc, miara = sprawdz(test, wyn)
    print(TN, FP, FN, TP, dokladnosc, precyzja, czulosc, miara)
    zapisz_do_pliku("dane_wina.txt",TN, FP, FN, TP, dokladnosc, precyzja, czulosc, miara)
if __name__ == '__main__':
    main()

