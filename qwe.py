import tkinter as tk
from tkinter import ttk
import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data["rates"][target_currency]
    return exchange_rate

def convert_currency():
    base_currency = base_currency_combobox.get()
    target_currency = target_currency_combobox.get()
    amount = float(amount_entry.get())

    exchange_rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = amount * exchange_rate

    result_label.config(text=f"{amount} {base_currency} дорівнює {converted_amount:.2f} {target_currency}")

# Create the main window
root = tk.Tk()
root.title("Конвертор валют")

# Create and place widgets
base_currency_label = ttk.Label(root, text="Базова валюта:")
base_currency_label.grid(row=0, column=0, padx=10, pady=5)

base_currency_combobox = ttk.Combobox(root, values=["USD", "EUR", "UAH"], width=10)
base_currency_combobox.grid(row=0, column=1, padx=10, pady=5)
base_currency_combobox.set("USD")

amount_label = ttk.Label(root, text="Сума:")
amount_label.grid(row=1, column=0, padx=10, pady=5)

amount_entry = ttk.Entry(root, width=15)
amount_entry.grid(row=1, column=1, padx=10, pady=5)

target_currency_label = ttk.Label(root, text="Цільова валюта:")
target_currency_label.grid(row=2, column=0, padx=10, pady=5)

target_currency_combobox = ttk.Combobox(root, values=["USD", "EUR", "UAH"], width=10)
target_currency_combobox.grid(row=2, column=1, padx=10, pady=5)
target_currency_combobox.set("USD")

convert_button = ttk.Button(root, text="Конвертувати", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
