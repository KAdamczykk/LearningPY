def merge(x, y):
    u=[]
    v=[]
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                u.append(i)
                v.append(j)

    return [u,v]


def merge_sorted(x, y):
    size_x = len(x)
    size_y = len(y)

    u = []
    v = []
    i_x = 0
    i_y = 0

    while i_x < size_x and i_y < size_y:
        if x[i_x] < y[i_y]:
            i_x += 1
        elif x[i_x] > y[i_y]:
            i_y += 1
        else:
            x_start = i_x
            while i_x < size_x and x[x_start] == x[i_x]:
                i_x += 1
            y_start = i_y
            while i_y < size_y and y[y_start] == y[i_y]:
                i_y += 1

            for i in range(x_start, i_x):
                for j in range(y_start, i_y):
                    u.append(i)
                    v.append(j)
    return [u, v]


def main():
    # l = [1,2,3]
    # l.append(4)
    # print(l)
    #
    # item = l.pop()
    # print(item)
    # print(l)
    #
    # l2 = [5,6,7]
    # l.append(l2)
    # print(l)
    #
    # l.extend(l2)
    # print(l)
    #
    # l.insert(0, 999)
    # print(l)
    #
    # l.pop(0)
    # print(l)
    #
    # l.append(3)
    # l.append(3)
    # print(l)
    #
    # l.remove(3)
    # print(l)

    x=[1,3,5,6,3]
    y=[2,3,1,5,5,4]

    result = merge(x, y)
    print(result)

    x1 = [1,3,5,6]
    y1 = [1,2,3,3,3,4,5,5]
    result = merge_sorted(x1, y1)
    print(result)

if __name__ == '__main__':
    main()