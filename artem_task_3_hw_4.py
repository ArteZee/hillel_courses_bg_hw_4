# get date and separate for coma
list_of_products: list = input("Put you product after space:\n").split(" ")

longest_word = max(list_of_products, key=len)
len_of_longest_word = len(list_of_products[list_of_products.index(longest_word)])
result = ("Самое длинное название продукта {} длинна {} символов").format(longest_word, len_of_longest_word)
print(result)
