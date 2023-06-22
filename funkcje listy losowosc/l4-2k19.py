import math
def drzewo(x, y):
    if x >= 0 and x <= 10 and y >= 0 and y <= 10:
        return (x == y) and (x % 10 < 4 or x % 10 > 5)
    elif x >= -10 and x <= -1 and y >= 0 and y <= 10:
        return True
    else:
        return False
def wypisz_prostokat(xmin, xmax, ymin, ymax):
    return f"{[xmin, xmax]} x {[ymin, ymax]}"
def najmniejszy_plot(xmin, xmax, ymin, ymax):
    for i in range (ymin, ymax):
        for j in range (xmin, xmax):
            D = drzewo(j,i)

def main():
    print(wypisz_prostokat(xmin = int(input("Podaj xmin")),
    xmax = int(input("Podaj xmax")),
    ymin = int(input("Podaj ymin")),
    ymax = int(input("Podaj ymax"))))






if __name__ == '__main__':
    main()