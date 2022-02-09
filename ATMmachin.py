import time

print("Please enter your CARD")

time.sleep(5)

password = 9135
pin = int(input("Enter your four digit pin: "))

balance = 5000


if pin == password:
    while True:
        print("""
            1 == balence 
            2 == Withdraw Balence
            3 == Deposit Balence
            4 == Exit 
            """)
        try:
            option = int(input("Please enter your choice: "))
        except:
            print("Please enter valid option")

        if option == 1:
            print(f"Your current balance is {balance}")

        if option == 2:
            withdraw_amount = int(input("Please enter withdraw amount: "))
            balance = balance - withdraw_amount
            print('='*30)
            print('='*30)
            
            print(f"{withdraw_amount} is debited from your account")
            print(f"Your updated balance is {balance}")
            print('='*30)
            print('='*30)

        if option == 3:
            deposit_amount = int(input("Please enter deposit amount: "))
            balance = balance + deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"your updated balance is {balance}")
           

        if option == 4:
            break

else:
    print("Wrong your pin please try again")
