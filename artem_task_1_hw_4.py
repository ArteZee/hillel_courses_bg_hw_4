sentence: str = input()

if len(sentence) < 2:
    print("Ваша строка слишком короткая: %s" % (sentence))
else:
    print(sentence[0:2] + sentence[-2:])
