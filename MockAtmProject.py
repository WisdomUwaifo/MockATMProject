name = input('What is your name? \n')
allowedusers = ['Seyi', 'Mike', 'Love']
if name in allowedusers:
    password = input('Your password? \n')
    allowedpassword = ['passwordseyi', 'passwordmike', 'passwordlove']
    userid = allowedusers.index(name)
    if password == allowedpassword[userid]:
        import datetime as datetime
        now = datetime.datetime.now()
        print("Current date and time : ")
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        print('welcome %s!' % name)
        print('These are the avalaible options')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complain')
        selectedoption = int(input('please select an option:'))
        if selectedoption == 1:
            print('how much would you like to withdraw?')
            print('1. $20')
            print('2. $40')
            print('3. $60')
            option = (input('please select an option'))
            allowedamount = ['$20', '$40', '60']
            if option in allowedamount:
                print('take your cash')
            else:
                print('wrong amount, please try again')
                print(name)
        elif selectedoption == 2:
            print('your current balance is $5,004.87')
            Depositamount = int(input('How much would you like to deposit?'))
            if Depositamount <= 1000:
                print('please insert your cash')
            elif Depositamount >= 1001:
                print('erro, please try again')
            else:
                print(
                    'Invalid amount, please go into the bank for one of our associates to assist you with your deposit')
                print('name')

        elif selectedoption == 3:
            input('what issue would like to report?')
            print(
                'thank you for contacting us. One of our associate will get back to you')
        else:
            print('Invalid Option Slected, Please Try Again.')

    else:
        print('password incorrect, please try again')
else:
    print('name not found, please try again.')
