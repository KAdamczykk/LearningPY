def merge(x,y):
    u = []
    v = []
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                u.append(i)
                v.append(j)
    return [u,v]
def merge_sorted(x,y):
    u = []
    v = []
    i_x = 0
    i_y = 0
    while i_x < len(x) and i_y < len(y):
        if x[i_x] < y[i_y]:
            i_x += 1
        elif x[i_x] > y[i_y]:
            i_y += 1
        else:
            x_start = i_x
            while i_x < len(x) and x[x_start] == x[i_x]:
                i_x += 1
            y_start = i_y
            while i_y < len(y) and y[y_start] == y[i_y]:
                i_y += 1
            for i in range(x_start, i_x):
                for j in range(y_start, i_y):
                    u.append(i)
                    v.append(j)
    return [u, v]

def main():
    x = [1, 3, 5, 6, 3]
    y = [2, 3, 1, 5, 5, 4]
    k = [1, 3, 3, 5, 6]
    l = [1, 2, 3, 4, 5, 5]
    print(merge(x,y))
    print(merge_sorted(k, l))
if __name__ == '__main__':
    main()
