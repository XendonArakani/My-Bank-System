#  Imports for the tkinter programs
import tkinter
import customtkinter

# Class that defines the blueprint for the object and contains depositing, withdrawing, history. 
class bankAccount:
    def __init__(self, name, accountNumber, balance):
        self.name = name  
        self.accountNumber = accountNumber  
        self.balance = balance  
        self.transactionHistory = []  

    # Records and does addition during withdraw
    def deposit(self, amount):
        self.balance += amount
        self.transactionHistory.append(f"Deposited ${amount}")

    # Records and does subtraction during withdraw
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactionHistory.append(f"Withdrew ${amount}")
        else:
            print("Insufficient balance!")

    # Returns history as a string
    def transaction_history(self):
        return "\n".join(self.transactionHistory)

# Create a window called bank
bankApp = customtkinter.CTk()
bankApp.geometry("720x480")
bankApp.title("Bank")

# Window title
title = customtkinter.CTkLabel(bankApp, text="Bank Account: ")
title.pack(padx=10, pady=10)

# Account info for Jorge
jorgeAccount = bankAccount("Joe", "12476", 1000)

# Label to display balance
balanceLabel = customtkinter.CTkLabel(bankApp, text=f"Balance: ${jorgeAccount.balance}")
balanceLabel.pack()

# Input box for money amount
amount_variable = tkinter.StringVar()
amountInput = customtkinter.CTkEntry(bankApp, placeholder_text="Enter Dollar Amount: ", width=350, height=40, border_width=2, border_color="green", textvariable=amount_variable)
amountInput.pack()

# Function withdraws the money
def withdraw_money():
    try:
        amount = float(amount_variable.get())
        jorgeAccount.withdraw(amount)
        balanceLabel.configure(text=f"Balance: ${jorgeAccount.balance}")
    except ValueError:
        pass

# Money withdraw button
withdrawButton = customtkinter.CTkButton(bankApp, text="Withdraw", command=withdraw_money)
withdrawButton.pack(padx=10, pady=10)

# Function deposits the money
def deposit_money():
    try:
        amount = float(amount_variable.get())
        jorgeAccount.deposit(amount)
        balanceLabel.configure(text=f"Balance: ${jorgeAccount.balance}")
    except ValueError:
        pass

# Money deposit button
depositButton = customtkinter.CTkButton(bankApp, text="Deposit", command=deposit_money)
depositButton.pack(padx=10, pady=10)

# Function to show transaction history
def show_transaction_history():
    history = jorgeAccount.transaction_history()
    historyWindow = tkinter.Tk()
    historyWindow.geometry("720x480")
    historyWindow.title("Transaction History")
    historyLabel = tkinter.Label(historyWindow, text=f"Transaction History:\n{history}")
    historyLabel.pack()

# Button for history
historyButton = customtkinter.CTkButton(bankApp, text="Transaction History", command=show_transaction_history)
historyButton.pack(padx=10, pady=10)

# Labels for the account name and number
nameLabel = customtkinter.CTkLabel(bankApp, text=f"Name: {jorgeAccount.name}")
nameLabel.pack()
accLabel = customtkinter.CTkLabel(bankApp, text=f"Account Number: {jorgeAccount.accountNumber}")
accLabel.pack()

# Starts the loop
bankApp.mainloop()