import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Function to calculate SIP
def calculate_sip():
    principal = principal_slider.get()
    interest_rate = interest_slider.get() / 100
    years = years_slider.get()

    # Calculate SIP amount
    amount = principal * ((1 + interest_rate / 12) ** (12 * years) - 1) / (interest_rate / 12)

    result_label.config(text=f"Your SIP Amount: ₹{amount:.2f}")


# Function to update result label in real-time
def update_result(*args):
    principal = principal_slider.get()
    interest_rate = interest_slider.get() / 100
    years = years_slider.get()

    # Calculate SIP amount
    amount = principal * ((1 + interest_rate / 12) ** (12 * years) - 1) / (interest_rate / 12)

    result_label.config(text=f"Your SIP Amount: ₹{amount:.2f}")


# Create the main window
root = tk.Tk()
root.title("SIP Calculator")
root.geometry("400x300")  # Set window size

# Use the 'ttkthemes' library to apply a modern theme
style = ttk.Style()
style.theme_use("clam")

# Create and place labels with a modern look
principal_label = ttk.Label(root, text="Principal Amount (₹):", style="TLabel")
principal_label.grid(row=0, column=0, padx=10, pady=10)

interest_label = ttk.Label(root, text="Annual Interest Rate (%):", style="TLabel")
interest_label.grid(row=1, column=0, padx=10, pady=10)

years_label = ttk.Label(root, text="Years Invested:", style="TLabel")
years_label.grid(row=2, column=0, padx=10, pady=10)

result_label = ttk.Label(root, text="", style="TLabel")
result_label.grid(row=4, column=0, padx=10, pady=10)

# Create sliders for adjusting values
principal_slider = ttk.Scale(root, from_=1000, to=100000, length=300, orient="horizontal", command=update_result)
principal_slider.grid(row=0, column=1, padx=10, pady=10)

interest_slider = ttk.Scale(root, from_=1, to=20, length=300, orient="horizontal", command=update_result)
interest_slider.grid(row=1, column=1, padx=10, pady=10)

years_slider = ttk.Scale(root, from_=1, to=30, length=300, orient="horizontal", command=update_result)
years_slider.grid(row=2, column=1, padx=10, pady=10)

# Create and place calculate button
calculate_button = ttk.Button(root, text="Calculate SIP", command=calculate_sip, style="TButton")
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Start the Tkinter main loop
root.mainloop()
