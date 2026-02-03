names = ["Giorgi", "Nika", "Luka", "Dato", "Sandro"]
user_name = input("შეიყვანე სახელი: ")
names.append(user_name)
print(names)


names = ["Giorgi", "Nika", "Luka", "Dato", "Sandro"]
names.insert(3, "Tarieli")
print(names)



names = ["Giorgi", "Nika", "Luka", "Dato", "Sandro"]
names.pop(4)
print(names)



names = ["Giorgi", "Nika", "Luka", "Dato", "Sandro"]
names.remove("Nika")
print(names)



names = ["Giorgi", "Nika", "Luka", "Dato", "Sandro"]
search_name = input("შეიყვანე სახელი: ")
if search_name in names:
    print(names.index(search_name))
else:
    print("not index in list")
