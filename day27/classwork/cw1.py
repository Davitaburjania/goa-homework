
cars = [
    "BMW", "Mercedes", "Audi", "Toyota", "Honda",
    "Ford", "Nissan", "Hyundai", "Kia", "Mazda"
]
print("მე-5 ელემენტი:", cars[4])


new_list = cars[1:6]
print("ახალი სია:", new_list)
print("ახალი სიის ბოლო ელემენტი:", new_list[-1])


print("ყოველი მეორე ელემენტი:", cars[::2])


print("მე-3-დან მე-8-მდე ყოველი მესამე:", cars[3:9:3])


first_five = cars[:5]
reversed_list = first_five[::-1]
print("შემოტრიალებული სია:", reversed_list)


copied_list = cars[:]
cars[7] = "Tesla"

print("ორიგინალი სია:", cars)
print("დაკოპირებული სია:", copied_list)
