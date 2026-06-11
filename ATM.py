# ATM Program

PIN = "1234"
balance = 1000.0

entered_pin = input("Enter your PIN: ")

if entered_pin != PIN:
    print("Incorrect PIN. Access denied.")
else:
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(f"Current Balance: ₹{balance:.2f}")

        elif choice == "2":
            amount = float(input("Enter deposit amount: ₹"))
            if amount > 0:
                balance += amount
                print(f"₹{amount:.2f} deposited successfully.")
                print(f"Updated Balance: ₹{balance:.2f}")
            else:
                print("Please enter a valid amount.")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: ₹"))
            if amount <= 0:
                print("Please enter a valid amount.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print(f"₹{amount:.2f} withdrawn successfully.")
                print(f"Remaining Balance: ₹{balance:.2f}")

        elif choice == "4":
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")# ATM Program

PIN = "1234"
balance = 1000.0

entered_pin = input("Enter your PIN: ")

if entered_pin != PIN:
    print("Incorrect PIN. Access denied.")
else:
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(f"Current Balance: ₹{balance:.2f}")

        elif choice == "2":
            amount = float(input("Enter deposit amount: ₹"))
            if amount > 0:
                balance += amount
                print(f"₹{amount:.2f} deposited successfully.")
                print(f"Updated Balance: ₹{balance:.2f}")
            else:
                print("Please enter a valid amount.")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: ₹"))
            if amount <= 0:
                print("Please enter a valid amount.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print(f"₹{amount:.2f} withdrawn successfully.")
                print(f"Remaining Balance: ₹{balance:.2f}")

        elif choice == "4":
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")