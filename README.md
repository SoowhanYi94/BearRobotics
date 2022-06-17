# BearRobotics


Please upload the code for this project to GitHub or anywhere, and post a link to your repository below. Please attach the instruction to clone your project, build and run tests in README.md file in the root directory of the repository.

1. Clone respository

git clone https://github.com/SoowhanYi94/BearRobotics.git

2. move to working directory

cd BearRobotics/simpleATM

3. run tests

python3 simpleATM.py


------------------------------------------------------------------------------------------------------------------------------------------

#simpleATM.py
1. It starts with inserting the card to the atm machine, and I will assume that the card will be inserted
2. The card will be validated through validate_card(). But I will assume that the card is valid. In the future.
3. extract_info() will extract information from the card and identify the user. However I created a fake account in order to proceed.
4. login(user) would let user login in to the system. Validating pin number is part of the login process, and the account will be locked if the pin number is wrong more than 5 times. However, validating pin number is not possible in this project. So it will let you login even if you put random pin numbers for now.
5. After logging in, it goes to finite state machine. 

------------------------------------------------------------------------------------------------------------------------------------------





