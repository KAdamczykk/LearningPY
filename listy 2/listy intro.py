def main():
   lista = [1,2,3,4,2]
   a = [1,2,3]
   p = []
   p.append(lista) #dodaje liste
   print(p)
   lista.pop(2) # usuwa liczbe po indeksem
   print(lista)
   a.remove(1) # usuwa wystąpienie danej liczby
   print(a)
   p.insert(0,a) #dodaje obiekt w dany indeks
   print(p)
   lista.sort() #sortuje liste
   print(lista)
   lista.count(2) #ilosc wystapien art w liscie
   print(lista.count(2))

if __name__ == '__main__':
    main()