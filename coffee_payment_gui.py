import tkinter as tk
from tkinter import messagebox, ttk
import random

class CoffeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Payment Selector")
        self.root.geometry("800x600")

        self.profiles = ["Profile 1", "Profile 2", "Profile 3"]
        self.selected_profile = tk.StringVar()
        self.selected_profile.set(self.profiles[0])

        self.profile_label = tk.Label(root, text="Select profile:")
        self.profile_label.pack()

        self.profile_dropdown = ttk.Combobox(root, textvariable=self.selected_profile, values=self.profiles, state="readonly")
        self.profile_dropdown.pack()

        self.load_button = tk.Button(root, text="Load", command=self.load_data)
        self.load_button.pack()

        self.save_button = tk.Button(root, text="Save", command=self.save_data)
        self.save_button.pack()

        self.coworkers_label = tk.Label(root, text="Enter coworker names and the price of their drink:")
        self.coworkers_label.pack()

        self.coworker_entries = []
        self.coworker_prices = {}
        for i in range(7):
            frame = tk.Frame(root)
            frame.pack()
            coworker_label = tk.Label(frame, text=f"Coworker {i+1}:")
            coworker_label.pack(side="left")
            self.coworker_entries.append(tk.Entry(frame))
            self.coworker_entries[i].pack(side="left")

            price_label = tk.Label(frame, text="Price:")
            price_label.pack(side="left")
            self.coworker_prices[self.coworker_entries[i]] = tk.Entry(frame)
            self.coworker_prices[self.coworker_entries[i]].pack(side="left")

        self.add_order_button = tk.Button(root, text="Generate name", command=self.add_order)
        self.add_order_button.pack()

    def add_order(self):
        coworkers = [entry.get() for entry in self.coworker_entries if entry.get()]
        if len(coworkers) < 2:
            messagebox.showerror("Error", "Please enter at least two coworkers.")
            return
        prices = {}
        for entry, price_entry in self.coworker_prices.items():
            name = entry.get()
            if name:
                price = price_entry.get()
                if not price:
                    messagebox.showerror("Error", f"Please enter price for {name}.")
                    return
                try:
                    prices[name] = float(price)
                except ValueError:
                    messagebox.showerror("Error", f"Please enter valid price for {name}.")
                    return
        if not prices:
            messagebox.showerror("Error", "Please enter prices for all coworkers.")
            return
        weights = {coworker: price for coworker, price in prices.items()}
        selected_coworker_name = random.choices(list(weights.keys()), weights=list(weights.values()))[0]
        messagebox.showinfo("Payment Selector", f"{selected_coworker_name} will pay for coffee today.")

    def save_data(self):
        profile_name = self.selected_profile.get()
        filename = f"data_{profile_name}.txt"
        with open(filename, "w") as f:
            for entry, price_entry in zip(self.coworker_entries, self.coworker_prices.values()):
                name = entry.get()
                price = price_entry.get()
                if name and price:
                    f.write(f"{name},{price}\n")
        messagebox.showinfo("Info", f"Data saved successfully for {profile_name}.")

    def load_data(self):
        profile_name = self.selected_profile.get()
        filename = f"data_{profile_name}.txt"
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    name, price = line.strip().split(",")
                    if i < len(self.coworker_entries):
                        self.coworker_entries[i].delete(0, tk.END)
                        self.coworker_entries[i].insert(0, name)
                        self.coworker_prices[self.coworker_entries[i]].delete(0, tk.END)
                        self.coworker_prices[self.coworker_entries[i]].insert(0, price)
        except FileNotFoundError:
            messagebox.showinfo("Info", f"No previous data found for {profile_name}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeApp(root)
    root.mainloop()