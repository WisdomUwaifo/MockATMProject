# create_record
# update_record
# read_record
# delete_record
# CRUD
import os
import validation
user_db_path = "data/user_record/"


def create(account_number, first_name, last_name, date_of_birth, email_address):
    user_data = first_name + ',' + last_name + ',' + \
        ',' + date_of_birth + ',' + email_address + ',' + str(200)
    if does_account_number_exist(account_number):
        return False
    if does_email_exist(email_address):
        print('User already exist')
        return False
        completion_status = False
    is_valid_account_number = validation.account_number_validation(
        account_number)
    try:
        f = open(user_db_path + str(account_number) + ".txt", "x")
    except FileExistsError:
        does_file_contain_data = read(
            user_db_path + str(account_number) + ".txt")
        if not does_file_contain_data():
            delete(account_number)
        # delete(account_number)

    else:
        f.write(str(user_data))
        # delte the already created file and print out error, then return false
        completion_status = True
    finally:
        f.close()
    return completion_status

# create a file
# name of the file would be "account_number.txt"
# add the user details to the fiel
# return true
# if saving to files fails, then delete created file


def read(account_number):
    is_valid_account_number = validation.account_number_validation(
        account_number)

    try:
        if is_valid_account_number:
            f = open(user_db_path + str(account_number) + ".txt", "r")
        else:
            f = open(user_db_path + account_number + ".txt", "r")
    except FileNotFoundError:
        print('User not found')
    except FileExistsError:
        print('User does not exist')
    except TypeError:
        print('Invalid account number format')
    else:
        return f.readline()
    return False

# Find users with account number
# fetch the content of the file


def update(account_number):
    print('update user record')


# find users with account number
# fetch the content of the file
# update the content of the file
# save the file
# return true


def delete(account_number):
    is_delete_successful = False
    if os.path.exists(user_db_path + str(account_number) + ".txt"):
        try:
            os.remove(user_db_path + str(account_number) + ".txt")
        except FileNotFoundError:
            print('user not found')
        finally:
            return is_delete_successful


# find user with account number
# delete the user record
# return true


def does_email_exist(email):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        user_list = str.split(read(user[0:10]), ',')
        if email in user_list:
            return True
    return False


def does_account_number_exist(account_number):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        if user == str(account_number) + '.txt':
            return True

    return False

    # print(read(user[0:10])
    # print('\n')
    # find user record in the date folder

    # create(1039456821, ["first_name", "last_name","date_of_birth", "home_dddress", "email_address", 200])

    # print(read(9543576743))
    # print(read({'one': 'two'}))
print(does_email_exist('wisdomuwaifo@gmail.com'))
