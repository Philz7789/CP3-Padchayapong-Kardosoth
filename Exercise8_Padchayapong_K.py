userName = input("Username : ")
password = input("Password : ")
if userName == ("Philz") and password == ("123456"):
    print("Welcome to Orange Fruit Online Shop")
    print("The price of an orange is 5 THB")
    orangeNo = int(input("Please select the number of pieces : "))
    print("====================================================")
    print("The total price is ",(orangeNo*5),(" THB"))
    print("====================================================")
    print("♥ Thank you so much & Welcome back again next time ♥")
else:
    print("That username or password was incorrect. Please try again.")