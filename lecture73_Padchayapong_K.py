systemMenu = {"ข้าวมันไก่":45,"ข้าวหมกไก่":40,"ข้าวไก่ทอด":50}
menuList = []
def showBill():
    total = 0
    print("====== My Menu List ======")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        total += int(menuList[number][1])
    print("Total :",total)


while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

showBill()