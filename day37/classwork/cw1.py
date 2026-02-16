def my_len(iterable):
    count = 0
    for _ in iterable:
        count += 1           
    return count
print(my_len([1, 2, 3, 4]))    
print(my_len("hello"))          
def my_find(text, word):
    text_length = my_len(text)
    word_length = my_len(word)
    i = 0
    while i <= text_length - word_length:
        j = 0
        while j < word_length and text[i + j] == word[j]:
            j += 1
        if j == word_length:
            return i
        i += 1
    return -1
print(my_find("hello world", "world"))  
print(my_find("hello world", "cat"))    

def my_insert(lst, index, value):
    new_list = []
    i = 0
    for element in lst:
        if i == index:
            new_list += [value]
        new_list += [element]
        i += 1
    if index >= i:
        new_list += [value]
    return new_list
numbers = [1, 2, 3, 4]
result = my_insert(numbers, 2, 99)
print(result)  