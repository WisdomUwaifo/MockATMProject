# init = Greetings, and direction to either login or register
# Register = First and Last Name, email address, and direction to generate account number
# generate acount number = Ramdom Number, database, dictionary, and direction to bank operation
# Bank Operation = make deposite, withdrawal, check account balancd, and make a complain.
#
import random
import database
import validation


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
# account_number = [1039456821]


def register():
    first_name = input('What is your first name? \n')
    last_name = input("What is your last name? \n")
    home_address = input(
        'What is your home adress inclusing the city and the Zipcode? \n')
    date_of_birth = input('What ia your date birth \n')
    email_address = input('what is your email address? \n')
    print('Thank you for creating an account with us. \n')
    account_number = generate_account_number()
    print('Here is your accoun number. We will mail your debit card to in 3 to 5 business days:',
          account_number)

    is_user_created = database.create(
        account_number, first_name, last_name, date_of_birth, email_address)
    if is_user_created:
        print('your account has been created')
        print(' = ==== ==== ======= ====== =')
        print('your account number is: %d' % account_number)
        print('keep your account number confidential')
        print(' = === ===== ==== ==== ==== =')
        login()
    else:
        print('something has gone wrong, please try again')
        register()


def login():
    print('login into your account')
    name = input('What is your name? \n')
    if name in authorized_name:
        email = input('what is your email address? \n')
        name_id = authorized_name.index(name)
        if email == authorized_email[name_id]:
            password = input('Please enter your password. \n')
            authorized_password = ['Pawisdom', 'pahamza', 'paalex', 'paadam']
            email_id = authorized_email.index(email)
            if password == authorized_password[email_id]:
                account_number_from_users = int(
                    input('what is your account number? \n'))
                if account_number_from_users in account_number:

                    bank_operation()
                else:
                    print('Wrong account number. Try again')

                # for account_number, user_details in database.items():
                    # if account_number == account_number_from_users:
                    # if user_details[3] == password:

            else:
                print('wrong Password, please try again')
        else:
            print('invalid email address, please try again')
    else:
        print('Invalid name, please try again')


def bank_operation():
    print('welcome %s ' % (authorized_name[0]))
    is_selected_option_valid = False
    while is_selected_option_valid == False:
        operation = int(input(
            'what would you like to do today? 1 (Create a new account) 2 (Withdrawal) 3 (Deposit) 4 (Check account balance) 5 (Make a Complain) \n'))
        if operation == 1:
            is_selected_option_valid = True
            print(generate_account_number())
            print('Please proceed to make your initial deposit.')
            make_a_deposit()
        elif operation == 2:
            is_selected_option_valid = True
            make_a_withdrawal()
        elif operation == 3:
            is_selected_option_valid = True
            make_a_deposit()
        elif operation == 4:
            is_selected_option_valid = True
            check_account_balance()
        elif operation == 5:
            is_selected_option_valid = True
            make_a_complain
        else:
            print('Invalid option selected. Please try again.')


def generate_account_number():
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
