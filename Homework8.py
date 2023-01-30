# Задача 1. 
       

# ingredient = {'Эспрессо': [1, 0, 0], 'Капучино': [1, 3, 0],
#               'Маккиато': [2, 1, 0], 'Кофе по-венски': [1, 0, 2],
#               'Латте Маккиато': [1, 2, 1], 'Кон Панна': [1, 0, 1]}
 
 
# def choose_coffee(preferences):
#     for i in preferences:
#         if ingredient[i][0] <= ingredients[0] and ingredient[i][1] <= ingredients[1] \
#                 and ingredient[i][2] <= ingredients[2]:
#             ingredients[0] -= ingredient[i][0]
#             ingredients[1] -= ingredient[i][1]
#             ingredients[2] -= ingredient[i][2]
#             return i
#     return 'К сожалению, не можем предложить Вам напиток'

 
# ingredients = []
# ingredients = [1, 2, 3]
# print(choose_coffee("Эспрессо, Капучино, Маккиато, Кофе по-венски, Латте Маккиато, Кон Панна".split(", ")))
# print(choose_coffee("Эспрессо, Капучино, Маккиато, Кофе по-венски, Латте Маккиато, Кон Панна".split(", ")))

# ingredients = [4, 4, 0]
# print(choose_coffee("Капучино, Маккиато, Эспрессо".split(", ")))
# print(choose_coffee("Капучино, Маккиато, Эспрессо".split(", ")))
# print(choose_coffee("Капучино, Маккиато, Эспрессо".split(", ")))


#Задача 2. 

small_symbols = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
big_symbols = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def shift(text, symbols, n):
    index = symbols.find(text)
    if index + n < len(symbols):
        return symbols[index + n]
    else:
        return symbols[(index + n) % len(symbols)]

    

def back_shift(text, symbols, n):
    index = symbols.find(text)
    if index - n >= 0:
        return symbols[index - n]
    else:        
        return symbols[(index - n) % len(symbols)]

    

def encrypt(text, n = 3):
    res = ""

    for i in range(0, len(text)): 
        if text[i].isupper():
            res += shift(text[i], big_symbols, n)
        
        elif text[i].islower():
            res += shift(text[i], small_symbols, n)
        else:
            res += text[i]
        
    return res


def decrypt (text, n = 3):
    res = ""
                   
    for i in range(0, len(text)):
        if text[i].isupper():
            res += back_shift(text[i], big_symbols, n)
        
        elif text[i].islower():
            res += back_shift(text[i], small_symbols, n)
        else:
            res += text[i]
        
    return res



str = encrypt(input())
print(str)
print(decrypt(str))