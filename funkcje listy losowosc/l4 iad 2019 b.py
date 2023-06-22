import math
import random
def fun(a, b):
    res1 = a + b
    res2 = a - b
    res3 = a * b
    return res1, res2, res3

def drzewo(x, y):
    if x >= 0 and x <= 10 and y >= 0 and y <= 10:
        return (x == y) and (x % 10 < 4 or x % 10 > 5)
    elif x >= -10 and x <= -1 and y >= 0 and y <= 10:
        return True
    else:
        return False

def wypisz_kolo(x, y, r):
    print(f"Srodek ({x}, {y}), promien {r}")

def odleglosc (x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1-y2)**2)

def najmniejszy_plot(x_sad, y_sad, r_sad, x, y):
    x_min = math.ceil(x_sad - r_sad)
    x_max = int(x_sad + r_sad)
    y_min = math.ceil(y_sad - r_sad)
    y_max = int(y_sad + r_sad)

    plot_r = -float("inf")

    czy_bylo_drzewo = False
    for i in range(x_min, x_max + 1):
        for j in range(y_min, y_max + 1):
            # czy punkt i,j jest w sadzie
            if odleglosc(i, j, x_sad, y_sad) <= r_sad:
                # punkt i, j jest w sadzie
                if drzewo(i, j):
                    czy_bylo_drzewo = True
                    # w pukcie i, j jest drzewo
                    odleglosc_drzewa_od_srodka_plotu = odleglosc(i, j, x, y)
                    if odleglosc_drzewa_od_srodka_plotu > plot_r:
                        plot_r = odleglosc_drzewa_od_srodka_plotu

    if not czy_bylo_drzewo:
        return 0,0,0
    return x, y, plot_r

def zapisz_do_pliku(sciezka, x, y, r):
    x_min = math.ceil(x - r)
    x_max = int(x + r)
    y_min = math.ceil(y - r)
    y_max = int(y + r)

    with open(sciezka, "w") as f:
        for j in range(y_max, y_min - 1, -1):
            f.write(f"{j} ")
            for i in range(x_min, x_max + 1):
                # czy punkt i,j jest w sadzie
                if odleglosc(i, j, x, y) <= r:
                    # punkt i, j jest w sadzie
                    if drzewo(i, j):
                        f.write("D")
                    else:
                        f.write(".")
                else:
                    # punkt i, j nie jest w sadzie
                    f.write(" ")
                    # print(" ", end="", file = f)
            f.write("\n")
        f.write("y/x ")
        for i in range(x_min, x_max + 1):
            f.write(f"{i}")

def obwod_kola(x, y, r):
    return 2 * math.pi * r

def naprawde_najkrotszy_plot(x, y, r):
    x_min = math.ceil(x - r)
    x_max = int(x + r)
    y_min = math.ceil(y - r)
    y_max = int(y + r)

    min_obwod = float("inf")
    min_plot = None

    for i in range(x_min, x_max + 1):
        for j in range(y_min, y_max + 1):
            # czy punkt i,j jest w sadzie
            if odleglosc(i, j, x, y) <= r:
                # punkt i, j jest w sadzie
                plot = najmniejszy_plot(x, y, r, i, j)
                obwod_plot = obwod_kola(plot[0], plot[1], plot[2])
                if obwod_plot < min_obwod:
                    min_obwod = obwod_plot
                    min_plot = plot
    return min_plot

#demonstracja czytania z pliku
# def czytaj_plik(sciezka):
#     sum = 0
#     with open(sciezka) as file:
#         for jaka_nazwa in file:
#             # line to sa kolejne linie pliku
#             sum += int(jaka_nazwa)
#
#         zmienna1 = int(file.readline())
#         zmienna2 = file.readline()
#         zmienna3 = float(file.readline())
#     return sum

def drzewo2(x, y):
    if not ( -10 <= x <= 10) or not (-10 <= y <= 10):
        return False
    # if x <-10 or x > 10 or y < -10 or y > 10:
    #     return False
    if 0 <= x <=10 and -10<=y <=10:
        if random.random(0 < 0.5):
            return True
        else:
            return False
    else:
        if random.random(0 < 0.1):
            return True
        else:
            return False
def main():
    random.seed(2022)
    print(czytaj_plik("plik.txt"))
    # print("Podaj polozenie sadu (x, y, r)")
    # x_s = int(input())
    # y_s = int(input())
    # r_s = float(input())
    # print("Podane koło to:")
    # wypisz_kolo(x_s, y_s, r_s)
    # print("Podaj wspolrzedne srodka plotu")
    # x_plotu = int(input())
    # y_plotu = int(input())
    # plot = najmniejszy_plot(x_s, y_s, r_s, x_plotu, y_plotu)
    # print(f"Najmniejszy plot zawierajacy wszystkie drzewka: ", end="")
    # wypisz_kolo(plot[0], plot[1], plot[2])
    # sciezka = input("Podaj sciezke do zapisu ")
    # zapisz_do_pliku(sciezka, 5, 6, 5)

    x_s = 8
    y_s = 7
    r_s = 7

    x_plotu = 5
    y_plotu = 8
    plot = najmniejszy_plot(x_s, y_s, r_s, x_plotu, y_plotu)
    print(f"Obwod sadu wynosi {obwod_kola(8, 7, 7)}")
    print(f"Dlugosc plotu {obwod_kola(plot[0], plot[1], plot[2])}")

    min_plot = naprawde_najkrotszy_plot(x_s, y_s, r_s)
    wypisz_kolo(min_plot[0], min_plot[1], min_plot[2])

if __name__ == "__main__":
    main()