# init = Greetings, and direction to either login or register
# Register = First and Last Name, email address, and direction to generate account number
# generate acount number = Ramdom Number, database, dictionary, and direction to bank operation
# Bank Operation = make deposite, withdrawal, check account balancd, and make a complain.
#

import random
database = {}


def initializing():
    print('Thank you for visiting UBank of America. We are alway at your service.')
    account_info = int(
        input('Do you have an account with us?: 1 (yes) 2 (no) \n'))
    if account_info == 1:
        login()
    elif account_info == 2:
        register()
    else:
        print('Invalid option selected, please try again')


authorized_name = ['Wisdom Uwaifo',
                   'Hamza Boubacar Kassomou', 'Alex Gano', 'Adam Kurbansho']
authorized_email = ['wisdom@ubank.org',
                    'hamza@ubank.org', 'alex@ubank.org', 'adam@ubank.org']


def register():
    input('What is your first name?')
    input("What is your last name?")
    Input('What is your home adress inclusing the city and the Zipcode?')
    input('What ia your date birth')
    input('what is your email address?')
    print('Thank you for creating an account with us. You may now proceed to create your bank account')
    generate_account_number()
    print('If you have any question contact our customer service team')


def login():
    name = input('What is your name? \n')

    if name in authorized_name:
        email = input('what is your email address? \n')

        name_id = authorized_name.index(name)
        if email == authorized_email[name_id]:
            password = input('Please enter your password. \n')
            authorized_password = ['Pawisdom', 'pahamza', 'paalex', 'paadam']
            email_id = authorized_email.index(email)
            if password == authorized_password[email_id]:
                bank_operation()
            else:
                print('wrong Password, please try again')
        else:
            print('invalid email address, please try again')
    else:
        print('Invalid name, please try again')


def bank_operation():
    operation = int(input(
        'what would you like to do today? 1 (Create a new account) 2 (Withdrawal) 3 (Deposit) 4 (Check account balance) 5 (Make a Complain) \n'))
    if operation == 1:
        print(generate_account_number())
        print('Please proceed to make your initial deposit.')
        make_a_deposit()
    elif operation == 2:
        make_a_withdrawal()
    elif operation == 3:
        make_a_deposit()
    elif operation == 4:
        check_account_balance()
    elif operation == 5:
        make_a_complain
    else:
        print('Invalid option selected. Please try again.')


def generate_account_number():
    print('Here is your accoun number. We will mail your debit card to in 3 to 5 business days.')
    return random.randrange(1111111111, 9999999999)


def make_a_deposit():
    print('To make a deposit, you must ensure that you depost the eligible amount')
    deposit_command = int(input('what amount would you like to deposit? \n'))
    if deposit_command <= 2000:
        print('depsit accepted')
        print('Thank you for banking with us')
    elif deposit_amount > 2000:
        print('Please, consider making this deposit amount twice or go into the bank and one of our customer service representative will help you.')
    else:
        print('Invalid amount, please try again')


def make_a_withdrawal():
    print('Please be aware that the maximum amount that you can withdraw from out ATM is 1000')
    withdrawal_Amount = int(input('How much would you like to withdraw?'))
    if withdrawal_Amount <= 1000:
        print('cash is dispensing')
    elif withdrawal_Amount > 1000:
        print('The amount you selected is larger than our ATM allowed withdrawal. Please reduce the amount or vist one of our bank locations')
    else:
        print('The amount you selected is invalid. please try again')


def check_account_balance():
    account_balance = input('would you like to check your account balance?')
    if account_balance == Yes:
        customer_pin = input('Please enter your three digit pin number')
        print('your account balance is $5000.94')
        print(' is there anything else we can do for you?')


def make_a_complain():
    print('Thank you so much for reaching out to us. We will reach out to you as soon as possible')
    first_name = input('What is your first name?')
    last_name = input('What is your last name')
    topic = input('complain topic')
    complain = input('What tell us what your complain is about')


initializing()
