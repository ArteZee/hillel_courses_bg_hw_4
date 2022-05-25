lst_1 = [0, 00, 0, 0, 0, 0, 0, 00, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lst_2 = [55, 3, 2, 1, 3, 4, 5, 6, 7, 11, 1, 1, 15, 5, 67, 7]

a = range(0,len(lst_1) - 1)

for i in a:
    if lst_1[i] in lst_2:
        print(True)
    else:
        print("Нет схожести ")
    break








