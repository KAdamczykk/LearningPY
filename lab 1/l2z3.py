def main():
    l_10 = 0
    for i in range (0,21):
        cyfra = int(input("Podaj cyfre od najmniej znaczącej"))
        if cyfra<0 and cyfra>7:
            raise ValueError("Dana cyfra nie jest w systemie 8")
        w_10 = cyfra * 8**i
        l_10 +=w_10
        print(f"Liczba w 10 jest równa {l_10}")



if "__main__" == __name__:
    main()