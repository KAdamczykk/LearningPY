def main():
    n=int(input("Podaj liczbe tygodni"))
    if n <=5:
        raise ValueError("Liczba tygodni ma być większa od 5")
    k= int(input("Podaj liczbe worków węgla do kupienia, 1 worek = 100kg"))
    if k<=0:
        raise ValueError
    porownanie = 0
    sum_cen_1 = 0
    sum_cen_2 = 0
    k_kup_1 =0
    k_kup_2 =0
    porownanie1=0
    porownanie2=0
    porownanie_dla2 = 0
    for i in range (1,n+1):
        cena = int(input(f"Podaj cene węgla w tygodniu {i}"))
        if cena <=0:
            raise ValueError
        if i ==1:
            porownanie = cena
            # Pan nr 1
        if i == 2:
            porownanie1 = cena
        if i == 3:
            porownanie2 = cena
        if i > 3:
            if porownanie > porownanie1 > porownanie2 > cena and k_kup_1 < k:
                porownanie = porownanie1
                porownanie1 = porownanie2
                porownanie2 = cena
                if k - k_kup_1 < k / 4:
                    k_kup_1 += k - k_kup_1
                    sum_cen_1 += (k - k_kup_1) * cena
                    print(f"Pan nr 1 zakupił {k - k_kup_1} worków węgla w {i} tygodniu za cene {(k - k_kup_1) * cena} zl")
                k_kup_1 += k / 4
                sum_cen_1 += cena * (k / 4)
                print(f"Pan nr 1 zakupił {k / 4} worów węgla w tygodniu {i} za cene {(k / 4) * cena} zl")

        #Pan nr 2
        if i ==1:
            porownanie_dla2 = cena
        if i == 2:
            if cena < porownanie_dla2 and k_kup_2<k:
                porownanie_dla2 = cena
                k_kup_2 += 2
                sum_cen_2 += 2 * cena
                print(f"Pan nr 2 kupił 2 worki węgla w tygodniu {i}za cene {2 * cena} zł")
        if i == 3:
            if cena < porownanie_dla2 and k_kup_2 < k:
                porownanie_dla2 = cena
                k_kup_2 += 2
                sum_cen_2 += 2 * cena
                print(f"Pan nr 2 kupił 2 worki węgla w tygodniu {i}za cene {2 * cena} zł")
        if i>3:
            if cena < porownanie_dla2 and k_kup_2<k:
                porownanie_dla2 = cena
                if k-k_kup_2==1:
                    k_kup_2 +=1
                    sum_cen_2 += cena
                    print(f"Pan nr 2 kupił 1 worek w tygodniu {i} za cene {cena}")
                k_kup_2 +=2
                sum_cen_2 += 2*cena
                print(f"Pan nr 2 kupił 2 worki węgla w tygodniu {i}za cene {2 * cena} zł")
        if k - k_kup_1 == 0 and k - k_kup_2 == 0:
            break


    if k_kup_1 < k:
        dop1 = (k-k_kup_1)*cena
        sum_cen_1+=dop1
        print(f"Gospodarz 1 musi dopłacić {(k-k_kup_1)*cena} za pozostałe worki")
    if k_kup_2 < k:
        dop2 = (k - k_kup_2) * cena
        sum_cen_2 += dop2
        print(f"Gospodarz 2 musi dopłacić {(k-k_kup_2)*cena} za pozostałe worki")

    print(f"Pan nr 1 wydał łącznie {sum_cen_1} zł")
    print(f"Pan nr 2 wydał łącznie {sum_cen_2} zł")
    if sum_cen_1>sum_cen_2:
        roznica= sum_cen_1-sum_cen_2
        print(f"Lepszą strategie miał pan nr 2, bo zaoczczedził o {roznica} zł wiecej")
    if sum_cen_2>sum_cen_1:
        roznica= sum_cen_2-sum_cen_1
        print(f"Lepszą strategie miał pan nr 1, bo zaoczczedził o {roznica} zł wiecej")
    if sum_cen_1==sum_cen_2:
        print(f"Obaj Panowie wydali tyle samo na ogrzewanie")





















if "__main__" == __name__:
    main()