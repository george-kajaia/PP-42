class BankingError(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):               
        return f"{super().__str__()} My custom exception"
    


try:
    raise BankingError("Cannot withdraw more than available balance")
except Exception as e:
    print(e)
