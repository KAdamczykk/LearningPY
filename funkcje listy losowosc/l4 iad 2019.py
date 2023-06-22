import math
import random


def drzewo(x, y):
    if x >= 0 and x <= 10 and y >= 0 and y <= 10:
        return (x == y) and (x % 10 < 4 or x % 10 > 5)
    elif x >= -10 and x <= -1 and y >= 0 and y <= 10:
        return True
    else:
        return False


def wypisz_prostokat(x_min, x_max, y_min, y_max):
    return f"{[x_min, x_max]}x{[y_min, y_max]}"


def najmniejszy_plot(xmin, xmax, ymin, ymax):
    xmin_d = float("inf")
    xmax_d = -float("inf")
    ymin_d = float("inf")
    ymax_d = -float("inf")
    czy_bylo_drzewo = False
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            if drzewo(x, y):
                if x < xmin_d:
                    xmin_d = x
                if x > xmax_d:
                    xmax_d = x
                if y < ymin_d:
                    ymin_d = y
                if y > ymax_d:
                    ymax_d = y
                czy_bylo_drzewo = True
    if not czy_bylo_drzewo:
        return 0, 0, 0, 0
    return xmin_d, xmax_d, ymin_d, ymax_d


def zapisz_pliku(sciezka, xmin, xmax, ymin, ymax):
    with open(sciezka, "w") as file:
        for y in range(ymax, ymin - 1, -1):
            file.write(f"{y}")
            for x in range(xmin, xmax + 1):
                if drzewo(x, y):
                    file.write("D")
                else:
                    file.write(".")
            file.write("\n")
        file.write("y/x")
        for x in range(xmin, xmax + 1):
            file.write(f"{x}")


def obwod_prostokata(xmin, xmax, ymin, ymax):
    bok1 = xmax - xmin
    bok2 = ymax - ymin
    obwod = 2 * bok1 + 2 * bok2
    return obwod


def najlepszy_podzial(xmin, xmax, ymin, ymax):
    x_gwiazdka = None
    najmniesza_suma_obw = float("inf")
    for x in range(xmin, xmax + 1):
        plot_1xmin, plot_1xmax, plot_1ymin, plot_1ymax = najmniejszy_plot(xmin, x, ymin, ymax)
        plot_2xmin, plot_2xmax, plot_2ymin, plot_2ymax = najmniejszy_plot(x, xmax, ymin, ymax)
        obw_1 = obwod_prostokata(plot_1xmin, plot_1xmax, plot_1ymin, plot_1ymax)
        obw_2 = obwod_prostokata(plot_2xmin, plot_2xmax, plot_2ymin, plot_2ymax)
        suma_obw = obw_1 + obw_2
        if najmniesza_suma_obw > suma_obw:
            najmniesza_suma_obw = suma_obw
            x_gwiazdka = x
    return x_gwiazdka


def drzewo2(x, y):
    x = int
    y = int
    if -10 > x or x > 10 or y > 10 or y < -10:
        return False
    elif 0 <= x <= 10 and -10 <= y <= 10:
        if random.random(0 < 0.5):
            return True
        else:
            return False
    elif -10 <= x <= -1 and -10 <= y <= 10:
        if random.random(0 < 0.1):
            return True
        else:
            return False


def main():
    random.seed(2022)
    xmin_s = int(input("Podaj xmin sadu"))
    xmax_s = int(input("Podaj xmax sadu"))
    ymin_s = int(input("Podaj ymin sadu"))
    ymax_s = int(input("Podaj ymax sadu"))
    print(wypisz_prostokat(xmin_s, xmax_s, ymin_s, ymax_s))
    xmin_p, xmax_p, ymin_p, ymax_p = najmniejszy_plot(xmin_s, xmax_s, ymin_s, ymax_s)
    print(wypisz_prostokat(xmin_p, xmax_p, ymin_p, ymax_p))
    sciezka = input("Podaj ścieżke pliku")
    zapisz_pliku(sciezka, xmin_s, xmax_s, ymin_s, ymax_s)
    obwod_sadu = obwod_prostokata(xmin_s, xmax_s, ymin_s, ymax_s)
    print(f"Obwod sadu wynosi {obwod_sadu}")
    dlugosc_plotu = obwod_prostokata(xmin_p, xmax_p, ymin_p, ymax_p)
    print(f"Długość płotu wynosi {dlugosc_plotu}")
    najlepszy_podzial_sadu = najlepszy_podzial(xmin_p, xmax_p, ymin_p, ymax_p)
    print(f"Najlepszym podziałem jest {najlepszy_podzial_sadu}")


if __name__ == "__main__":
    main()