def Check_Balance():
    
    print("="*25)
    print(f"Your Balance is {balance}")


def Deposite():
    
    print("="*25)
    global balance
    amount = float(input("Enter your amount to deposite\n =>"))
    if amount >= 0 :
        balance += amount
    else :
        print("Enter positive amount")
    
def Withdraw():
    print("="*25)
    global balance
    amount = float(input("Enter withdraw amount\n =>"))
    if amount <= 0 :
        print("Can't withdraw 'negative' or 'Zero' amount")
    elif amount < balance :
        balance -= amount
    else :
        print(f"Your Balance is {balance}")
        print("Enter less amount than balance")
        Withdraw()

balance = 0.0
print("Wellcome to ABC bank")
while True :
    print("="*25)
    print("1. Check Balance")
    print("2. Deposite an amount")
    print("3. Withdraw an amount")
    print("4. Quit")
    print()
    choice = input("Enter your choice(1-4): ")

    if choice == '1' :
        Check_Balance()
    elif choice == '2' :
        Deposite()
    elif choice == '3' :
        Withdraw()
    elif choice == '4' :
        break
    else :
        print("Enter valid input")
print("="*25)
print("Thank you for Banking with us")