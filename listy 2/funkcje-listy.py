import math
def zlacz_append(t,k):
    u=[]
    for i in range(len(t)):
        u.append(t[i])
    for j in range (len(k)):
        u.append(k[j])
    return u
def zlacz(t,k):
    j = 0
    u = [None]*(len(t) + len(k))
    for i in range (len(u)):
        if i<len(t):
            u[i]=t[i]
        else:
            u[i] = k[j]
            if j<len(k)-1:
                j+=1
    return u
def zawin(t,k):
    u = []
    for i in range(k):
        for j in range(len(t)):
            u.append(t[j])
    return u
def rep_each(t,k):
    u = []
    for i in range(len(t)):
        for j in range(k):
            u.append(t[i])
    return u
def trim_nan(x):
    u = []
    k = None
    l = None
    for i in range(len(x)):
        if not math.isnan(x[i]):
            k = i
            break
    for j in range(len(x)-1,-1,-1):
        if not math.isnan(x[j]):
            l = j
            break
    if k == None or l == None:
        return x
    for w in range(k,l+1):
        u.append(x[w])
    return u
def rm_nan(x):
    u = []
    for i in range (len(x)):
        if not math.isnan(x[i]):
            u.append(x[i])
    return u
def dominanta(t):
    liczby = []
    powtorzenia = []
    max_pow = -float('inf')
    max_pow_l = None
    for i in range(len(t)):
        pass
def kwadrat_lacinski(t):
    assert len(t) == len(t[0])
    for i in range(len(t)):
        for j in range(len(t[0])):
            for k in range(j):
                if t[i][k] == t[i][j]:
                    return False
            for k in range(j+1, len(t[0])):
                if t[i][k] == t[i][j]:
                    return False
    for i in range(len(t[0])):
        for j in range(len(t)):
            for k in range(j+1, len(t)):
                if t[k][i] == t[j][i]:
                    return False
            for k in range(j):
                if t[k][i] == t[j][i]:
                    return False
    return True
def unique(x):
    u = []
    for i in range(len(x)-1):
        if not x[i]==x[i+1]:
            u.append(x[i])
    u.append(x[len(x)-1])
    return u
def rangi(t):
    #lista indeksow
    index_przes = [a for a in range (1,len(t)+1)]
    #sortowanie
    for i in range(1,len(t)):
        for j in range(len(t)-i):
            if not t[j] <= t[j+1]:
                t[j], t[j+1] = t[j+1], t[j]
                index_przes[j], index_przes[j+1] = index_przes[j+1], index_przes[j]
    #rangowanie
    lista_rang = [None]*len(t)
    for k in range(len(t)):
        counter=0
        suma = 0
        for l in range(len(t)):
            if t[k] == t[l]:
                counter+=1
                suma+=(l+1)
        lista_rang[k] = suma/counter
    #sortowanie indeksów i rang
    for m in range (1, len(t)):
        for n in range(len(t)-m):
            if not index_przes[n] <= index_przes[n+1]:
                index_przes[n], index_przes[n+1] = index_przes[n+1], index_przes[n]
                lista_rang[n], lista_rang[n+1] = lista_rang[n+1], lista_rang[n]
    return lista_rang
def split_labels(x,n):
    l = []
    y = []
    assert len(x) == len(n)
    for i in range(len(x)):
        z = True
        for j in range(len(l)):
            if n[i] == l[j]:
                y[j].append(x[i])
                z = False
                break
        if z:
            l.append(n[i])
            y.append([x[i]])
    return l, y
def main():
    a = [1,2,3]
    b = [2,3,4]
    c = [float('nan'), float('nan'), float('nan'),1,2,3,float('nan'),float('nan'),1,2,float('nan')]
    d = [[1,2,3], [4,5,6], [7,8,9]]
    e = [1,2,3,4,5,6,6,7,8,9,9,9]
    f = [4,1,3,5,2,4,3,4]
    g = ['k', 'r', 'w', 'k', 'w', 'a', 'k']
    h = [1,2,3,4,5,6,7]
    print(zlacz_append(a,b))
    print(zlacz(a,b))
    print(zawin(a,2))
    print(rep_each(a,2))
    print(trim_nan(c))
    print(rm_nan(c))
    print(kwadrat_lacinski(d))
    print(unique(e))
    print(rangi(f))
    print(split_labels(h,g))

if __name__ == '__main__':
    main()
