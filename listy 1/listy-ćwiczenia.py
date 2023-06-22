import random
import math
def min_max(lista):
    #3.1
    nowa = [float("inf"),-float("inf")]
    for i in range(len(lista)):
        if lista[i]<nowa[0]:
            nowa[0] = lista[i]
        if lista[i]>nowa[1]:
            nowa[1]=lista[i]
    return nowa
def shuffle(t):
    #3.2
    for i in range(len(t)):
        k = random.randint(0, len(t)-1)
        n = random.randint(0,len(t)-1)
        t[k], t[n] =t[n], t[k]
    return t
def permute(t,p):
    #3.3
    new = []
    for  i in range(min(len(t), len(p))):
        new += [t[p[i]]]
    return new
def is_sorted(x):
    #3.4
    for i in range (1,len(x)):
        if x[i-1]>x[i]:
            return  False
    return True
def merge(x,y):
    #3.5
    new = [None]* (len(x)+len(y))
    k=0
    l=0
    for i in range(len(new)):
        if k == len(x):
            new[i]= y[l]
            l+=1
            continue
        if l == len(y):
            new[i] = x[k]
            k+=1
            continue
        if x[k]<=y[l]:
            new[i] = x[k]
            k+=1
        elif x[k]>y[l]:
            new[i] = y[l]
            l+=1
    return new
def partition(t,k):
    pass
def any_duplicated(x):
    #3.7
    for i in range(1, len(x)):
        if x[i]==x[i-1]:
            return "Duplikują się"
    return "Nie duplikują się"
def kty_najwiekszy(t,k):
    pass
def add_vectorized(x,y):
    #3.12
    r = [None]*(max(len(x), len(y)))
    for i in range (len(r)):
        r[i]= x[i%len(x)]+y[i%len(y)]
    return r
def cumsum(x):
    #3.13
    suma = 0
    for i in range(len(x)):
        x[i]+=suma
        suma = x[i]
    return x
def diff(x):
    #3.14
    for i in range (1, len(x)):
        x[i-1] = x[i]-x[i-1]
    return x
def polidrom(x):
    #3.15
    for i in range (len(x)):
        if not x[i]==x[len(x)-1-i]:
            return "Nie jest"
    return "Jest"
def odwrot_kolejnosc(x):
    #3.16
    for i in range (len(x)//2+1):
        x[i], x[len(x)-1-i] = x[len(x)-1-i], x[i]
    return x
def zamien_nan(x):
    #3.17
    suma = 0
    counter = 0
    for i in range(len(x)):
        for j in range(len(x)):
            if not math.isnan(x[j]):
                suma+=x[j]
                counter+=1
        srednia = suma/counter
        if math.isnan(x[i]):
            x[i]=srednia
    return x
def zastap_nana(t):
    #3.18
    min = 0
    max = 0
    for i in range (len(t)):
        if not math.isnan(t[i]):
            min = t[i]
        elif math.isnan(t[i]):
            for j in range (i, len(t)):
                if not math.isnan(t[j]):
                    max = t[j]
                    break
            t[i] = (min+max)/2
    return t
def lex(x,y):
    #3.19
    for i in range(min(len(x), len(y))):
        if x[i]<y[i]:
            return True
        if x[i]>y[i]:
            return False
        if x[i]==y[i]:
            continue
        if i == min(len(x), len(y)) -1 and x[i]==y[i]:
            return True
def sumator(a,b):
    #3.20
    suma = []
    c=0
    l=0
    for i in range (min(len(a), len(b))):
        if i == min(len(a), len(b))-1:
            l = (a[i]+b[i]+c)%10
            c = (a[i]+b[i]+c)//10
            suma += [l]
            for j in range(i, max(len(a), len(b))):
                if len(a)>len(b):
                    l = (a[j]+c)%10
                    c = (a[j]+c)//10
                    suma += [l]
                else:
                    l = (b[j] + c) % 10
                    c = (b[j] + c) // 10
                    suma += [l]
        else:
            l = (a[i] + b[i] + c) % 10
            c = (a[i] + b[i] + c) // 10
            suma += [l]
    return suma
def horner(lista,x):
    #3.21
    suma=0
    for i in range (len(lista)-1,-1,-1):
        if i == len(lista)-1:
            suma+=lista[i]*x
        elif i == 0:
            suma+=lista[i]
        else:
            suma = (suma+lista[i])*x
    return suma
def is_prime(x):
    #3.24
    lista_b = [None]*len(x)
    counter_p = 0
    for i in range(len(lista_b)):
        if x[i]<2:
            lista_b[i] = False
        elif x[i] ==2:
            lista_b[i]=True
        else:
            for j in range(2, x[i]):
                if x[i]%j==0:
                    counter_p +=1
            if counter_p==0:
                lista_b[i] = True
                counter_p=0
            else:
                lista_b[i]= False
                counter_p=0
    return lista_b

def main():
    lista1 = [2,4,7,9,15,17]
    lista2 = [2,1]
    x=-1
    print(is_prime(lista1))
if __name__ == "__main__":
    main()