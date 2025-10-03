import tkinter as tk
from tkinter import messagebox
import random

class RouletteGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Roulette Game")

        self.balance = tk.DoubleVar(value=100.0)
        self.bet_amount = tk.DoubleVar(value=0.0)
        self.bet_choice = tk.StringVar(value="red")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Balance:").grid(row=0, column=0)
        tk.Label(self.root, textvariable=self.balance).grid(row=0, column=1)

        tk.Label(self.root, text="Bet Amount:").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.bet_amount).grid(row=1, column=1)

        tk.Label(self.root, text="Bet on (red/black/green):").grid(row=2, column=0)
        tk.Entry(self.root, textvariable=self.bet_choice).grid(row=2, column=1)

        bet_values = [0.25, 0.5, 1, 2, 4]
        for i, val in enumerate(bet_values):
            tk.Button(self.root, text=f"Bet {val}", command=lambda v=val: self.place_bet(v)).grid(row=3, column=i)

        tk.Button(self.root, text="Place Bet", command=self.place_bet).grid(row=4, columnspan=5)

    def place_bet(self, amount=None):
        if amount is None:
            amount = self.bet_amount.get()
        choice = self.bet_choice.get().lower()

        if amount <= 0:
            messagebox.showerror("Invalid Bet", "Bet amount must be greater than zero.")
            return

        if choice not in ["red", "black", "green"]:
            messagebox.showerror("Invalid Choice", "You can only bet on 'red', 'black', or 'green'.")
            return

        if amount > self.balance.get():
            messagebox.showerror("Invalid Bet", "You do not have enough balance to place this bet.")
            return

        outcome = self.spin_roulette()
        self.update_balance(choice, outcome, amount)

    def spin_roulette(self):
        outcome = random.choices(
            ["red", "black", "green"],
            [18/37, 18/37, 1/37]
        )[0]
        messagebox.showinfo("Roulette Outcome", f"The ball landed on {outcome}!")
        return outcome

    def update_balance(self, choice, outcome, amount):
        if outcome == choice:
            if choice == "green":
                self.balance.set(self.balance.get() + amount * 35)  # Green pays 35 to 1
            else:
                self.balance.set(self.balance.get() + amount)  # Red/Black pays 1 to 1
        else:
            self.balance.set(self.balance.get() - amount)

        if self.balance.get() <= 0:
            messagebox.showinfo("Game Over", "You have run out of balance! Game over.")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = RouletteGame(root)
    root.mainloop()
