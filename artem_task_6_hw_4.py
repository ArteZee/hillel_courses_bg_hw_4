sentence: tuple = (1,2,3)
first_elem, second_elem, *other_elements = sentence

edit_sentence = first_elem,second_elem
new_sentence = tuple(edit_sentence)

print(new_sentence)