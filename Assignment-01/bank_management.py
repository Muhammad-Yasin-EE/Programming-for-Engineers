# Name: Muhammad Yasin
# CMS ID: 033-25-0040
# Class: BEE-II
# Assignment 01 - Bank Management System (Mini Project)

"""
Bank Management System (Mini Project)
Assignment 01 - Python

A menu-driven program that simulates basic banking operations:
Deposit, Withdraw, and Check Balance.
"""

# Global variables to hold account info
account_holder = ""
balance = 0.0


def initialize_account():
    """Ask the user for account holder name and initial balance."""
    global account_holder, balance

    account_holder = input("Enter Account Holder Name: ")

    while True:
        try:
            balance = float(input("Enter Initial Balance: "))
            if balance >= 0:
                break
            else:
                print("Initial balance must be zero or positive. Try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    print(f"\nAccount created successfully for {account_holder}!")
    print(f"Starting Balance: {balance}\n")


def deposit():
    """Handle deposit functionality."""
    global balance
    try:
        amount = float(input("Enter deposit amount: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    if amount <= 0:
        print("Deposit amount must be positive.")
    else:
        balance += amount
        print(f"Deposit successful! Updated Balance: {balance}")


def withdraw():
    """Handle withdraw functionality."""
    global balance
    try:
        amount = float(input("Enter withdrawal amount: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    if amount <= 0:
        print("Withdrawal amount must be positive.")
    elif amount > balance:
        print("Insufficient balance! Withdrawal denied.")
    else:
        balance -= amount
        print(f"Withdrawal successful! Updated Balance: {balance}")


def check_balance():
    """Display the current balance."""
    print(f"Account Holder: {account_holder}")
    print(f"Current Balance: {balance}")


def show_menu():
    """Display the main menu."""
    print("\n----- BANK MANAGEMENT SYSTEM -----")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")


def main():
    """Main program loop."""
    initialize_account()

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            check_balance()
        elif choice == "4":
            print(f"\nThank you for banking with us, {account_holder}!")
            print("Program terminated.")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 4.")


if __name__ == "__main__":
    main()
