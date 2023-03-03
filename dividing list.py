"""Программа деления списка на произвольное
количество частей"""

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
        20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


def splet_list(lst, N):
    a = len(lst) // N
    b = len(lst) % N
    print('a //=', a)
    print('b % =', b)
    print(f'Делить список на N={N} частей:')
    if a + b == N and b != 0:
        a += 1
    elif 1 <= N - b <= 3 and b != 0:
        a += 1
    ls = []
    for i in range(1, N+1):
        ls.append([])
    n = -1
    while n != N-1:
        n += 1
        while len(ls[n]) != a and len(lst) >= a:
            ls[n].append(lst[0])
            lst.remove(lst[0])
    if len(lst) != 0:
        while len(lst) != 0:
            ls[n].append(lst[0])
            lst.remove(lst[0])
    elif 2 <= (len(ls[n]) - len(ls[n-1])) <= 4:
        ls[n - 2].append(ls[n-1][0])
        ls[n-1].remove(ls[n-1][0])
        ls[n - 1].append(ls[n][0])
        ls[n].remove(ls[n][0])
        ls[n - 1].append(ls[n][0])
        ls[n].remove(ls[n][0])
    elif (len(ls[n]) - len(ls[n-1])) == 6:
        t2 = 0
        while t2 != 2:
            ls[n - 2].append(ls[n - 1][0])
            ls[n - 1].remove(ls[n - 1][0])
            ls[n - 1].append(ls[n][0])
            ls[n].remove(ls[n][0])
            ls[n - 1].append(ls[n][0])
            ls[n].remove(ls[n][0])
            t2 += 1
        ls[n - 3].append(ls[n - 2][0])
        ls[n - 2].remove(ls[n - 2][0])
        ls[n - 2].append(ls[n-1][0])
        ls[n-1].remove(ls[n-1][0])
        ls[n - 4].append(ls[n - 3][0])
        ls[n - 3].remove(ls[n - 3][0])
        ls[n - 3].append(ls[n - 2][0])
        ls[n - 2].remove(ls[n - 2][0])
    print('Пустой исходный список:', lst)
    print('Итоговые списки:', end='\t')
    for i in ls:
        print(i, end='\t')
    print()


if __name__ == '__main__':
    splet_list(lst1, 7)
