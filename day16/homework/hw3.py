correct_password = "goa123"
attempts = 3

while attempts > 0:
    user_input = input("შეიყვანე პაროლი: ")

   
    if user_input == correct_password:
        print("პაროლი სწორია! შესვლა წარმატებულია.")
        break

    
    attempts -= 1
    print("Password is incorrect! Try again")

    print("დაგრჩა", attempts, "მცდელობა.")

   
    if attempts == 0:
        break
