print("")  
print("Welcome to ATM")  
print("")  
print()  

# Account details: {Account Number: [Name, DOB, Balance, PIN, Savings]}
accounts = {  
    1001: ["User 1", "24-08-2024", 10000, 2408, 5000],  
    1002: ["User 2", "16-07-2024", 20000, 1234, 7000],  
    1003: ["User 3", "20-01-2024", 5000, None, 2000]      
}  

dobm = {1: "January", 2: "Feb", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July",  
        8: "August", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}  

while True:  
    print("Choose Your Option")  
    print("1. Withdrawal")  
    print("2. Deposit")  
    print("3. Pin Generation")  
    print("4. Mini Statement")  
    print("5. Fast Cash")  
    print("6. Quick Cash")  
    print("7. Savings")  
    print("8. Exit")  
    option = int(input("Enter Your Option: "))  
    print()  

    if option == 1:  # Withdrawal  
        print("")  
        accno = int(input("Enter Account Number: "))  
        if accno not in accounts:  
            print("Account Does not Exist!")  
        else:  
            pin = int(input("Enter Pin: "))  
            if accounts[accno][3] is None:  
                print("Generate Pin First")  
            elif accounts[accno][3] != pin:  
                print("Invalid Pin")  
            else:  
                amt = int(input("Enter Amount to Withdraw: "))  
                if amt > accounts[accno][2]:  
                    print("Insufficient Funds")  
                else:  
                    accounts[accno][2] -= amt  
                    print("Withdrawal Successful!")  
        print("")  

    elif option == 2:  # Deposit  
        print("")  
        accno = int(input("Enter Account Number: "))  
        if accno not in accounts:  
            print("Account does not Exist")  
        else:  
            amt = int(input("Enter Amount to Deposit: "))  
            accounts[accno][2] += amt  
            print("Deposit Successful")  
        print("")  

    elif option == 3:  # Pin Generation  
        print("")  
        accno = int(input("Enter Account Number: "))  
        if accno not in accounts:  
            print("Account Does not Exist")  
        else:  
            if accounts[accno][3] is None:  
                pin = int(input("Enter Pin: "))  
                cpin = int(input("Confirm Pin: "))  
                if pin != cpin:  
                    print("Pin Does Not Match")  
                else:  
                    accounts[accno][3] = pin  
                    print("Pin Generated Successfully")  
            else:  
                print("Pin Already Exists")  
        print("")  

    elif option == 4:  # Mini Statement  
        print("")  
        accno = int(input("Enter Account Number: "))  
        if accno not in accounts:  
            print("Account Does not Exist")  
        else:  
            pin = int(input("Enter Pin: "))  
            if pin != accounts[accno][3]:  
                print("Invalid Pin")  
            else:  
                print(f"Name: {accounts[accno][0]}")  
                print(f"Account Number: {accno}")  
                dob = accounts[accno][1].split("-")  
                date, month, year = dob[0], dobm[int(dob[1])], dob[2]  
                print(f"Date of Birth: {date}-{month}-{year}")  
                print(f"Account Balance: {accounts[accno][2]}")  
                print(f"Savings Balance: {accounts[accno][4]}")  
        print("")  

    elif option == 5:  # Fast Cash (Predefined amounts)  
        print("")  
        accno = int(input("Enter Account Number: "))  
        if accno not in accounts:  
            print("Account Does not Exist!")  
        else:  
            pin = int(input("Enter Pin: "))  
            if accounts[accno][3] != pin:  
                print("Invalid Pin")  
            else:  
                print("Select Fast Cash Amount:")  
                print("1. $500\n2. $1000\n3. $2000\n4. $5000")  
                choice = int(input("Enter Option: "))  
                fast_cash_amounts = {1: 500, 2: 1000, 3: 2000, 4: 5000}  
                if choice in fast_cash_amounts and fast_cash_amounts[choice] <= accounts[accno][2]:  
                    accounts[accno][2] -= fast_cash_amounts[choice]  
                    print("Fast Cash Withdrawal Successful!")  
                else:  
                    print("Invalid Choice or Insufficient Balance")  
        print("")  

    elif option == 6:  # Quick Cash (Custom fast withdrawal)  
        print("")  
        accno = int(input("Enter Account Number: "))  
        if accno not in accounts:  
            print("Account Does not Exist!")  
        else:  
            pin = int(input("Enter Pin: "))  
            if accounts[accno][3] != pin:  
                print("Invalid Pin")  
            else:  
                amt = int(input("Enter Quick Cash Amount: "))  
                if amt > accounts[accno][2]:  
                    print("Insufficient Funds")  
                else:  
                    accounts[accno][2] -= amt  
                    print("Quick Cash Withdrawal Successful!")  
        print("")  

    elif option == 7:  # Savings (Transfer money between main balance and savings)  
        print("")  
        accno = int(input("Enter Account Number: "))  
        if accno not in accounts:  
            print("Account Does not Exist!")  
        else:  
            pin = int(input("Enter Pin: "))  
            if accounts[accno][3] != pin:  
                print("Invalid Pin")  
            else:  
                print("1. Transfer to Savings")  
                print("2. Transfer to Main Account")  
                choice = int(input("Enter Option: "))  
                amt = int(input("Enter Amount: "))  

                if choice == 1:  # Transfer to Savings  
                    if amt > accounts[accno][2]:  
                        print("Insufficient Balance")  
                    else:  
                        accounts[accno][2] -= amt  
                        accounts[accno][4] += amt  
                        print("Amount Transferred to Savings")  

                elif choice == 2:  # Transfer to Main Balance  
                    if amt > accounts[accno][4]:  
                        print("Insufficient Savings Balance")  
                    else:  
                        accounts[accno][4] -= amt  
                        accounts[accno][2] += amt  
                        print("Amount Transferred to Main Account")  

                else:  
                    print("Invalid Option")  
        print("")  

    else:  # Exit  
        print("Thank you for using our ATM!")  
        break