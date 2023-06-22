import copy
def read_data(datafile):
    extracted_data = [i.strip().split() for i in open(datafile)]
    flat_list = [int(item) for sublist in extracted_data for item in sublist]
    return flat_list
def validate(lista):
    d = int(input("Podaj wartość d "))
    n = int(input("Podaj wartość n "))
    nowa = []
    if d>=n:
        raise ValueError("Błędne dane")
    for i in range(len(lista)):
        if 0<lista[i]<n:
            nowa+=[lista[i]]
        elif  lista[i]>=n:
            continue
    return d, n, nowa
def merge_isands(tab):
    new = [tab[0]]
    i = 2
    counter = 0
    while i < len(tab):
        if tab[i - 1] >= tab[i]:
            for j in range(i, len(tab), 2):
                if tab[j - 1] < tab[j]:
                    new += [tab[j - 1]] + [tab[j]]
                    i = j + 1
                    counter += 1
                    break
                else:
                    continue
            if counter == 0:
                new += [tab[len(tab) - 1]]
                break
        else:
            new += [tab[i]]
            i += 1
    return new
def create_map(kord, d, n):
    mapa = ['_']*n
    mapa[0] = '|'
    j = 1
    for i in range(2, len(mapa)):
        if kord[j - 1] <= i <= kord[j]:
            mapa[i] = '|'
            for k in range(1,d+1):
                if mapa[kord[j-1]-k] == '_':
                    mapa[kord[j-1]-k] = '-'
                if mapa[kord[j]+k]== '_':
                    mapa[kord[j]+k] = '-'
                else:
                    continue
            if i == kord[j]:
                j += 2
                if j > len(kord) - 1:
                    break
    return mapa






def main():
    koordynaty = read_data("koordynaty")
    print(koordynaty)
    d, n,  ograniczone_koordynaty = validate(koordynaty)
    print(d, ograniczone_koordynaty)
    wyscalowana_lista = merge_isands(ograniczone_koordynaty)
    print(wyscalowana_lista)
    mapa = create_map(wyscalowana_lista, d,n)
    print(mapa)
if __name__ == "__main__":
    main()