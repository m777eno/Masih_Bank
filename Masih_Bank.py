#Author: Enoch Masih
#Name of program: Masih Bank
#Last Updated: 5/02/2020
#Pupose of program: Simulated banking Program to teach about better banking habits.

#Function
def login(): #Welcomes and prompts user to login or sign-up
    selection = input("\n~~ Welcome to Masih Bank ~~\nType the number associated with the option and press Enter to select that option.\n1. Create a new account\n2. Login\n>>>")
    if selection == "1":# when user types "1" they are taken to create_login function which creates a login
        create_login()
    elif selection =="2": # when user types "2" they are taken to search_account function which searches for their account
        search_account()
    elif selection != "1" or "2": # if user enters anything other than "1" or "2" the function prompts and begins again and gives them another chance.
        print("\n>>>Invalid Entry.<<<\nPlease try again.")
        login()

def last_account(): #Returns the count of the last account in the ledger.txt. This lets the program know the amount of accounts documented in ledger.txt.
    f = open("ledger.txt", "r")
    for i in f: #This loop passes each line so it ends at the bottom line of the ledger.txt file.
        pass
    last_sequence = i.find(":")#Now that its on the bottom line it reads the data. data is separated by ":"
    last_sequence = i[:last_sequence] #Everything before the first ":" indicates a sequence number used to count until the next ":"
    f.close()
    return int(last_sequence)#the function returns this last sequence number so the program knows the count on the ledger

def create_login():#This function creates a new account. This function also checks that the username is unique to the individual, but not password.
    new_user = input("\nlets get started on your new account!\nRemember username and password are Case-Sensitive.\nPlease make your credentials unique.\ntype in a username.\n>>>")#Smaller print commands reduced to create a succinct program.
    account_num = 0 #A new variable created used for the program to count with respect to the ledger.
    username = "admin" #A new variable declared to compare user input to data existing in the ledger.
    while username != new_user: #This loop checks if the username entered is present in the current ledger. If it is not present, Program proceeds.
        if account_num > last_account():#If the program's counter(account_num) is greater than the count of the ledger (last_account) than it has been validated that the username is unique, program continues.
            password = input("type in a password.\n>>>")#User types in password, and reminded to keep a copy.
            f = open("ledger.txt", "a")#This time the file is opened in a amending mode to add to the file.
            f.write((str(int(last_account())+1)) + ":" + new_user + ":" + password + ":" + str(0.00) + ":" + str(0.00) + "\n")#Consolidates information gathered from the ledger and the user to write a new account information.
            f.close()#Program opens and closes file when purpose completed to save memory.
            print("\nAccount Created!\nPlease keep a copy of your username and password.\nLets Explore your new account.")#User knows it was successfully created.
            login() #User can now login using their new account.
            break # I found out that this break command is critical as it stops the loop.
        f = open("ledger.txt", "r+")
        each_line = f.readlines()[account_num]#The ledger.txt file is created into a list. Each item on the list is a account. which is then counted using the program's counter called account_num
        category = each_line.split(":")#An item on the list contains several pieces of information related to an account categorized by ":".
        username = category [1]#Each category is named. This allows the information to be interpreted and analyzed by the program for comparison.
        account_num += 1#If the account in the ledger.txt did not meet the requirements, the count is increased by one to check the next line.
        f.close()
    if username == new_user: #Checks if the username is equal to user's input. If so then informs the user that username has been taken.
        print("\n>>>Username is taken. Please try again and create unique username.<<<\n")
        create_login()#Once informed user taken back to try again.

def search_account():#If the user already has an account; This function searches for it. If account is found the program proceeds.
    print("\n~~Login~~")
    account_num = 0 #Same variable name used as the function create_login since purpose of the variable is the same.
    username = "admin"#Same variable name used as the function create_login since purpose of the variable is the same.
    username_temp = input("Type in your username.\n>>>")
    while username_temp != username:#Program continues to iterate if username is not present. With each iteration program checks the next line in the ledger.
        f = open("ledger.txt", "r+")
        if account_num > last_account():#If the program's counter(account_num) is greater than the ledger's counter (Last_account) that means account was not found.
            choice = input("\nAccount not found.\nType 1 to try again or type 2 to return to the Welcome menu.\n")#The user is given option to try again or return to welcome screen.
            if choice == "1":
                search_account()
            elif choice == "2":
                login()
            elif choice != "1" or "2":# if user enters anything other than "1" or "2" the function prompts and begins again and gives them another chance.
                print(">>>Invalid Entry.<<<\n")
                login()
                break
        each_line = f.readlines()[account_num]#Ledger.txt is created into a list and account_num variable is used to assign value of specific line which holds one account.
        category = each_line.split(":")#The line is split into different categories.
        username = category [1]#username is set to category one
        if account_num < last_account():#if count of program (account_num) is less than the count of the ledger(last_account) than the program passes
            pass
        account_num += 1#each iteration increases the program counter by one to check each line of the file.
    if username == username_temp:# if username entered matches the username on file than the program proceeds to password.
        print("\nAccount Found!")
        if account_num == 0: #used to correct the counter especially for the admin account.
            match_password(account_num)
        else:
            match_password((account_num - 1))#because the while loop increases the counter by one after it breaks this helps reset it.

def match_password(account_num):#Matches password to the username in the ledger. The account_num variable carries the username so it doesn't have to be re-typed.
    f = open("ledger.txt", "r+")
    each_line = f.readlines()[account_num]
    category = each_line.split(":")
    password = category [2]# assigns password as category two.
    password_temp = input("Type in your Password.\n>>>")
    if password_temp == password: #If password on file matches the password entered by the user, than the program continues
        print("Successful Login!")
        main_menu(account_num)#Once logged in user is taken to the main_menu of the program along with the account number
    elif password_temp != password:#If the password does not match, the user has to enter the username again as well.
        print(">>>Incorrect Password<<<\n Please try again starting with the Username.") #Incorrect password forces user to re-enter username as well.
        search_account()

def main_menu(account_num): #Displays main menu and Lets the user select options
    select_main = input("\n>>> Main Menu <<<\nType the corresponding number to enter the option.\n1. Checking\n2. Savings\n3. Transfer\n4. Loans\n5. Good Banker \n6. Logout\n7. References\n>>>")
    if select_main == "1":
        checking(account_num)
    elif select_main == "2":
        savings(account_num)
    elif select_main == "3":
        transfer(account_num)
    elif select_main == "4":
        loans(account_num)
    elif select_main == "5":
        good_banker(account_num)
    elif select_main == "6":
        print("Successfully Logged out!")
        login()
    elif select_main == "7":
        references(account_num) #References does not need user information to be passed into it.
    else:
        print(">>>Invalid Entry.<<<\nPlease Try again.")
        main_menu(account_num)

def transfer(account_num):
    print("\n~~Tranfer~~\nTransfers can be made between your Checking and Savings account.")
    f = open("ledger.txt", "r+")
    each_line = f.readlines()[account_num]
    category = each_line.split(":")
    checking_val = category [3]
    savings_val = category [4]
    print("Checking: $","{0:.2f}".format(float(checking_val)))
    print("Savings: $","{0:.2f}".format(float(savings_val)))
    select_trans = input("\n>>>Options:\n1. Transfer funds to Checking\n2. Transfer funds to Savings\n3. Return to Main Menu\n>>>")
    if select_trans == "1":
        tran_check = round(float(input("Enter the numeric amount to transfer from your Savings to the Checking account.\nDo not include commas.\n>>>")),2)
        if float(tran_check) > float(savings_val):
            print("Unfortunately you do not have $", "{0:.2f}".format(tran_check), "in your Savings account.\nTry again or return to Main Menu and deposit money into Savings.")
            trans_fail = input("1. Try again\n2. Return to Main Menu\n>>>")
            if trans_fail == "1":
                transfer(account_num)
            elif trans_fail == "2":
                main_menu(account_num)
            else:
                print(">>>Invalid Entry.<<<")
                transfer(account_num)
                f.close()
        elif float(tran_check) <= float(savings_val):
            if float(tran_check) == float(savings_val):
                print("Caution: You have transferred the entire amount from your Savings")
            savings_val = str(float(savings_val) - float(tran_check))
            checking_val = str(float(checking_val) + float(tran_check))
            update_savings(account_num,savings_val)
            update_checking(account_num,checking_val)
            print("Transfer successful!")
            transfer(account_num)
    elif select_trans == "2":
        tran_sav = round(float(input("Enter the numeric amount to transfer from your Checking to the Savings account.\nDo not include commas.\n>>>")),2)
        if float(tran_sav) > float(checking_val):
            print("Unfortunately you do not have $", "{0:.2f}".format(tran_sav), "in your Checking account.\nTry again or return to Main Menu and deposit money into Checking.")
            trans_fail = input("1. Try again\n2. Return to Main Menu\n>>>")
            if trans_fail == "1":
                transfer(account_num)
            elif trans_fail == "2":
                main_menu(account_num)
            else:
                print(">>>Invalid Entry.<<<")
                transfer(account_num)
                f.close()
        elif float(tran_sav) <= float(checking_val):
            if float(tran_sav) == float(checking_val):
                print("Caution: You have transferred the entire amount from your Checkings")
            savings_val = str(float(savings_val) + float(tran_sav))
            checking_val = str(float(checking_val) - float(tran_sav))
            update_savings(account_num,savings_val)
            update_checking(account_num,checking_val)
            print("Transfer successful!")
            transfer(account_num)
    elif select_trans == "3":
        main_menu(account_num)
    else:
        print(">>>Invalid Entry.<<<")
        transfer(account_num)
    f.close()

def good_banker(account_num):
    print("\n~~Good Banker~~\nCollection of advice.")
    print("\n~~Loans~~\nThere are two types of loans. Simple interest loans and compounded interest loans.\nSimple interest loans have a consistent interest rate based on the principal value.\nCompounded interest loans take the unpaid interest of the first billing and add it to the principal of the second billing thereby compounding it.")
    print("When paying your Home mortgage; the monthly interest is paid first with the reamining amount going towards the principal.\nThis is a simple interest loan, Since your interest is paid in full first and not compounded.")
    print("\n~~Checking~~\n'Collect as soon as possible, pay as late as possible.' used to be a popular rule to keep money in your account as long as possible.\nContrary to this belief, It is better to pay your bills as soon as they arrive")
    print("Old advice was to keep checking account balance low, as you would not make any interest on it as opposed to a savings.\nBetter advice states, to leave a large cushion in the checking account.\nIf you miscalculated, an overdraft fee in checking could cost more.")
    print("\n~~Savings~~\nTwo popular options for saving money is a traditional savings account or a money market.\nSavings account are great for short-term savings such as vacations, medical bills, or emergencies.\nMoney Market is a more effective option which yields a higher interest rate.\nKeep in mind that these accounts have higher fees for untimely withdrawals.")
    print("401k and Roth IRA are popular retirement accounts. 401k are usually employee sponsored. Roth IRA are opened individually.\nWhen retiring, any funds withdrawn from a Roth IRA have already been taxed while fund withdrawn from a 401k will be taxed during the time of withdrawl.")
    main_menu(account_num)

def references(account_num):
    print("~~References~~")
    print("\nLoan advice")
    print(">>https://thefinancebuff.com/is-home-mortgage-simple-interest-or-compound-interest.html")
    print("\nChecking advice")
    print(">>>https://thefinancebuff.com/3-good-money-habits-going-obsolete-in-a-low-interest-rate-world.html")
    print("\nSavings advice")
    print(">>>https://www.investopedia.com/ask/answers/012615/why-would-you-keep-funds-money-market-account-and-not-savings-account.asp")
    print("\n>>>https://www.thesimpledollar.com/investing/roth-ira-vs-401k/")
    main_menu(account_num)

def loans(account_num):
    print("\n~~Loans~~")
    select_loans = input("1. Loan calculator\n2. Learn about Loans\n3. Return to Main Menu\n>>>")
    if select_loans == "1":
        loan_calc(account_num)
    elif select_loans == "2":
        print("~~Tip 1\nThere are two types of loans. Simple interest loans and compounded interest loans.\nSimple interest loans have a consistent interest rate based on the principal value.\nCompounded interest loans take the unpaid interest of the first billing and add it to the principal of the second billing thereby compounding it.")
        print("~~Tip 2\nWhen paying your Home mortgage; the monthly interest is paid first with the remaining amount going towards the principal.\nThis is a simple interest loan, Since your interest is paid in full first and not compounded.")
        loans(account_num)
    elif select_loans == "3":
        main_menu(account_num)
    else:
        print(">>>Invalid Entry.<<<\nPlease Try again.")
        loans(account_num)

def loan_calc(account_num):
    print("\n~~Loan Calculator~~")
    print("This will calculate a fixed monthly payment. For example a home mortgage.")
    interest = (((float(input("Enter your yearly interest. [Sometimes referred to as APR]\nDo not enter the '%' symbol.\n>>>")))/100)/12) #take in user input as float divide by 100 to convert percent to decimal then divide by 12 for 12 months of a year. Result is monthly interest
    interest_pay = float(interest + 1) #This variable is used to simplify and break up the monthly_pay equation.
    principal = float(input("Enter the principal amount. Do not include commas.\n>>>"))
    principal = (principal - float(input("Enter the amount of down payment. If you are not making a down payment, enter 0\n>>>")))
    monthly = ((float(input("Enter the amount in years.\n>>>")))*12)
    years = monthly / 12
    monthly_pay = round((principal * interest) * (pow(interest_pay,monthly)) /(pow(interest_pay,monthly)-1))
    print("You would pay $","{0:.2f}".format(float(monthly_pay)), "per month.")
    total_interest = ((monthly_pay * monthly) - principal)
    if monthly > 12:
        print("over", round(years),"years you would have paid $", "{0:.2f}".format(float(total_interest)), "of just interest fees alone.")
    elif monthly <= 12:
        print("over", round(monthly),"months you would have paid $", "{0:.2f}".format(float(total_interest)), " of just interest fees alone.")
    f = open("ledger.txt", "r+")
    each_line = f.readlines()[account_num]
    category = each_line.split(":")
    savings_val = category [4]
    if monthly_pay > float(savings_val):
        print("As it turns out, with the current balance in your savings account you would not be able to afford a single monthly payment.\nGo back to savings and deposit some funds, then try again.")
        loans(account_num)
    elif round(monthly_pay) == float(savings_val):
        print("According to your savings account, you can afford only 1 month's payment.\nGo back to savings and deposit some funds, then try again.")
        loans(account_num)
    elif monthly_pay < float(savings_val):
        afford = (round((float(savings_val)) / monthly_pay))
        if afford < 12:
            print("According to your savings account, You can afford", afford, "month's payment.")
            print("Since you cannot afford the monthly payments for the entire year, make sure you have a steady income.")
            print("Go back to savings to deposit or withdraw funds, then try again.")
        elif afford >= 12:
            afford = round(afford /12)
            print("According to your savings account, You can afford",afford, "year's payment.")
            if afford >= years:
                print("You can afford to pay the principal and interest fully.\nConsider an increased down payment, since you can afford this out right.")
            if afford < years:
                print("Since you cannot pay the principal fully with your current funds in savings, make sure you have a steady income.")
                print("Go back to savings to deposit or withdraw funds, then try again.")
        f.close()
        loans(account_num)

def checking(account_num):
        print("\n~~checking~~")
        f = open("ledger.txt", "r+")
        each_line = f.readlines()[account_num]
        category = each_line.split(":")
        checking_val = category [3]
        print("Account Balance: $","{0:.2f}".format(float(checking_val)))
        if float(checking_val) == 0:
            print("Ah oh! looks like your checking account has $","{0:.2f}".format(float(checking_val)))
            print("Don't worry, for simulation purposes we will add a credit of $100")
            checking_val = str(float(checking_val) + 100)
            update_checking(account_num,checking_val)
        select_check = input("\n>>>Options:\n1. deposit or withdraw funds.\n2. Learn more about Checking account.\n3. Return to Main Menu.\n>>>")
        if select_check == "1":
            checking_val = str(((float(checking_val))+(round(float(input("Deposit by entering '+' or Withdraw by entering '-' followed by the numeric amount.\nDo not include commas.\n>>>")),2))))
            update_checking(account_num,checking_val)
            print("Balance: $","{0:.2f}".format(float(checking_val)))
            checking(account_num)
        elif select_check == "2":
            print("~~Tip 1\n'Collect as soon as possible, pay as late as possible.' used to be a popular rule to keep money in your account as long as possible.\nContrary to this belief, It is better to pay your bills as soon as they arrive.")
            print("~~Tip 2\nOld advice was to keep checking account balance low, as you would not make any interest on it as opposed to a savings.\nBetter advice states, to leave a large cushion in the checking account.\nIf you miscalculated, an overdraft fee in checking could cost more.")
            checking(account_num)
        elif select_check == "3":
            main_menu(account_num)
        else:
            print(">>>Invalid Entry.<<<\nPlease Try again.")
            checking(account_num)
        f.close()

def savings(account_num):
    print("\n~~Savings~~")
    f = open("ledger.txt", "r+")
    each_line = f.readlines()[account_num]
    category = each_line.split(":")
    savings_val = category [4]
    print("Account Balance: $","{0:.2f}".format(float(savings_val))) #Variable savings_val is turned into float, which is then formatted to display with 2 decimal points.
    if float(savings_val) == 0:
        print("Ah oh! looks like your Savings account has $","{0:.2f}".format(float(savings_val)))
        print("Don't worry, for simulation purposes we will add a credit of $100")
        savings_val = str(float(savings_val) + 100.00)
        update_savings(account_num,savings_val)
    select_sav = input("\n>>>Options:\n1.deposit or withdraw funds.\n2.Learn more about Savings account.\n3.Return to Main Menu.\n>>>")
    if select_sav == "1":
        savings_val = str(((float(savings_val))+(round(float(input("Deposit by entering '+' or Withdraw by entering '-' followed by the numeric amount.\nDo not include commas.\n>>>")),2))))
        update_savings(account_num,savings_val)
        print("Updated Balance: $","{0:.2f}".format(float(savings_val)))
        savings(account_num)
    elif select_sav == "2":
        print("~~Tip 1\nTwo popular options for saving money is a traditional savings account or a money market.\nSavings account are great for short-term savings such as vacations, medical bills, or emergencies.\nMoney Market is a more effective option which yields a higher interest rate.\nKeep in mind that these accounts have higher fees for untimely withdrawals.")
        print("~~Tip 2\n401k and Roth IRA are popular retirement accounts. 401k are usually employee sponsored. Roth IRA are opened individually.\nWhen retiring, any funds withdrawn from a Roth IRA have already been taxed while fund withdrawn from a 401k will be taxed during the time of withdrawl.")
        savings(account_num)
    elif select_sav == "3":
        main_menu(account_num)
    else:
        print(">>>Invalid Entry.<<<\nPlease Try again.")
        savings(account_num)
    f.close()

def update_checking(account_num, checking_val):
    f = open("ledger.txt", "r+")
    each_line = f.readlines()[account_num]
    category = each_line.split(":")
    sequence = category [0]
    username = category [1]
    password = category [2]
    savings = category [4]
    f = open("ledger.txt", "r+")
    all_line = f.readlines()
    all_line [account_num] = sequence + ":" + username + ":" + password + ":" + checking_val + ":" + savings
    f.close()
    f = open("ledger.txt", "w+")
    f.writelines(all_line)
    f.close()

def update_savings(account_num, savings_val):
    f = open("ledger.txt", "r+")
    each_line = f.readlines()[account_num]
    category = each_line.split(":")
    sequence = category [0]
    username = category [1]
    password = category [2]
    checking = category [3]
    f = open("ledger.txt", "r+")
    all_line = f.readlines()
    all_line [account_num] = sequence + ":" + username + ":" + password + ":" + checking + ":" + savings_val+"\n"
    f.close()
    f = open("ledger.txt", "w+")
    f.writelines(all_line)
    f.close()

login()
