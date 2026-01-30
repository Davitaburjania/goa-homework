# STRING FUNCTIONS (მეთოდები)


# .upper()
# ყველა ასოს აქცევს დიდ ასოდ (uppercase)
text1 = "hello world"
print(text1.upper())   # HELLO WORLD

text2 = "Python"
print(text2.upper())   # PYTHON

text3 = "gamarjoba"
print(text3.upper())   # GAMARJOBA


# .lower()
# ყველა ასოს აქცევს პატარა ასოდ (lowercase)
text4 = "HELLO WORLD"
print(text4.lower())   # hello world

text5 = "PyThOn"
print(text5.lower())   # python

text6 = "GAMARJOBA"
print(text6.lower())   # gamarjoba


# .capitalize()
# მხოლოდ პირველ სიმბოლოს აქცევს დიდ ასოდ, დანარჩენს — პატარა ასოდ
text7 = "hello world"
print(text7.capitalize())   # Hello world

text8 = "pYTHON"
print(text8.capitalize())   # Python

text9 = "gEORGIA"
print(text9.capitalize())   # Georgia


# .title()
# თითოეული სიტყვის პირველ ასოს აქცევს დიდ ასოდ
text10 = "hello world"
print(text10.title())   # Hello World

text11 = "python is cool"
print(text11.title())   # Python Is Cool

text12 = "gamarjoba chema megobrebo"
print(text12.title())   # Gamarjoba Chema Megobrebo


# .find()
# ეძებს კონკრეტულ სიმბოლოს ან სიტყვას string-ში
# აბრუნებს მის ინდექსს (ადგილმდებარეობას)
# თუ ვერ იპოვა — აბრუნებს -1
text13 = "hello world"
print(text13.find("w"))   # 6

text14 = "python programming"
print(text14.find("python"))   # 0

text15 = "hello"
print(text15.find("z"))   # -1

