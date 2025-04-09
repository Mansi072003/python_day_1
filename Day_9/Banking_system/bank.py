def display_menu():
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def atm():
    balance = 1000.0  

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(f"Your current balance is: Rs{balance:.2f}")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"Rs{amount:.2f} deposited successfully.")
                print(f"New balance: Rs{balance:.2f}")
            else:
                print("Invalid deposit amount.")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Invalid withdrawal amount.")
            elif amount > balance:
                print("Insufficient balance! Withdrawal denied.")
            else:
                balance -= amount
                print(f"Rs{amount:.2f} withdrawn successfully.")
                print(f"Remaining balance: Rs{balance:.2f}")

        elif choice == "4":
            print("Thank you for using our ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    print("Welcome to the ATM!")
    atm()
