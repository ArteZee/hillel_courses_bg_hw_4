list_of_tuple = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
new_list = []

for i in range(0, len(list_of_tuple) ):
    alfa = list(list_of_tuple[i])
    new_list.append(alfa)

print(new_list)
