def main():
    s = int(input("Ziarno generatora "))
    n = int(input("Podaj ilość iteracji"))
    m=2**31-1
    a=1103515245
    c=12345
    number_file = "liczby.txt"
    with open(number_file, "w") as write_file:
        for i in range (n):
            s = (a*s+c)%m
            liczba = s/m
            i+=1
            write_file.write(f"{liczba}")
            write_file.write("\n")


if __name__ == '__main__':
    main()