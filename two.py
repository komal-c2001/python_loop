correct_pass="Some_pass"
not_found = True
while not_found:
    user_pass = input("Enter the password : ")
    if user_pass == correct_pass:
        print("Password is correct")
        not_found = False
    else:
        print("Password is incorrect")