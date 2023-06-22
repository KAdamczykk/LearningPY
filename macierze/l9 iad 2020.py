import random


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
def losuj_miny(plansza, liczba_min):
    wiersze = len(plansza)
    kolumny = len(plansza[0])
    for k in range(liczba_min):
        wart_i = random.randint(0,wiersze-1)
        wart_j = random.randint(0, kolumny-1)
        plansza[wart_i][wart_j] = 9
    return plansza
def wypisz_macierz_cenzura(plansza, cenzura):
    wynikowa = [['*']* len(plansza[0]) for a in range(len(plansza))]
    for i in range(len(plansza)):
        for j in range (len(plansza[0])):
            if cenzura[i][j] == True:
                wynikowa[i][j] = plansza[i][j]
    return  wynikowa
def odkryj_pole(plansza, cenzura, wiersz, kolumna):
    assert 0<=wiersz<=len(plansza)-1
    assert 0<=wiersz<=len(plansza[0])-1
    if plansza[wiersz][kolumna] == 9:
        return False
    else:
        cenzura[wiersz][kolumna] = True
        return True
def numery_przy_minach(plansza):
    wiersze= len(plansza)
    kolumny = len(plansza[0])
    for i in range (wiersze):
        for j in range (kolumny):
            if plansza[i][j]==9:
                    continue
            elif i ==0 and j==0:
                if plansza[i+1][j]==9:
                    plansza[i][j]+=1
                if plansza[i+1][j+1]==9:
                    plansza[i][j]+=1
                if plansza[i][j+1]==9:
                    plansza[i][j]+=1
            elif i ==0 and j ==kolumny-1:
                if plansza[i+1][j]==9:
                    plansza[i][j]+=1
                if plansza[i][j-1] == 9:
                    plansza[i][j] += 1
                if plansza[i+1][j-1]==9:
                    plansza[i][j]+=1
            elif i ==0:
                if plansza[i][j-1]==9:
                    plansza[i][j]+=1
                if plansza[i][j+1]==9:
                    plansza[i][j]+=1
                if plansza[i+1][j-1]==9:
                    plansza[i][j]+=1
                if plansza[i+1][j]==9:
                    plansza[i][j]+=1
                if plansza[i+1][j+1]==9:
                    plansza[i][j]+=1
            elif i == wiersze-1 and j==0:
                if plansza[i][j+1]==9:
                    plansza[i][j]+=1
                if plansza[i-1][j]==9:
                    plansza[i][j]+=1
                if plansza[i-1][j+1]==9:
                    plansza[i][j]+=1
            elif i == wiersze-1 and j == kolumny-1:
                if plansza[i][j-1]==9:
                    plansza[i][j]+=1
                if plansza[i-1][j-1]==9:
                    plansza[i][j]+=1
                if plansza[i-1][j]==9:
                    plansza[i][j]+=1
            elif i == wiersze-1:
                if plansza[i][j-1]==9:
                    plansza[i][j]+=1
                if plansza[i][j+1]==9:
                    plansza[i][j]+=1
                if plansza[i-1][j-1]==9:
                    plansza[i][j]+=1
                if plansza[i-1][j+1]==9:
                    plansza[i][j]+=1
                if plansza[i-1][j]==9:
                    plansza[i][j]+=1
            elif j==0:
                if plansza[i+1][j]==9:
                    plansza[i][j]+=1
                if plansza[i-1][j]==9:
                    plansza[i][j]+=1
                if plansza[i+1][j+1]==9:
                    plansza[i][j]+=1
                if plansza[i][j+1]==9:
                    plansza[i][j]+=1
                if plansza[i-1][j+1]==9:
                    plansza[i][j]+=1
            elif j == kolumny-1:
                if plansza[i + 1][j] == 9:
                    plansza[i][j] += 1
                if plansza[i - 1][j] == 9:
                    plansza[i][j] += 1
                if plansza[i + 1][j - 1] == 9:
                    plansza[i][j] += 1
                if plansza[i][j - 1] == 9:
                    plansza[i][j] += 1
                if plansza[i - 1][j - 1] == 9:
                    plansza[i][j] += 1
            else:
                if plansza[i + 1][j+1] == 9:
                    plansza[i][j] += 1
                if plansza[i+1][j] == 9:
                    plansza[i][j] += 1
                if plansza[i + 1][j - 1] == 9:
                    plansza[i][j] += 1
                if plansza[i][j + 1] == 9:
                    plansza[i][j] += 1
                if plansza[i][j - 1] == 9:
                    plansza[i][j] += 1
                if plansza[i-1][j - 1] == 9:
                    plansza[i][j] += 1
                if plansza[i-1][j] == 9:
                    plansza[i][j] += 1
                if plansza[i-1][j + 1] == 9:
                    plansza[i][j] += 1
    return plansza
def main():
    M = [[0]*15 for i in range(10)]
    cenzura = [[False]* 15 for j in range(10)]
    wypisz_macierz(wypisz_macierz_cenzura(M, cenzura))
    plansza = numery_przy_minach(M)
    for i in range(0,100):
        wiersz = int(input('Podaj wiersz '))
        kolumna = int(input('Podaj kolumne '))
        k = odkryj_pole(M, cenzura, wiersz, kolumna)
        if k ==False:
            print("Przegrałeś")
            break
        else:
            wypisz_macierz(wypisz_macierz_cenzura(M, cenzura))
if __name__ == '__main__':
    main()

