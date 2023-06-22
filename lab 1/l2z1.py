def main():
    pozostale_cukierki = 100
    while pozostale_cukierki >= 0:
        liczba1 = int(input(f"podaj liczbe"))
        if liczba1 < 0 or liczba1 > 99:
            print("Błąd")
            break

        pozostale_cukierki -= liczba1
        if pozostale_cukierki < 0:
            print("Błąd")
            break

        if pozostale_cukierki == 0:
            print("Wygrał gracz 1")
        print(f"Pozostało {pozostale_cukierki} cukierków")
        liczba2 = int(input(f"podaj liczbe"))
        if liczba2 > 99 or liczba2 < 0:
            print("Błąd")
            break

        pozostale_cukierki -= liczba2
        if pozostale_cukierki < 0:
            print("Błąd")
            break

        if pozostale_cukierki == 0:
            print("Wygrał gracz 2")
        print(f"Pozostało {pozostale_cukierki} cukierków")


if "__main__" == __name__:
    main()
