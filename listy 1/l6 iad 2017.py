import matplotlib.pyplot as plt
import math
import random
def odleglosc(x,y):
    suma = 0
    for i in range (min(len(x), len(y))):
        iter = (x[i] - y[i])**2
        suma += iter
    wynik = math.sqrt(suma)
    return wynik
def random_point(n, a=-1, b =1):
    lista = [math.nan]*n
    for i in range (len(lista)):
        k = random.uniform(a,b)
        lista[i] = k
    return lista
def volume_exact(n):
    objetosc = ((math.pi)**(n/2))/(math.gamma((n/2 + 1)))
    return objetosc
def unit_ball_ratio( n):
    objetosc_kuli = volume_exact(n)
    objetosc_kostki = 2**n
    stosunek = objetosc_kuli/objetosc_kostki
    return  stosunek
def volume_approx(n,m=10000):
    punkt1 = [0]*n
    punkt2=[None]*n
    liczba_mn1 = 0
    liczba_wn1 = 0
    for i in range(m):
        for j in range(len(punkt2)):
            k = random.uniform(-1,1)
            punkt2[j] = k
        dis = odleglosc(punkt1, punkt2)
        if dis<=1:
            liczba_mn1+=1
            liczba_wn1+=1
        else:
            liczba_wn1+=1
        punkt2 = [None]*n
    stosunek = liczba_mn1/liczba_wn1
    wyskalowany = stosunek *2**n
    return wyskalowany








def main():
   x = [1,3,5,3,5]
   y = [9,3,2,1,4]
   print(odleglosc(x,y))
   n = min(len(x), len(y))
   print(random_point(n))
   v_kuli = volume_exact(n)
   print(v_kuli)
   print(unit_ball_ratio(n))
   print(volume_approx(n))
   y_exact = [None] * 18
   y_approx = [None] * 18
   y_ratio = [None] * 18
   for i in range(19):
       y_exact[i] = volume_exact(i + 1)
       y_approx[i] = volume_approx(i + 1)
       y_ratio[i] = unit_ball_ratio(i + 1)
   fig = plt.figure()
   x= range(1,20)
   #y_exact =
   #y_approx =
   #y_ratio =
   ax1 = fig.add_subplot(2, 1, 1)
   ax1.scatter(x, y_approx, color="red", marker=(3, 0, 0))
   ax1.scatter(x, y_exact)
   ax1.grid()
   ax2 = fig.add_subplot(2, 1, 2)
   ax2.scatter(x, y_ratio)
   ax2.grid()
   fig.savefig('volume.png', dpi = 90)

   if __name__ == "__main__":
    main()