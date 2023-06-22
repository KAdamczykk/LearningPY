def pomocnicza(wiersz):
    dlugosc =   len(wiersz)+2
    nowy_wiersz = [None]*dlugosc
    j=2
    for i in range (len(nowy_wiersz)):
        if i == 0:
            nowy_wiersz[i] = wiersz[j-2]
        elif i == 1:
            nowy_wiersz[i] = wiersz[j-2]+wiersz[j-1]
        elif i ==  len(nowy_wiersz)-2:
            nowy_wiersz[i] = wiersz[len(wiersz) - 1] + wiersz[len(wiersz) - 2]
        elif i == len(nowy_wiersz)-1:
            nowy_wiersz[i] = wiersz[len(wiersz)-1]
        else:
            nowy_wiersz[i] = wiersz[j-2]+wiersz[j-1]+wiersz[j]
            if j <len(wiersz)-1:
                j+=1
    return nowy_wiersz
def glowna(a,b,c,d,n):
    wiersz1 = [a]
    wiersz2 = [b,c,d]
    if n <1:
        raise ValueError
    elif n==1:
        return wiersz1
    elif n ==2:
        return wiersz2
    else:
        wiersz_i = wiersz2
        for i in range (3, n+1):
            wiersz_i_plus_1 = pomocnicza(wiersz_i)
            wiersz_i = wiersz_i_plus_1
        return wiersz_i_plus_1


def main():
   a=1
   b=1
   c=1
   d=1
   n=5
   print(glowna(a,b,c,d,n))
if __name__ == "__main__":
     main()