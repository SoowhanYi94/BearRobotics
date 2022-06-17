from dataclasses import dataclass
import string
## Intended to verify the account with name and account number. 
## It only returns true because we do not have the user data. 
def verify_account(name_recipient, account_num):
    return True
def input_name() -> string:
    while(True):
        try:
            name = input("Please enter the name of the friend: ")
            
            return name
        except ValueError:
            print("Enter the correct numbers")
            
def input_account_num() -> int:
    while(True):
        try:
            account_num = int(input("Enter the account number of the reciepent: ")) 
            return account_num
        except ValueError:
            print("Enter the correct numbers")
            
@dataclass
class User:
    name:string = None
    bank:string = None
    account_num:int = None
    card_num: string = None
    pin : int = None
    balance: int = None
    friends: dict = None
    locked: bool = False

    def __init__(self):
        self.name = None
        self.bank = "Bank of Korea"
        # self.account_num = self.account_num_generator()
        # self.card_num = self.card_num_generator()
        self.pin = 1111
        self.balance = 0
        self.friends = {}
        self.locked = False
    ## When adding friends, it only considers the redundancy of account number.
    def add_friend(self) :
        account_num = input_account_num()
        name = input_name()
        if (verify_account(name, account_num)) :
            if (account_num in self.friends.keys()):
                print("The friend is already in the friend list ")
            else:
                self.friends[account_num] = name
                print(f"Your friend {name} is added to your friends list")
        else:
            print("The account number and the name does not exist in the bank system")
        print("\n")
    def add_friend_(self, account_num: int, name: string) :
        if (verify_account(name, account_num)) :
            if (account_num not in self.friends.keys()):
                self.friends[account_num] = name
                print(f"Your friend {name} is added to your friends list")
            else:
                print("The friend is already in the friend list ")
        else:
            print("The account number and the name does not exist in the bank system")
        print("\n")
    def delete_friend(self):
        if (len(self.friends) <1 ) :
            print("You do not have friends on the list. please add your friend")
            return False
        
        num_friend = 1
        friends_names = list(self.friends.values())
        friends_keys = list(self.friends.keys())
        while (1):
            
            for i in range(len(friends_names)):
                print(f"{i + 1} {friends_names[i]}  \n")
            
            while(True):
                try:
                    num_friend = int(input("Choose the coreesponding number: "))
                    break
                except ValueError:
                    print("Enter the correct number")
            if (num_friend <= len(self.friends) and num_friend > 0):
                break
            else:
                print("Please choose the number corresponding to the recipient")

        self.friends.pop(friends_keys[num_friend-1], None)
    def view_friend(self):
        if len(self.friends) == 0: 
            print("Friend list is empty")
            return False
        n = 1
        for i in self.friends:
            print(f"{n}. Name: {self.friends[i]} Account number: {i} ")
            n+=1
        print("\n")
        
    def balance_enquiry(self):
        print(f"Total balance {self.balance} Dollars")
        print('')
        
    def deposit_cash(self, amount: int) -> bool:
        if (amount < 0) :
            print ("You cannot deposit negative amount.")
            return False
        else :
            self.balance += amount
            self.balance_enquiry
        return True
            

    def withdraw_cash(self, amount):
        if (amount < 0) :
            print ("You cannot widthraw negative amount")
        elif amount > self.balance:
            print("You don't have sufficient balance to make this widthdrawal")
        else:
            self.balance = self.balance - amount
            print('')
            self.balance_enquiry()
            return True
        self.balance_enquiry()
        print("why?")
        return False
            
            
   
    ## When transfering money to another account, I did not consider that the other account is real or not. I have the method for verifying accounts but it only returns true as we do not have the bank system to prove the account is in the system. 
    def transfer_money(self, amount: int) -> bool:
        if (amount > self.balance) :
            print ("You do not have sufficient balance to make this transfer")
            self.balance_enquiry()
            return False
        # For now its just putting numbers.
        
        # if account_num not in account_nums:
        #     print ("")
        #     return false
        name_recipient = input_name()
        account_num = input_account_num()
        while (not verify_account(name_recipient, account_num)) :
            account_num = input_account_num()
            name_recipient = input_name()
            
        
        ## the name and account_num for the recipient has to be proven from the bank system. For this project, I will assume that the name and the account number is correct. 
        # if (invalid_user(name, account_num)):
            
        self.balance -= amount
        ## I actually dont transfer money to another account but I will do the actual transfer if they were real accounts
        print(f"{amount} Dollars successfully transfered to {name_recipient}'s account {account_num}. Your remaining balance is {self.balance} Dollars")
        add_friend_list = (input("Would you like to add your friend to the friend list?: (y/n)"))
        if(add_friend_list == 'y') :
            if (account_num in self.friends.keys()):
                print("Same account number is already in the friends list")
            else:
                self.add_friend_(account_num, name_recipient)
        self.balance_enquiry()
        return True
    
    def transfer_money_friend(self, amount):
        if (amount > self.balance) :
            print ("You do not have sufficient balance to make this transfer \n")
            return False
        
        if (len(self.friends) <1 ) :
            print("You do not have friends on the list. please add your friend \n")
            
            return False
        
        num_friend = 1
        friends_names = list(self.friends.values())
        friends_keys = list(self.friends.keys())
        while (1):
            
            for i in range(len(friends_names)):
                print(f"{i + 1} {friends_names[i]}  \n")
            
            while(True):
                try:
                    num_friend = int(input("Choose the coreesponding number: "))
                    break
                except ValueError:
                    print("Enter the correct number")
        
            if (num_friend <= len(self.friends) and num_friend > 0):
                break
            else:
                print("Please choose the number corresponding to the recipient")

            
        self.balance -= amount
        print(f"{amount} has been successfully transferred to your friend {self.friends[friends_keys[num_friend - 1]]}  \n")
        self.balance_enquiry()
        return True

    def print_my_account(self):
        print(f"name: {self.name} \n")
        print(f"bank: {self.bank} \n")
        print(f"account number: {self.account_num} \n")
        print(f"card number: {self.card_num} \n")
        # print(f"pin: {self.pin} \n")
        print(f"balance: {self.balance} \n")
        print(f"friends: {self.friends} \n")
    
 