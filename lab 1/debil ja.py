def main():
    i = 0
    while i >=0:

        i = int(input("Podaj wartość oceny"))
        if i < 0:
            print("Błąd")
            break

        print(f"wartość wynosi{i}")
if "__main__" == __name__:
    main()



