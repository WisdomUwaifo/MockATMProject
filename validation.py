
def account_number_validation(account_number):
    if account_number:
        if len(str(account_number)) == 10:
            try:
                int(account_number)
                return True
            except ValueError:
                print('Invalid account number, please try again')
                return False
            except TypeError:
                print('Invalid account type. Try again')
                return False
        else:
            print('account number cannot be less than or more than 10 digits')
            return False
    else:
        print('Account number is a required field')
        return False
