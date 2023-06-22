import csv
def wczytaj_csv():
    studenci = []
    with open("studenci.csv") as f:
        for row in csv.reader(f):
            studenci.append(row)
    return studenci
def zmien_typ(m):
    wiersze = len(m)
    kolumny = len(m[0])
    for i in range (wiersze):
        suma = 0
        counter = 0
        counter_str = 0
        z= True
        for j in range (kolumny):
            if j ==2:
                m[i][j] = int(m[i][j])
            elif j>2 and m[i][j]!='':
                m[i][j] = float(m[i][j])
                suma+=m[i][j]
                counter+=1
            elif j>2 and m[i][j]=='':
                counter_str +=1
                z = False
        if not z:
            for k in range(kolumny):
                if counter_str ==1 and m[i][k]=='':
                    m[i][k] = float(suma/counter)
                elif counter_str>1 and m[i][k]=='':
                    m[i][k] =0.0
    return m
def wypisz(studenci):
    wiersze = len(studenci)
    kolumny = len(studenci[0])
    for i in range (wiersze):
        for j in range (-1, kolumny+1):
            if j==-1:
                print("|", end=" ")
            elif 0<=j<=kolumny-1:
                print(f"{studenci[i][j]}", end=" ")
            elif j == kolumny:
                print("|")
def wyznacz_ocene(punkty):
    assert 0<=punkty<=100
    if punkty<50.5:
        return 2.0
    elif 50.5<=punkty<60.5:
        return 3.0
    elif 60.5<=punkty<70.5:
        return 3.5
    elif 70.5<=punkty<80.5:
        return 4.0
    elif 80.5<=punkty<90.5:
        return 4.5
    else:
        return 5.0
def oceny(studenci):
    wiersze = len(studenci)
    kolumny = len(studenci[0])
    oceny = [[0]*2 for a in range(wiersze)]
    for i in range (wiersze):
        k=0
        suma= 0
        for j in range(2,kolumny):
            if j==2:
                oceny[i][k] = studenci[i][j]
                k+=1
            else:
                suma+=studenci[i][j]
        oceny[i][k] = wyznacz_ocene(suma)
    return oceny
def statystyki(studenci):
    wiersze = len(studenci)
    kolumny = len(studenci[0])
    max_1 = -float('inf')
    max_2 = -float('inf')
    max_3 = -float('inf')
    max_4 = -float('inf')
    max_5 = -float('inf')
    min_1 = float('inf')
    min_2 = float('inf')
    min_3 = float('inf')
    min_4 = float('inf')
    min_5 = float('inf')
    suma_1 = 0
    suma_2 = 0
    suma_3 = 0
    suma_4 = 0
    suma_5 = 0

    for i in range (wiersze):
        for j in range(3,kolumny):
            if j==3:
                if min_1>studenci[i][j]:
                    min_1 = studenci[i][j]
                if max_1<studenci[i][j]:
                    max_1 = studenci[i][j]
                suma_1+=studenci[i][j]
            if j ==4:
                if min_2 > studenci[i][j]:
                    min_2 = studenci[i][j]
                if max_2 < studenci[i][j]:
                    max_2 = studenci[i][j]
                suma_2 += studenci[i][j]
            if j ==5:
                if min_3 > studenci[i][j]:
                    min_3 = studenci[i][j]
                if max_3 < studenci[i][j]:
                    max_3 = studenci[i][j]
                suma_3 += studenci[i][j]
            if j==6:
                if min_4 > studenci[i][j]:
                    min_4 = studenci[i][j]
                if max_4 < studenci[i][j]:
                    max_4 = studenci[i][j]
                suma_4 += studenci[i][j]
            if j ==7:
                if min_5 > studenci[i][j]:
                    min_5 = studenci[i][j]
                if max_5 < studenci[i][j]:
                    max_5 = studenci[i][j]
                suma_5 += studenci[i][j]

    stats = [[1,max_1,min_1,round(suma_1/wiersze, 1)], [2,max_2,min_2,round(suma_2/wiersze, 1)], [3,max_3,min_3,round(suma_3/wiersze, 1)],[4,max_4,min_4,round(suma_4/wiersze, 1)],[5,max_5,min_5,round(suma_5/wiersze, 1)]]
    return stats
def main():
    M = wczytaj_csv()
    print(M)
    modified_m = zmien_typ(M)
    print(modified_m)
    wypisz(modified_m)
    marks = oceny(modified_m)
    print(marks)
    wypisz(marks)
    stats = statystyki(modified_m)
    wypisz(stats)
    
if __name__ == '__main__':
    main()

