x = 1

while x <= 5:
    if x % 2 == 0:
        print(x, "ლუწია")
    else:
        print(x, "კენტია")
    x += 1


num = int(input("შეიყვანე რიცხვი: "))

if num > 0:
    print("დადებითი რიცხვია")
    if num % 2 == 0:
        print("ლუწია")
    else:
        print("კენტია")
else:
    print("ნულს ან უარყოფითს უდრის")
