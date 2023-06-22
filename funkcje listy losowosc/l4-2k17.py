import numpy as np
from sklearn import datasets, svm
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def F(a, b):

    """
    Nie interesuje nas, co funkcja robi:
    traktujemy ja jako "czarna skrzynke".
    Wazne jest jedynie to, ze F(a, b) zwraca wartosc z przedzialu [0,1]
    dla a, b > 0
    Przykład inspirowany http://scikit-learn.org/stable/auto_examples/
    exercises/plot_iris_exercise.html
    """
    iris = datasets.load_iris()  # zbior iris
    X, y = iris.data, iris.target
    X, y = X[y != 0, :2], y[y != 0]  # tylko klasy 1 i 2
    n_sample = len(X)
    np.random.seed(1234)
    order = np.random.permutation(n_sample)
    X = X[order]
    y = y[order].astype(float)
    X_train = X[:int(0.8 * n_sample)]  # proba uczaca = losowe 80%
    y_train = y[:int(0.8 * n_sample)]
    X_test = X[int(0.8 * n_sample):]  # proba testowa = pozostale 20%
    y_test = y[int(0.8 * n_sample):]
    clf = svm.SVC(gamma=a, C=b)  # support vector classifier
    clf.fit(X_train, y_train)
    return np.mean(clf.predict(X_test) == y_test)  # accuracy, wartosc z [0,1]
def main():
    input_file = "input.txt"
    with open(input_file, "r") as readfile:
        a1 = float(readfile.readline())
        an = float(readfile.readline())
        n = int(readfile.readline())
        b1 = float(readfile.readline())
        bm = float(readfile.readline())
        m = int(readfile.readline())
        print(a1,an,n,b1,bm,m)
    if not (a1 < an and b1 < bm and n > 1 and m > 1):
        raise ValueError("Błędne dane")

    r = (an-a1)/ (n-1)
    q = (bm-b1)/ (n-1)
    f_max=0
    f_min=1
    p_max =( 0 , 0)
    p_min = (0,0)
    ot_file = "output.txt"
    with open(ot_file, "w") as write_file:
        write_file.write("a \ b  |")
        for i in range (m):
            b_i = b1 + i * q
            write_file.write(f"{(b_i): 5.2f}")
        write_file.write("\n")
        write_file.write('_______|')
        for j in range(m * 6 - 8):
            write_file.write('_')
        write_file.write('\n')
        for j in range (n):
            a_j=a1+j*r
            write_file.write(f"{(a_j): <6.2f} |")
            for i in range (m):
                b_i = b1+i*q
                f_ij = F(a_j, b_i)
                write_file.write(f"{(f_ij): 5.2f}")
                if f_max < F(a_j, b_i):
                    f_max=F(a_j, b_i)
                    p_max = (a_j, b_i)
                if f_min>F(a_j, b_i):
                    f_min = F(a_j, b_i)
                    p_min = (a_j, b_i)
            write_file.write("\n")

    print(f"f max = {f_max} dla punktu {p_max}, f min = {f_min} dla punktu {p_min}")
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # ustal zakresy na osiach:
    ax.set_xlim([a1-r, an+r])
    ax.set_ylim([b1-q, bm+1])
    for j in range(n):
        a_j= a1 + j * r
        for i in range(m):
            b_i = b1 + i * q
            f_ij = F(a_j, b_i)
            scaled_f_ij = (f_ij - f_min) /(f_max - f_min)
            ax.add_patch(patches.Rectangle(
                (a_j - r / 2, b_i - q / 2),  # (x,y)
                r,  # szerokosc
                q,  # wysokosc
                facecolor=str(scaled_f_ij)  # stopien szarosci (od 0 do 1) jako napis
                ))
    # zapis do PNG po zakończeniu rysowania
    fig.savefig('output.png', dpi=90)


if __name__ == '__main__':
    main()