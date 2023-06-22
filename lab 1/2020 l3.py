import math
def main():
    n = int(input("Podaj liczbe naturalną"))
    if n <= 1:
        raise ValueError("Miały być naturalne")
    i=2
    lista = []
    while n >1:
        if n%i==0:
            n=n/i
            pierwsza = i
            print(pierwsza)
            lista.append(pierwsza)

        else:
            i+=1
    lista_bez_pow = set(lista)
    naj_pow = max(lista,key=lista.count)
    l_powt = lista.count(naj_pow)
    print(f"najwięcej powtórzeń ma {naj_pow} i ma {l_powt} powtórzen")
    wynik_bez_krotnosci = math.prod(lista_bez_pow)
    print(f"Wynik bez krotności {wynik_bez_krotnosci}")




if "__main__" == __name__:
     main()