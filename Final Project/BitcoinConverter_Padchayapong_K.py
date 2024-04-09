#created by Pachayapong Kardosoth

from tkinter import *
from forex_python.bitcoin import BtcConverter

main_window = Tk()
main_window.iconbitmap('bitcoin.ico')
main_window.title('Bitcoin Converter')
main_window.minsize(450,300)
main_window.configure(background="linen")

label_top = Label(main_window,text = "Bitcoin Converter",width=30,foreground="black",bg="gray",font=("Helvetica",30)).grid(row=0)
label_BTC_USDT = Label(main_window, text="BTC/USDT",font=("Helvetica",14))
label_BTC_USDT.grid(row=1,column=0)

b = BtcConverter()
b.get_latest_price('USD')
label_BTC_USDT_price = Label(main_window,text=b.get_latest_price('USD'),foreground="green",font=("Helvetica",14)).grid(row=2)
label_user_currency = Label(main_window, text="Enter your currency")
label_user_currency.grid(row=3,column=0)

blank = Label(main_window,text="")
blank.grid(row=5)

def change_currency(choice):
    choice = currency_option.get()

    def present_price():
        t = b.get_latest_price(choice)

    label_BTC_AnyCurrency_price = Label(main_window, text=b.get_latest_price(choice), foreground="green",
                                        font=("Helvetica", 14)).grid(row=5)

    def get_amount():
        fill_entry = int(amount_entry.get())
        label_BTC = Label(main_window,text="Your BTC is")
        label_BTC.grid(row=9)
        label_convert = Label(main_window,text=b.convert_to_btc(fill_entry,choice))
        label_convert.grid(row=10)
        label_BTC.after(5000, label_BTC.destroy)
        label_convert.after(5000, label_convert.destroy)

    calculateButton = Button(main_window, text="Convert Currency", command=get_amount)
    calculateButton.grid(row=7, column=0)

currency_choices = ['USD','EUR','JPY','GBP','AUD','CAD','CHF','CNY','SEK','NZD','THB']

currency_option = StringVar()
currency_option.set("Currency")
currency_dropdown = OptionMenu(
    main_window,
    currency_option,
    *currency_choices,
    command=change_currency
)
currency_dropdown.grid(row=4)

amount_entry = Entry(main_window)
amount_entry.grid(row=6)

label_editor = Label(main_window,text="Created by Padchayapong K.")
label_editor.place(x=520,y=275)

label_note = Label(main_window,text="Note: The green price is your currency \"CURRENT PRICE\"")
label_note.place(x=20,y=275)

main_window.mainloop()