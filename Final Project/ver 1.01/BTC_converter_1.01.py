import tkinter as tk
from tkinter import ttk, messagebox
from forex_python.bitcoin import BtcConverter

class BitcoinConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bitcoin Converter")
        self.geometry("500x400")
        self.iconbitmap("bitcoin.ico")
        self.configure(background="linen")

        self.btc_converter = BtcConverter()
        self.create_widgets()

    def create_widgets(self):
        # Top label
        top_label = tk.Label(self, text="Bitcoin Converter", width=30, foreground="black", bg="gray", font=("Helvetica", 30))
        top_label.pack(pady=10)

        # BTC/USDT label and price
        btc_usdt_label = tk.Label(self, text="BTC/USDT", font=("Helvetica", 14))
        btc_usdt_label.pack(pady=5)
        btc_usdt_price = self.get_latest_price("USD")
        btc_usdt_price_label = tk.Label(self, text=btc_usdt_price, foreground="green", font=("Helvetica", 14))
        btc_usdt_price_label.pack(pady=5)

        # Currency dropdown
        currency_label = tk.Label(self, text="Enter your currency")
        currency_label.pack(pady=5)
        currency_choices = ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD", "THB"]
        self.currency_var = tk.StringVar()
        self.currency_var.set("Currency")
        currency_dropdown = ttk.Combobox(self, textvariable=self.currency_var, values=currency_choices, state="readonly")
        currency_dropdown.pack(pady=5)
        currency_dropdown.bind("<<ComboboxSelected>>", self.update_currency_price)

        # Amount entry
        amount_label = tk.Label(self, text="Enter amount")
        amount_label.pack(pady=5)
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(pady=5)

        # Convert button
        convert_button = tk.Button(self, text="Convert Currency", command=self.convert_currency)
        convert_button.pack(pady=10)

        # Result label
        self.result_label = tk.Label(self, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

        # Created by label
        created_by_label = tk.Label(self, text="Created by Padchayapong K.")
        created_by_label.pack(side=tk.BOTTOM, pady=10)

    def get_latest_price(self, currency):
        try:
            price = self.btc_converter.get_latest_price(currency)
            return f"{price:.2f} {currency}"
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return "N/A"

    def update_currency_price(self, event):
        currency = self.currency_var.get()
        price = self.get_latest_price(currency)
        self.result_label.config(text=f"Current price: {price}", foreground="green")

    def convert_currency(self):
        currency = self.currency_var.get()
        if currency == "Currency":
            messagebox.showerror("Error", "Please select a currency.")
            return

        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        try:
            btc_amount = self.btc_converter.convert_to_btc(amount, currency)
            result_text = f"{amount} {currency} = {btc_amount:.8f} BTC"
            self.result_label.config(text=result_text, foreground="black")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = BitcoinConverter()
    app.mainloop()