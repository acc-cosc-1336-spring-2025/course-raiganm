from bank_account import BankAccount # type: ignore
 
def main():
    account = BankAccount() #variable represents a BankAccount--- object or instance of a class
    print(account.get_balance())
 
main()