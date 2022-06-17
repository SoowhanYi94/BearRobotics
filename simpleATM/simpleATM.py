
#Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw
from User import User
from CashBin import Cashbin
# I have created my own account here to show the account information
# Future new users can be added by add_user function
# I also created friends list and cash bin for convinience

cash_bin = Cashbin()
def validate_card():
    # I would like to give it a time limit here if I was to implement the verification
    # time limit in seconds and after 100 seconds it will return to the initial stage
    # I will assume that the card is verified nomatter what
    # while (timelimit < 100) :  
    #     if (cardInserted) :
    #         return verify(card)
    # return False
    
    return True

def extract_info(user) :
    # Extracts information from the card
    # card should be added as a parameter here but we are not using real card yet.
    # For this project I just made an fake account. Also the pin is not known when we are extracting information from the card.
    user.name = "Steve"
    user.bank = "Bank of Korea"
    user.account_num = 111111111111
    user.card_num = "000000000001"
    # user.pin = 1234
    user.balance = 9999
    user.friends = dict()
    
def verify_pin(user, pin):
    ## According to the problem statement, we are not supposed to know the pin when wer are extracting information from the card. so I made a separate function in order to verify the pin from the server or something.
    ## For now, it is just returning true meaning that the pin is verified no matter what
    return True

def withdraw_cash_atm(user: User) -> bool:
    ## 1. amount of money to withdraw
    amount = 0
    while(True):
        try:
            amount = int(input("Enter the amount of money you want to withdraw: "))
            if (amount <= 0):
                print("You cannot withdraw negative amount or zero amount")
                continue
            
        except ValueError:
            print("Enter the correct numbers")
        if (amount <= user.balance and amount > 0):
            break   
    ## 2. check if enough money in atm
    if not check_cash_bin(amount):
        return False
    ## 3. request withdrawl from the account
    ## 4. if true, withdraw from the atm
    ## 5. show the remaining balance
    if (user.withdraw_cash(amount)):
        cash_bin.cash -= amount
        # user.balance_enquiry()
    else :
        print("Money has not been withdrawn from your account")
        return False
    return True

## This is needs to be integrated with the bank system or the atm machine to check the real amount
## This just returns true if the user agrees with the amount. 
def check_amount_cash(amount: int) -> bool:
    ## cash counted is the cash that the atm counted
    ## for now, i set this equal to the amount that is input. 
    cash_counted = amount
    agree = input(f"{cash_counted} Is this amount correct?: (y/n)")
    while(agree != 'y' and agree != 'n'):
        agree = input("Is this amount correct?: (y/n)")
    return agree == 'y'

def check_cash_bin(amount: int):
    if cash_bin.cash < amount :
        print("We do not have enough money to dispense")
        return False
    return True

def deposit_cash_atm(user: User) -> bool:
    ## 1. amount of money to deposit
    amount = 0
    while(True):
        try:
            amount = int(input("Enter the amount of money you want to deposit: "))
            if (amount <= 0):
                print("You cannot deposit negative amount or zero amount")
                continue
            
        except ValueError:
            print("Enter the correct numbers")
        if (amount < user.balance and amount > 0):
            break 
    ## 2. check if the correct amount has been putted
    ## 3. if true request deposit to the account
        ## if not show the amount that the machine counted
        ## if they dont agree it needs to dispense the money that was given
    ## 4. finish & show the remaining balance
    count = 0
    while(not check_amount_cash(amount)):
         amount = int(input("Enter the amount of money you have put: "))
         count+=1
         if count > 5:
             print("Cash amount is not correct. Please try again")
             return False
    if (user.deposit_cash(amount)):
        cash_bin.cash += amount
    else : 
        user.balance_enquiry()
        return False
    user.balance_enquiry()
    return True
   
def balance_enquiry_atm(user: User):
    ## 1. just show the balance of the user
    user.balance_enquiry()
def input_amount():
    while(True):
        try:
            amount = int(input("Enter the amount of money you want to transfer: "))
            if (amount <= 0):
                print("You cannot transfer negative amount or zero amount")
                continue
            return amount
        except ValueError:
            print("Enter the correct numbers")
def transfer_money_atm(user: User) -> bool:
    ## 1. amount of money to transfer
    ## 2. name and account number of the recipient
    ## 3. verify if the name and account number is in the system
    ## 4. if verified, transfer the money
        ## if not, ask for the name and account number again
    ## 5. request the transfer to the user
    ## 6. show the remaining balance
    amount = input_amount()
    return user.transfer_money(amount)
    
def transfer_money_friend_atm(user: User) -> bool:
    ## 1. amount of money to transfer
    ## 2. choose friend from the friend list
    ## 2 - 1. if the friend list is empty, then request for the name and number
    ## 2 - 2. verify the new friend 
    ## 3. request transfer to the user
    ## 4. finish and show the remaining balance
    amount = input_amount()
    return user.transfer_money_friend(amount)

def add_friend_atm(user: User):
    user.add_friend()
    
def manage_friends_atm(user: User):
    print(" Enter 1 to Add friend \n Enter 2 to Delete friend \n Enter 3 to View friend list \n ")
    num = input("Enter the number corresponding to the activity: ")
    if num == "1":
        user.add_friend()
    elif num == "2":
        user.delete_friend()
    elif num == "3":
        user.view_friend()
    else:
        print("Please enter the correct number")
    
def FSM(user):
    quit = False 
    while quit == False:
        print(" Enter 1 to Widthdraw Cash \n Enter 2 to Deposit Cash \n Enter 3 to See the Balance \n Enter 4 to Transfer money \n Enter 5 to Transfer money to friend  \n Enter 6 to Manage friends \n Enter 7 to See my Information \n Enter 8 to quit \n")

        query = input("Enter the number corresponding to the activity you want to do: ")
        print("\n")
        if query == "1":
            withdraw_cash_atm(user)
        elif query == "2":
            deposit_cash_atm(user)
        elif query == "3":
            balance_enquiry_atm(user)
        elif query == "4":
            transfer_money_atm(user)
        elif query == "5":
            transfer_money_friend_atm(user)
        elif query == "6":
            manage_friends_atm(user)
        elif query == "7":
            user.print_my_account()
        elif query == "8":
            quit = True
        else:
            print("Please enter a correct value")


## If the user inputs the wrong pin number more than 5 times, the account will be locked and asked to call the bank.
## verify_pin is the function for checking pin number but it only returns true for now because it needs the server for the pin number.              
def login(user: User) -> bool:
    wrongcnt = 0
    if user.locked :
        print ("You have entered wrong passward more than 5 times. Your account has been locked. Please contact your bank")
        return False
    while wrongcnt < 5:
        pin = int(input('Please enter your four digit pin: '))
        if verify_pin(user, pin):
            return True
        else:
            print("Entered wrong pin")
            wrongcnt+=1
    print ("You have entered passward more than 5 times wrong. Your account has been locked")
    user.locked = True
    return False

    
if __name__ == '__main__':
    user = User()

    # create_fake_users()
    print('Please insert your card')
    ## Now I will assume the card has been inserted.
    ## it will not get out of the while loop until the valid card is inserted. 
    validate_card()
        
    ## Now I will assume that the valid card has been inserted
    ## This should be extract_info(user, card) in order to extract info from the card. However, I do not intend to use real card yet.
    extract_info(user) 
    
    if (login(user)):
        FSM(user)
    
    
        
