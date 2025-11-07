# შედარებითი ოპერაციები: ტოლობა == , ნაკლებობა < , არ არის ტოლი != , მეტობა > , მეტია ან ტოლია >= , ნაკლებია ან ტოლია

print(5 == 5)               #true
print(10 == 7)              #false
print("cat" == "cat")       #true
print("dog" == "dOg")       #false
print(1== 1)                #true

print(5 != 3)       #true
print(10 != 34)     #true
print(20 != 20)     #false
print(7 != 7.0)     #false
print(11 != 12)     #true

print(30 < 32)      #true
print(20 < 20)      #false
print(45 < 53)      #true
print(10 < 43)      #true
print(22 < 21)      #false

print(30 > 35)      #false
print(10 > 10)      #false
print(66 > 53)      #true
print(14 > 43)      #false
print(55 > 21)      #true

print(30 >= 30)     #true 
print(43 >= 10)     #true
print(53 >= 53)     #true
print(22 >= 43)     #false 
print(10 >= 21)     #false

print(40 <= 40)     #true
print(45 <= 16)     #false
print(54 <= 51)     #false
print(12 <= 44)     #true 
print(19 <= 22)     #true