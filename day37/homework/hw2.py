# ვქმნით ფუნქციას, რომელსაც აქვს default პარამეტრი name თუ ფუნქციის გამოძახებისას არგუმენტი არ გადაეცა,
# ავტომატურად გამოიყენებს ჩემს სახელს 

def print_name(name="dato"):
    
   
    for letter in name:
        print(letter)


print_name("giorgi")

print_name()
