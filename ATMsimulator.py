balance = 1000.0

while True:
    print("=====ATM Simulator=====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        print(f"\nYour current balance is: ${balance}")
    elif choice ==2:
        amount = float(input("\nEnter amount to deposit: $"))
        if amount>0:
            balance += amount
            print(f"${amount} deposit successfully!")
        else:
            print("Invalid amount! Please try again")
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: $"))
        if amount <= 0:
            print("Invalid amount. Please try again.")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"${amount} withdrawn successfully!")
    elif choice == 4:
        print("\nThank you for using our ATM. Goodbye! 👋")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 4.")