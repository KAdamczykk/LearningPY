import math
def main():
    ob = int(input(("podaj obwod głowy Zosi")))
    if ob<45 and ob>60:
        raise ValueError
    liczba_rozdzek = int(input("Podaj ilość różdzek"))
    if liczba_rozdzek<=0:
        raise  ValueError
    liczba_patykow =int(input("Podaj liczbe patykow"))
    if liczba_patykow<0:
        raise ValueError
    r_g = ob/(2*math.pi)
    r_w=0.9*r_g
    R_z = 3*r_g
    h=5*r_g
    a=90
    R_t = (a*math.sqrt(3))/6
    if R_z<=R_t:
        print("Tektury wystarczy")
    else:
        print("Tektury nie wystarczy")
    l = math.sqrt(h**2+r_w**2)
    r_wm = r_w/100
    l_m = l/100
    P_b = math.pi*r_wm*l_m
    #trzebaby jeszcze dodać pole pierscieniarazy dwa
    if P_b<=21/110:
        print("Wystarczy farby")
    else:
        print("Nie wystarczy farby")
    dlugosc_patykow =liczba_patykow * 187
    max_dlugosc_rozdzki = round(dlugosc_patykow/liczba_rozdzek, 2)
    if max_dlugosc_rozdzki<19:
        print("nie da się wykonać danej liczby różdżek")
    elif max_dlugosc_rozdzki>25:
        max_dlugosc_rozdzki==25
        print(f"Wystarczy na {liczba_rozdzek} różdżek, max długość {max_dlugosc_rozdzki}")
    else:
        print(f"Da się wykonać {liczba_rozdzek} różdżek, max długość {max_dlugosc_rozdzki}")





if "__main__" == __name__:
    main()