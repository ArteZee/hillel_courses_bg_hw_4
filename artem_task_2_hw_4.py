sentence: str = input()
# create empty dictionary
dic = {}

for key in sentence:
    dic[key] = sentence.count(key)

print(dic)
