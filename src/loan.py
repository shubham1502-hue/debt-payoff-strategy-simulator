

class Loan:

    def __init__(self, name, balance, interest_rate, min_payment):
        """
        Represents a single loan in the debt portfolio.

        Parameters
        ----------
        name : str
            Name or identifier of the loan
        balance : float
            Current remaining balance of the loan
        interest_rate : float
            Annual interest rate (example: 0.22 for 22%)
        min_payment : float
            Minimum required monthly payment
        """

        self.name = name
        self.balance = float(balance)
        self.interest_rate = float(interest_rate)
        self.min_payment = float(min_payment)

        # Convert annual rate to monthly rate
        self.monthly_rate = self.interest_rate / 12

    def apply_interest(self):
        """
        Apply one month of interest to the loan balance.
        Interest is added before payments are made.
        """

        if self.balance <= 0:
            return 0

        interest = self.balance * self.monthly_rate
        self.balance += interest

        return interest

    def make_payment(self, payment_amount):
        """
        Apply a payment to the loan.

        Parameters
        ----------
        payment_amount : float
            Amount being paid toward the loan

        Returns
        -------
        float
            Actual payment applied (cannot exceed remaining balance)
        """

        if self.balance <= 0:
            return 0

        payment = min(payment_amount, self.balance)
        self.balance -= payment

        return payment

    def is_paid_off(self):
        """
        Check if the loan balance has been fully paid.
        """

        return self.balance <= 0

    def get_balance(self):
        """
        Return the current loan balance.
        """

        return self.balance

    def __repr__(self):
        """
        Helpful representation for debugging and logging.
        """

        return f"Loan(name={self.name}, balance={round(self.balance,2)}, rate={self.interest_rate})"