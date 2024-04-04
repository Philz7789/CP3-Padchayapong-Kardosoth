class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " +self.name+ " " +self.lastName + "'s cart")

customer1 = Customer()
customer1.name = input("Enter your name : ")
customer1.lastName = input("Enter your lastname : ")
customer1.addCart()