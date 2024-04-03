menuList = []
priceList = []

def showBill():
    print("====== My Menu List ======")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])

while True:
    menuName = input("Please Enter menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)

print(menuList,priceList)
showBill()
print("ราคารวมค่าอาหาร : ",sum(priceList)," THB")