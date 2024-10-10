import tkinter as tk
from tkinter import ttk, messagebox
import requests

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("400x350")
        self.root.configure(bg="#f0f8ff")

        # Fixer.io API key (replace with your own API key)
        self.api_key = 'YOUR_FIXER_API_KEY'
        self.url = f'http://data.fixer.io/api/latest?access_key={self.api_key}'
        self.rates = self.get_conversion_rates()

        self.create_widgets()

    def get_conversion_rates(self):
        try:
            response = requests.get(self.url)
            data = response.json()

            if data["success"]:
                return data["rates"]
            else:
                raise Exception(data["error"]["info"])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch conversion rates: {e}")
            return {}

    def create_widgets(self):
        # Title
        title_label = ttk.Label(self.root, text="Currency Converter", font=("Arial", 20), background="#f0f8ff")
        title_label.pack(pady=10)

        # Amount Entry
        self.amount_label = ttk.Label(self.root, text="Amount:", background="#f0f8ff")
        self.amount_label.pack(pady=5)

        self.amount_entry = ttk.Entry(self.root)
        self.amount_entry.pack(pady=5)

        # From Currency Dropdown
        self.from_currency_label = ttk.Label(self.root, text="From Currency:", background="#f0f8ff")
        self.from_currency_label.pack(pady=5)

        self.from_currency = ttk.Combobox(self.root, values=list(self.rates.keys()), state="readonly")
        self.from_currency.pack(pady=5)
        self.from_currency.set("USD")

        # To Currency Dropdown
        self.to_currency_label = ttk.Label(self.root, text="To Currency:", background="#f0f8ff")
        self.to_currency_label.pack(pady=5)

        self.to_currency = ttk.Combobox(self.root, values=list(self.rates.keys()), state="readonly")
        self.to_currency.pack(pady=5)
        self.to_currency.set("EUR")

        # Convert Button
        self.convert_button = ttk.Button(self.root, text="Convert", command=self.convert_currency)
        self.convert_button.pack(pady=20)

        # Result Label
        self.result_label = ttk.Label(self.root, text="", font=("Arial", 14), background="#f0f8ff")
        self.result_label.pack(pady=10)

    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency.get()
            to_currency = self.to_currency.get()

            if not from_currency or not to_currency:
                raise ValueError("Please select both currencies.")

            if from_currency != 'EUR':
                amount = amount / self.rates[from_currency]

            result = round(amount * self.rates[to_currency], 2)
            self.result_label.config(text=f"{self.amount_entry.get()} {from_currency} = {result} {to_currency}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
