import math
def main():
    n = int(input("Podaj liczbe boków stołu"))
    if n<5:
        raise ValueError("Niepoprawne dane")
    a = int(input("Podaj długość boku w cm"))
    if a<=30 and a>70:
        raise ValueError("Niepoprwne dane")
    h = int(input("Podaj wysokość stołu w cm"))
    if h <=50 and h>100:
        raise ValueError("Niepoprawne dane")
    print("Poprawne dane")
    #obliczamy czy da się wykonać stół
    R = a/(2*math.sin(math.pi/n))
    if R>157.5:
        raise ValueError("Nie można wyciąć takiego blatu")
    print("Można wyciąć taki blat")
    ilosc_belek = n*h//390 + 1
    print(f"Potrzeba {ilosc_belek} belek")
    max = 0
    for k in range (1,n-3):
        d= (a*math.sin(((k+1)*math.pi)/n))/math.sin(math.pi/n)
        if d>max:
            max = d
    if max <= math.sqrt(46400):
        print("Stół się zmieści")
    else:
        print("Stół się nie zmieści")

if "__main__" == __name__:
    main()
