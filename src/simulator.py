

import pandas as pd
from loan import Loan


"""
Simulation Engine

This module runs the month-by-month debt repayment simulation.
It loads loans from a dataset, applies interest, applies minimum
payments, then distributes extra payments according to a chosen
strategy (snowball or avalanche).
"""


def load_loans(filepath):
    """
    Load loan data from CSV and convert it into Loan objects.

    Parameters
    ----------
    filepath : str
        Path to the loan dataset

    Returns
    -------
    list
        List of Loan objects
    """

    df = pd.read_csv(filepath)

    loans = []

    for _, row in df.iterrows():
        loan = Loan(
            row.loan_name,
            row.balance,
            row.interest_rate,
            row.min_payment
        )

        loans.append(loan)

    return loans


def run_simulation(loans, strategy, extra_payment=500):
    """
    Run the debt payoff simulation.

    Parameters
    ----------
    loans : list
        List of Loan objects
    strategy : function
        Strategy function (snowball or avalanche)
    extra_payment : float
        Extra monthly payment available beyond minimum payments

    Returns
    -------
    DataFrame
        Monthly simulation results
    """

    month = 0

    records = []

    # Continue until all loans are paid off
    while any(not loan.is_paid_off() for loan in loans):

        month += 1

        monthly_interest = 0
        monthly_payment = 0

        # Step 1: Apply interest to all active loans
        for loan in loans:

            if not loan.is_paid_off():

                interest = loan.apply_interest()
                monthly_interest += interest

        # Step 2: Apply minimum payments
        for loan in loans:

            if not loan.is_paid_off():

                payment = loan.make_payment(loan.min_payment)
                monthly_payment += payment

        # Step 3: Allocate extra payment using strategy
        ordered_loans = strategy(loans)

        remaining_extra = extra_payment

        for loan in ordered_loans:

            if remaining_extra <= 0:
                break

            if not loan.is_paid_off():

                payment = loan.make_payment(remaining_extra)

                remaining_extra -= payment
                monthly_payment += payment

        # Step 4: Calculate remaining balance
        total_balance = sum(loan.balance for loan in loans)

        records.append({
            "month": month,
            "remaining_balance": total_balance,
            "interest_paid": monthly_interest,
            "payment_made": monthly_payment
        })

    results_df = pd.DataFrame(records)

    return results_df