import random
import math
random.seed(2020)
def skok(pozycja):
    if random.random()<0.5:
        pozycja+=1
        print("Kozica skoczyła o 1 pole")
    elif 0.5<=random.random()<0.8:
        pozycja+=2
        print("Kozica skoczyła o 2 pola")
    else:
        pozycja+=3
        print("Kozica skoczyła o 3 pola")
    return pozycja
def mega_skok(pozycja):
    if random.random()<0.3:
        pozycja+=5
        print("Kozica wykonała MEGA SKOK")
    else:
        pozycja-=1
        if pozycja<0:
            pozycja=0
        print("Kozica nie zrobiła MEGA SKOKU")
    return pozycja
def atak(pozycja_atak, pozycja_b, tura_atak, tura_b):
    if tura_atak == True and tura_b == False and pozycja_atak<=pozycja_b:
        print("Kozica jest za nisko, żeby atakować")
        tura_atak=False
        tura_b=True
        return pozycja_atak, pozycja_b, tura_atak, tura_b
    elif random.random()<0.5:
         pozycja_b -= math.ceil(((pozycja_atak-pozycja_b)/2)**2)
         if pozycja_b<0:
             pozycja_b==0
         print("Atak udany")
         tura_atak = False
         tura_b=True
         return pozycja_atak, pozycja_b, tura_atak, tura_b
    elif 0.5<=random.random()<1:
        pozycja_atak-=1
        if pozycja_atak<0:
            pozycja_atak=0
        print("Atak nieudany")
        tura_atak = False
        tura_b = True
        return pozycja_atak, pozycja_b, tura_atak, tura_b

def main():
    pozycja_1=0
    pozycja_2=0
    pozycja_1_stara=0
    pozycja_2_stara=0
    ruch=0
    tura_1= True
    tura_2= False
    file= "zapisgry.txt"
    i=1
    while i>0:
        if pozycja_1>=20 or pozycja_2>=20:
            break
        if tura_1==True and tura_2==False:
            print("Ruch kozicy 1")
            print("Co chcesz zrobić \n 1-skok \n 2-mega skok \n 3-atak")
            wybor = int(input())
            if wybor ==1:
                pozycja_1_stara=pozycja_1
                pozycja_1 = skok(pozycja_1)
                ruch = pozycja_1-pozycja_1_stara
                with open(file, "a") as writefile:
                    writefile.write(f"Kozica 1 wybór: skok, ruch:{ruch}\n ")
                    writefile.write(f"Pozycja kozicy 1: {pozycja_1}\n")
                    writefile.write(f"Pozycja kozicy 2: {pozycja_2}\n")
                tura_1 = False
                tura_2 = True
            elif wybor ==2:
                pozycja_1_stara=pozycja_1
                pozycja_1 = mega_skok(pozycja_1)
                ruch = pozycja_1-pozycja_1_stara
                with open(file, "a") as writefile:
                    writefile.write(f"Kozica 1 wybór: megaskok, ruch: {ruch} \n")
                    writefile.write(f"Pozycja kozicy 1: {pozycja_1} \n")
                    writefile.write(f"Pozycja kozicy 2: {pozycja_2} \n")
                tura_1 = False
                tura_2= True
            elif wybor ==3:
                pozycja_1, pozycja_2, tura_1, tura_2 = atak(pozycja_1, pozycja_2, tura_1, tura_2)

                with open(file, "a") as writefile:
                    writefile.write(f"Kozica 1 wybór: atak \n")
                    writefile.write(f"Pozycja kozicy 1: {pozycja_1} \n")
                    writefile.write(f"Pozycja kozicy 2: {pozycja_2} \n")
            else:
                print("Błędne dane")
                with open(file, "a") as writefile:
                    writefile.write(f"Kozica 1 wybór: błąd, ruch:0 \n")
                    writefile.write(f"Pozycja kozicy 1: {pozycja_1}\n")
                    writefile.write(f"Pozycja kozicy 2: {pozycja_2}\n")
                tura_1 = False
                tura_2 = True
            print(f"Pozycja kozicy 1: {pozycja_1} \n Pozycja kozicy 2: {pozycja_2}")
        elif tura_2==True and tura_1==False:
            print("Ruch kozicy 2")
            print("Co chcesz zrobić \n 1-skok \n 2-mega skok \n 3-atak")
            wybor = int(input())
            if wybor == 1:
                pozycja_2_stara=pozycja_2
                pozycja_2 = skok(pozycja_2)
                ruch = pozycja_2-pozycja_2_stara
                with open(file, "a") as writefile:
                    writefile.write(f"Kozica 2 wybór: skok, ruch {ruch}\n")
                    writefile.write(f"Pozycja kozicy 1: {pozycja_1}\n")
                    writefile.write(f"Pozycja kozicy 2: {pozycja_2}\n")
                tura_1 = True
                tura_2 = False
            elif wybor == 2:
                pozycja_2_stara = pozycja_2
                pozycja_2 = mega_skok(pozycja_2)
                ruch = pozycja_2 - pozycja_2_stara
                with open(file, "a") as writefile:
                    writefile.write(f"Kozica 2 wybór: megaskok, ruch:{ruch}\n ")
                    writefile.write(f"Pozycja kozicy 1: {pozycja_1}\n")
                    writefile.write(f"Pozycja kozicy 2: {pozycja_2}\n")
                tura_1 = True
                tura_2 = False
            elif wybor == 3:
                pozycja_2, pozycja_1, tura_2, tura_1 = atak(pozycja_2, pozycja_1, tura_2, tura_1)
                with open(file, "a") as writefile:
                    writefile.write(f"Kozica 2 wybór: atak, \n ")
                    writefile.write(f"Pozycja kozicy 1: {pozycja_1}\n")
                    writefile.write(f"Pozycja kozicy 2: {pozycja_2} \n")
            else:
                print("Błędne dane")
                with open(file, "a") as writefile:
                    writefile.write(f"Kozica 1 wybór: błąd, ruch: 0 \n")
                    writefile.write(f"Pozycja kozicy 1: {pozycja_1} \n")
                    writefile.write(f"Pozycja kozicy 2: {pozycja_2} \n")
                tura_1 = True
                tura_2 = False
            print(f"Pozycja kozicy 1: {pozycja_1} \n Pozycja kozicy 2: {pozycja_2}")
    if pozycja_1>pozycja_2:
        print("Wygrywa kozica 1 ")
        with open(file, "a") as writefile:
            writefile.write(f"Wygrała Kozica 1")
    elif pozycja_2>pozycja_1:
        print("Wygrywa kozica 2")
        with open(file, "a") as writefile:
            writefile.write(f"Wygrała Kozica 2")
    else:
        print("Remis")
        with open(file, "a") as writefile:
            writefile.write(f"Remis")

if __name__ == '__main__':
    main()