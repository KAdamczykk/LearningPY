def hilbert(n):
    hil= [[0]*n for a in range (n)]
    for i in range (n):
        for j in range (n):
            hil[i][j] = 1/(i+j+1)
    return hil
def slad(A):
    suma = 0
    for i in range (len(A)):
        suma += A[i][i]
    return suma
def symetryczna(A):
    for i in range (len(A)):
        for j in range(len(A[0])):
            if A[i][j] != A[j][i]:
                return False
    return True
def mnoz_przez_skal (A, k ):
    for i in range(len(A)):
        for j in range (len(A[0])):
            A[i][j] = k * A[i][j]
    return A
def transpozycja(A):
    wiersze = len(A)
    kolumny = len(A[0])
    tran = [[0]*wiersze for i in range (kolumny)]
    for i in range(wiersze):
        for j in range (kolumny):
            tran[j][i] = A[i][j]
    return tran
def rozszerz_o_kolumne(A,b,i):
    wiersze = len(A)
    kolumny = len(A[0])+1
    B = [[0]*kolumny for a in range (wiersze)]
    for k in range(wiersze):
        for j in range(kolumny):
            if j==i:
                B[k][j] = b[k]
            elif j<i:
                B[k][j] = A[k][j]
            else:
                B[k][j] = A[k][j-1]
    return B
def usun(A,i,j):
    assert 0<=i<len(A)  or 0<=j<len(A[0])
    wiersze = len(A)
    kolumny = len(A[0])
    B = [[0]*(kolumny-1) for a in range (wiersze-1)]
    for k in range(wiersze):
        if k ==i:
            continue
        elif k<i:
            for l in range(kolumny):
                if l<j:
                    B[k][l] = A[k][l]
                elif l==j:
                    continue
                else:
                    B[k][l-1] = A[k][l]
        else:
            for l in range(kolumny):
                if l<j:
                    B[k-1][l] = A[k][l]
                elif l==j:
                    continue
                else:
                    B[k-1][l-1] = A[k][l]
    return B
def suma_w_kolumnie(A):
    suma = 0
    for j in range(1):
        for i in range(len(A)):
            suma += A[i][j]
    return suma
def magiczny(A):
    wiersze = len(A)
    kolumny = len(A[0])
    assert wiersze == kolumny
    suma = 0
    for j in range(kolumny):
        suma+=A[0][j]
    for i in range(1, wiersze):
        suma_k = 0
        for j in range(kolumny):
            suma_k += A[i][j]
        if suma_k!=suma:
            return False
    for j in range(kolumny):
        suma_k = 0
        for i in range (wiersze):
            suma_k += A[i][j]
        if suma_k!=suma:
            return False
    suma_k=0
    for i in range(wiersze):
        suma_k += A[i][i]
    if suma_k!=suma:
        return False
    j = kolumny-1
    suma_k = 0
    for i in range(wiersze):
        suma_k +=A[i][j]
        j-=1
    if suma_k!= suma:
        return False
    return True
def srednia(A):
    wiersze = len(A)
    kolumny = len(A[0])
    s= [0]*kolumny
    for j in range(kolumny):
        suma=0
        for i in range(wiersze):
            suma+=A[i][j]
        srednia = suma/wiersze
        s[j] = srednia
    return s
def srednia_nie_ujm_kol(A):
    wiersze = len(A)
    kolumny = len(A[0])
    B = [[] for a in range(wiersze)]
    for j in range(kolumny):
        suma= 0
        for i in range(wiersze):
            suma+=A[i][j]
        srednia = suma/wiersze
        if srednia<0:
            continue
        else:
            for i in range(wiersze):
                B[i].append(  A[i][j])
    return B
def srednia(A,j):
    suma = 0
    for i in range(len(A)):
        suma+=A[i][j]
    srednia = suma/len(A)
    return srednia

def sortowanie_po_kol(A):
    wiersze = len(A)
    kolumny = len(A[0])
    for j in range(1,kolumny):
        for k in range(kolumny - j):
            if not srednia(A,k) <= srednia(A, k+1):
                for i in range(wiersze):
                    A[i][k], A[i][k+1] = A[i][k+1], A[i][k]
    return A
def main():
    macierz_kwad = [[1,2,3], [4,5,6], [7,8,9]]
    macierz = [[-1,2,3],[4,-5,6], [7,-8,-9], [-10,-11,12]]
    #print(hilbert(3))
    #print(slad(macierz_kwad))
    #print(symetryczna(macierz_kwad))
    #print(transpozycja(macierz))
    lista = [0,0,0,0]
    #print(rozszerz_o_kolumne(macierz, lista, 2))
    #print(usun(macierz, 1,2))
    #print(suma_w_kolumnie(macierz))
    jedynkowo= [[1,1,1],[1,1,1], [1,1,1]]
    #print(magiczny(jedynkowo))
    #print(srednia(macierz_kwad))
    #print(srednia_nie_ujm_kol( macierz))
    print(sortowanie_po_kol(macierz))
if __name__ == '__main__':
    main()

