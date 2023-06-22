def main():
    height = int(input("Podaj wysokość ściany (7,9,11)"))
    if height == 7 or height == 9 or height == 11:
        True
    else:
        raise ValueError
    width = 10
    o = int(input("Podaj długość rolki o"))
    x = int(input("Podaj wartość rolki x"))
    time_x = float(input("Podaj ilość jednostek czasu x"))
    if time_x <= 0:
        raise ValueError
    time_o = time_x/3
    if o<= 0 or x<=0:
        raise ValueError
    if x > width - 1:
        raise ValueError
    n = x/2 #założenie że o musi być co najmniej dwa razy krótsze
    if o>n and o>width:
        raise ValueError
    window_width = 3
    window_height = 3

    ilosc_print = o+x
    licznik = 0

    for i in range(1, height):
        if
        for i in range (1,ilosc_print):
            for i in range (1,o+1):
                print("o", end=" ")
            for i in range (1,x+1):
                print("x", end=" ")









if "__main__" == __name__:
     main()