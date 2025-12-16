total = 0
for i in range(5):
    print(i + 1, "რიცხვი შეიყვანე: ")
    num = int(input())
    total = total + num
print("რიცხვების ჯამი არის:", total)

if total % 2 == 0:
    print("მიღებული რიცხვი ლუწია")
else:
    print("მიღებული რიცხვი კენტია")





num = int(input("შეიყვანე რიცხვი: "))
while (num % 5 > 0) or (num % 7 > 0):
    print("თავიდან სცადე:")
print("შენ შემოიტანე სწორი რიცხვი:", num)
