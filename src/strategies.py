"""
Debt payoff strategies.

Each strategy receives a list of Loan objects and returns
those loans ordered by priority for allocating extra payments.
"""


def snowball(loans):
    """
    Snowball Strategy

    Prioritize loans with the smallest balance first.
    Motivation: quick wins and psychological momentum.
    """

    active_loans = [loan for loan in loans if not loan.is_paid_off()]

    # Smallest balance first
    ordered_loans = sorted(active_loans, key=lambda loan: loan.balance)

    return ordered_loans


def avalanche(loans):
    """
    Avalanche Strategy

    Prioritize loans with the highest interest rate first.
    Motivation: minimize total interest paid.
    """

    active_loans = [loan for loan in loans if not loan.is_paid_off()]

    # Highest interest rate first
    ordered_loans = sorted(active_loans, key=lambda loan: loan.interest_rate, reverse=True)

    return ordered_loans
