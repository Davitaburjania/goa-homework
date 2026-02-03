# 2) კომენტარებით ახსნა append(), insert() და pop() ფუნქციების

# append() — ამატებს ელემენტს სიის ბოლოში
# insert(index, value) — ამატებს ელემენტს კონკრეტულ ინდექსზე
# pop() — შლის ელემენტს სიიდან (თუ ინდექსი არ მიუთითე, შლის ბოლოს)

# --------------------------------------------------


numbers = [10, 20, 30, 40, 50]
print(len(numbers))  

# --------------------------------------------------


nums = []

for i in range(5):
    num = int(input("შეიყვანე რიცხვი: "))
    nums.append(num)

print(nums)

# --------------------------


colors = ["red", "green", "blue", "yellow", "purple"]
colors.pop()  
print(colors)

# ----------------------------------------

animals = ["dog", "cat", "elephant", "lion"]
animals.insert(1, "monkey") 
print(animals)

# ---------------------------------------------
students = []

for i in range(3):
    name = input("შეიყვანე სტუდენტის სახელი: ")
    students.append(name)

students.insert(0, "Teacher")  
students.pop()              
print(len(students))          
print(students)               
# ------------------------------------------------

# 8) Custom ფუნქციების ახსნა
# Custom ფუნქცია არის ჩვენ მიერ შექმნილი ფუნქცია,
# რომელიც გვიმარტივებს კოდის წერას და თავიდან გვაცილებს გამეორებას.


# ფუნქციის შექმნის ეტაპები:
# 1) def keyword
# 2) ფუნქციის სახელი
# 3) ფრჩხილებში პარამეტრები
# 4) კოდის ბლოკი

# ---------------------------------

def sum_numbers(a, b):
    return a + b

print(sum_numbers(5, 7))

# ------------------------------------------

def check_even(num):
    if num % 2 == 0:
        print("რიცხვი ლუწია")
    else:
        print("რიცხვი კენტია")

check_even(10)

# -----------------------------
def square(num):
    return num * num

print(square(6))
# --------------------------
def to_upper(text):
    return text.upper()
print(to_upper("gamarjoba"))

# -----------
def full_name(name, surname):
    print("ჩემი სახელია", name, "და ჩემი გვარია", surname)
full_name("დათო", "აბურჯანია")