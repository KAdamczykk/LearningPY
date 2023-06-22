def main():
    n=int(input("Podaj liczbe dni "))
    if n <=6:
        raise ValueError("Liczba dni ma być większa od 6")
    t= int(input("Podaj liczbe ton"))
    if t<=0 and t%2==1:
        raise ValueError("t musi być liczbą parzystą, dodatnią")
    cena_m1 = 0
    cena_m2 = 0
    zakup = 0
    sprzedaz = 0
    magazyn = 0
    dochod_nowy =0
    dochod_stary = 0

    for i in range (1,n+1):
        cena_hurtowa = int(input(f"Podaj wartość ceny w dniu {i}"))
        if cena_hurtowa<=0:
            raise  ValueError("Zła wartość ceny")
        if i ==1:
            cena_m1 = cena_hurtowa
            zakup = t/2
            magazyn += zakup
            sprzedaz = t/2
            magazyn -= sprzedaz
            dochod_nowy+= round(sprzedaz*cena_hurtowa*1.15 - zakup*cena_hurtowa,2)
            dochod_stary+=round(t*cena_hurtowa*1.15-t*cena_hurtowa, 2)
            print(f"Nowy model: kupiono {zakup} ton cukru \n Nowy model: sprzedano: {sprzedaz} ton cukru")
            print(f"Nowy model: w magazynie zostało {magazyn} ton cukru \n Nowy model: dochód {dochod_nowy} \n Stary model{dochod_stary}")
        if i ==2:
            cena_m2 = cena_m1
            cena_m1 = cena_hurtowa
            zakup = t / 2
            magazyn += zakup
            sprzedaz = t / 2
            magazyn -= sprzedaz
            dochod_nowy += round(sprzedaz * cena_hurtowa * 1.15 - zakup * cena_hurtowa, 2)
            dochod_stary += round(t * cena_hurtowa * 1.15 - t * cena_hurtowa, 2)
            print(f"Nowy model: kupiono {zakup} ton cukru \n Nowy model: sprzedano: {sprzedaz} ton cukru")
            print(
                f"Nowy model: w magazynie zostało {magazyn} ton cukru \n Nowy model: dochód {dochod_nowy} \n Stary model{dochod_stary}")
        if i>=3 and i <n:
            if cena_m2>cena_m1>cena_hurtowa:
                zakup = 2*t
                if magazyn + zakup>5*t:
                    zakup = t/2
                    magazyn += zakup

                else:
                    magazyn += zakup
                sprzedaz = t / 2
                magazyn -= sprzedaz

                dochod_nowy += round(sprzedaz * cena_hurtowa * 1.15 - zakup * cena_hurtowa, 2)
                dochod_stary += round(t * cena_hurtowa * 1.15 - t * cena_hurtowa, 2)
                print(f"Nowy model: kupiono {zakup} ton cukru \n Nowy model: sprzedano: {sprzedaz} ton cukru")
                print(
                    f"Nowy model: w magazynie zostało {magazyn} ton cukru \n Nowy model: dochód {dochod_nowy} \n Stary model{dochod_stary}")
            elif cena_m2<cena_m1<cena_hurtowa:
                zakup = t/2
                magazyn += zakup

                p= (cena_hurtowa-cena_m2)/(cena_m2*5*t)
                sprzedaz = t / 2 + p
                if magazyn - sprzedaz <0:
                    sprzedaz = t/2
                    magazyn -=sprzedaz
                else:
                    magazyn -= sprzedaz
                dochod_nowy += round(sprzedaz * cena_hurtowa * 1.15 - zakup * cena_hurtowa, 2)
                dochod_stary += round(t * cena_hurtowa * 1.15 - t * cena_hurtowa, 2)
                print(f"Nowy model: kupiono {zakup} ton cukru \n Nowy model: sprzedano: {sprzedaz} ton cukru")
                print(
                    f"Nowy model: w magazynie zostało {magazyn} ton cukru \n Nowy model: dochód {dochod_nowy} \n Stary model{dochod_stary}")
            else:
                zakup = t/2

                if magazyn + zakup > 5 * t:
                    zakup = t / 2
                    magazyn += zakup

                else:
                    magazyn += zakup
                sprzedaz = t / 2
                magazyn -= sprzedaz

                sprzedaz = t / 2

                dochod_nowy += round(sprzedaz * cena_hurtowa * 1.15 - zakup * cena_hurtowa, 2)
                dochod_stary += round(t * cena_hurtowa * 1.15 - t * cena_hurtowa, 2)
                print(f"Nowy model: kupiono {zakup} ton cukru \n Nowy model: sprzedano: {sprzedaz} ton cukru")
                print(
                    f"Nowy model: w magazynie zostało {magazyn} ton cukru \n Nowy model: dochód {dochod_nowy} \n Stary model{dochod_stary}")
            cena_m2 = cena_m1
            cena_m1 = cena_hurtowa
        if i ==n:

            if cena_m2 > cena_m1 > cena_hurtowa:
                zakup = 2 * t
                if magazyn + zakup > 5 * t:
                    zakup = t / 2
                    magazyn += zakup

                else:
                    magazyn += zakup
                sprzedaz = t / 2
                magazyn -= sprzedaz

                dochod_nowy += round(sprzedaz * cena_hurtowa * 1.15 - zakup * cena_hurtowa + cena_hurtowa*magazyn*1.15, 2)
                dochod_stary += round(t * cena_hurtowa * 1.15 - t * cena_hurtowa, 2)
                print(f"Nowy model: kupiono {zakup} ton cukru \n Nowy model: sprzedano: {sprzedaz} ton cukru")
                print(
                    f"Nowy model: z magazynu sprzedano {magazyn} ton cukru \n Nowy model: dochód {dochod_nowy} \n Stary model{dochod_stary}")
            elif cena_m2 < cena_m1 < cena_hurtowa:
                zakup = t / 2
                magazyn += zakup

                p = (cena_hurtowa - cena_m2) / (cena_m2 * 5 * t)
                sprzedaz = t / 2 + p
                if magazyn - sprzedaz < 0:
                    sprzedaz = t / 2
                    magazyn -= sprzedaz
                else:
                    magazyn -= sprzedaz
                dochod_nowy += round(sprzedaz * cena_hurtowa * 1.15 - zakup * cena_hurtowa + cena_hurtowa*magazyn*1.15, 2)
                dochod_stary += round(t * cena_hurtowa * 1.15 - t * cena_hurtowa, 2)
                print(f"Nowy model: kupiono {zakup} ton cukru \n Nowy model: sprzedano: {sprzedaz} ton cukru")
                print(
                    f"Nowy model: z magazynu sprzedano {magazyn} ton cukru \n Nowy model: dochód {dochod_nowy} \n Stary model{dochod_stary}")
            else:
                zakup = t / 2

                if magazyn + zakup > 5 * t:
                    zakup = t / 2
                    magazyn += zakup

                else:
                    magazyn += zakup
                sprzedaz = t / 2
                magazyn -= sprzedaz

                sprzedaz = t / 2

                dochod_nowy += round(sprzedaz * cena_hurtowa * 1.15 - zakup * cena_hurtowa+ cena_hurtowa*magazyn*1.15, 2)
                dochod_stary += round(t * cena_hurtowa * 1.15 - t * cena_hurtowa, 2)
                print(f"Nowy model: kupiono {zakup} ton cukru \n Nowy model: sprzedano: {sprzedaz} ton cukru")
                print(
                    f"Nowy model: z magazynu sprzedano {magazyn} ton cukru \n Nowy model: dochód {dochod_nowy} \n Stary model{dochod_stary}")
    print(f"Całkowity dochód nowego modelu {dochod_nowy}, a starego {dochod_stary}")
    if dochod_nowy>dochod_stary:
        print(f"Nowy system był wydajnieszy o {dochod_nowy-dochod_stary} zł")
    elif dochod_nowy<dochod_stary:
        print(f"Stary system był wydajnieszy o {dochod_stary-dochod_nowy} zł")
    elif dochod_nowy==dochod_stary:
        print(f"Nowy system był tak samo wydajny jak stary")















if "__main__" == __name__:
    main()