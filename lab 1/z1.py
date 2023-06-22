print("podaj liczbe schodów")
liczba_schodow = int (input())
numer_pietra = liczba_schodow//15
dodatkowe_schody = liczba_schodow%15
numer_pietra_plus_jeden =numer_pietra+1
parzyste_pietra = numer_pietra%2

if liczba_schodow < 1:
    print("błędne dane")
elif liczba_schodow > 300:
    print("błędne dane")
elif dodatkowe_schody == 0:
    print(f"jesteś na piętrze "  f"  {numer_pietra}")
elif dodatkowe_schody>0:
    print(f"jesteś pomiędzy {numer_pietra}, a {numer_pietra_plus_jeden} piętrem")

if liczba_schodow < 1:
    print("  ")
elif liczba_schodow > 300:
    print("  ")
elif dodatkowe_schody == 0 and parzyste_pietra == 0:
    print("jesteś na piętrze z toaletą")
elif dodatkowe_schody == 0 and parzyste_pietra == 1:
    print("toaleta jest na następnym piętrze")
elif dodatkowe_schody > 0 and parzyste_pietra == 0:
    ilosc_w_dol = dodatkowe_schody
    print(f"masz {ilosc_w_dol} schodów do łazienki w dół")
elif dodatkowe_schody > 0 and parzyste_pietra == 1:
    ilosc_w_gore = 15 - dodatkowe_schody
    print(f"masz {ilosc_w_gore} schodów do najbliższej toalety w góre")