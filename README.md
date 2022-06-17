# BearRobotics

1. Clone respository

git clone https://github.com/SoowhanYi94/BearRobotics.git

2. move to working directory

cd BearRobotics/simpleATM

3. run tests

python3 simpleATM.py


------------------------------------------------------------------------------------------------------------------------------------------

#simpleATM.py
1. It starts with inserting the card to the atm machine, and I will assume that the card will be inserted
2. The card will be validated through validate_card(). But I will assume that the card is valid.
3. extract_info() will extract information from the card and identify the user. However I created a fake account in order to proceed.
4. login(user) would let user login in to the system. Validating pin number is part of the login process, and the account will be locked if the pin number is wrong more than 5 times. However, validating pin number is not possible in this project. So it will let you login even if you put random pin numbers for now.
5. After logging in, it goes to finite state machine. 


As we do not have access to the bank system, I had to make some assumptions about the card and the users. 
The card, user, and the pin number will always be valid. Also the target recipient is always in the bank system when the user is trying to transfer money.
Also I made a feature to manage friends so that the user can easily transfer money from atm machine in the future.

------------------------------------------------------------------------------------------------------------------------------------------





