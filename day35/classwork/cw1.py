def multiply_numbers():
    num1 = int(input("შეიყვანე პირველი რიცხვი: "))
    num2 = int(input("შეიყვანე მეორე რიცხვი: "))
    return num1 * num2
result = multiply_numbers()
print(result)



def example():
    a = 5
    b = 3
    return a + b   # აბრუნებს შედეგს ფუნქციის გარეთ

result = example()  # აქ ვინახავთ return-ით დაბრუნებულ მნიშვნელობას
print(result)       # print-ით ვაჩვენებთ ეკრანზე
