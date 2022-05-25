# get date and separate for coma
list_words: list= input().split(",")
list_words.sort()
# create new list to append unique words
new_list = []
for i in range(0, len(list_words) -1 ):
    if list_words[i] != list_words[i + 1]:
        new_list.append(list_words[i])


print (list_words)
print(new_list)
