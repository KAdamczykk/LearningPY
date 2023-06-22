def mnozenie_macierzy(a,b):
    assert len(a[0]) == len(b)
    w_a = len(a)
    w_b = len(b)
    k_a = len(a[0])
    k_b  = len(b[0])
    wynik= [[0]*k_b for i in range (w_a)]
    for i in range(w_a):
        for j in range(k_b):
            for k in range(k_a):
                wynik[i][j] += a[i][k]*b[k][j]
    return wynik
def wypisz_macierz(matrix):
    print(" ", end=" ")
    for column in range(len(matrix[0])):
        if column < 10:
            print(column, end=" ")
        else:
            print(chr(ord("A")+column-10), end=" ")
    print()
    for row in range(len(matrix)):
        if row < 10:
            print(row, end=" ")
        else:
            print(chr(ord("A")+row-10), end=" ")
        for column in range(len(matrix[row])):
            print(f'{matrix[row][column]}', end=" ")
        print()
    print()
def main():
    a= [[2,1,1],[3,0,1]]
    b = [[3,1],[2,1],[1,0]]
    k = mnozenie_macierzy(a,b)
    wypisz_macierz(k)
if __name__ == '__main__':
    main()

