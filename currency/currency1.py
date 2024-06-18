import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Your API key from ExchangeRate-API
API_KEY = '4fe058c6a0ef3e2c571d9947'  # Replace with your actual API key

# Function to get exchange rates
def get_exchange_rate(from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{from_currency}/{to_currency}"
    print(f"Calling API: {url}")  # Debug: Print the API URL
    response = requests.get(url)
    print(f"API Response: {response.status_code}")  # Debug: Print the status code
    data = response.json()
    if response.status_code == 200:
        print(f"Conversion Rate: {data['conversion_rate']}")  # Debug: Print the conversion rate
        return data['conversion_rate']
    else:
        messagebox.showerror("Error", data.get('error-type', 'Unknown error occurred'))
        return None

# Function to perform conversion
def convert_currency():
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    amount = amount_var.get()

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number")
        return

    rate = get_exchange_rate(from_currency, to_currency)

    if rate is not None:
        converted_amount = amount * rate
        result_label.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")

# Function to handle the exit
def handle_exit():
    window.destroy()

# GUI setup
window = tk.Tk()

# Function to toggle fullscreen
def toggle_fullscreen(event=None):
    state = not window.attributes('-fullscreen')
    window.attributes('-fullscreen', state)
    if state:
        window.attributes('-zoomed', True)  # For Windows systems to maximize window
    else:
        window.attributes('-zoomed', False)

# Function to minimize window
def minimize_window(event=None):
    window.iconify()

# Bind keys to functions
window.bind('<F11>', toggle_fullscreen)  # Bind F11 key to toggle fullscreen
window.bind('<Escape>', toggle_fullscreen)  # Bind Escape key to exit fullscreen
window.bind('<F10>', minimize_window)  # Bind F10 key to minimize window

window.title("Currency Converter")
window.geometry("400x300")
window.config(bg='#F0F0F0')

# Currency options
currencies = ['USD', 'EUR', 'GBP', 'INR', 'AUD', 'CAD', 'SGD', 'JPY', 'CNY']

# Labels and entry
amount_var = tk.StringVar()
amount_label = tk.Label(window, text="Amount:", bg='#F0F0F0')
amount_label.grid(row=0, column=0, padx=10, pady=10)
amount_entry = tk.Entry(window, textvariable=amount_var)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

from_currency_var = tk.StringVar(value='USD')
from_currency_label = tk.Label(window, text="From Currency:", bg='#F0F0F0')
from_currency_label.grid(row=1, column=0, padx=10, pady=10)
from_currency_menu = ttk.Combobox(window, textvariable=from_currency_var, values=currencies)
from_currency_menu.grid(row=1, column=1, padx=10, pady=10)

to_currency_var = tk.StringVar(value='EUR')
to_currency_label = tk.Label(window, text="To Currency:", bg='#F0F0F0')
to_currency_label.grid(row=2, column=0, padx=10, pady=10)
to_currency_menu = ttk.Combobox(window, textvariable=to_currency_var, values=currencies)
to_currency_menu.grid(row=2, column=1, padx=10, pady=10)

# Convert button
convert_button = tk.Button(window, text="Convert", command=convert_currency, bg='#007BFF', fg='white')
convert_button.grid(row=3, column=0, columnspan=2, pady=20)

# Result label
result_label = tk.Label(window, text="", bg='#F0F0F0', font=("Arial", 12, "bold"))
result_label.grid(row=4, column=0, columnspan=2)

# Exit button
exit_button = tk.Button(window, text="Exit", command=handle_exit, bg='#DC3545', fg='white')
exit_button.grid(row=5, column=0, columnspan=2, pady=10)

window.mainloop()
