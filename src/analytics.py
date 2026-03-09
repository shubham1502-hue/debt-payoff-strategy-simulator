

"""
Analytics Module

This module compares different debt repayment strategies
(snowball vs avalanche) using the simulation engine.
It calculates payoff timelines, total interest paid,
and returns datasets that can be used for visualization.
"""


import os
import sys

# Ensure the src directory is on the Python path so local modules resolve correctly
current_dir = os.path.dirname(__file__)
if current_dir not in sys.path:
    sys.path.append(current_dir)

from simulator import load_loans, run_simulation
from strategies import snowball, avalanche


def compare_strategies(filepath, extra_payment=500):
    """
    Run simulations for both snowball and avalanche strategies
    and compare their outcomes.

    Parameters
    ----------
    filepath : str
        Path to the loan dataset

    extra_payment : float
        Additional monthly payment beyond minimum payments

    Returns
    -------
    dict
        Summary comparison of strategies

    DataFrame
        Snowball simulation results

    DataFrame
        Avalanche simulation results
    """

    # Load two independent copies of the loans
    # (simulation mutates balances so we must reload)

    loans_snowball = load_loans(filepath)
    loans_avalanche = load_loans(filepath)

    # Run simulations

    snowball_results = run_simulation(
        loans_snowball,
        snowball,
        extra_payment
    )

    avalanche_results = run_simulation(
        loans_avalanche,
        avalanche,
        extra_payment
    )

    # Calculate metrics

    snowball_months = snowball_results.month.max()
    avalanche_months = avalanche_results.month.max()

    snowball_interest = snowball_results.interest_paid.sum()
    avalanche_interest = avalanche_results.interest_paid.sum()

    summary = {
        "snowball_payoff_months": int(snowball_months),
        "avalanche_payoff_months": int(avalanche_months),
        "snowball_total_interest": float(round(snowball_interest, 2)),
        "avalanche_total_interest": float(round(avalanche_interest, 2)),
        "interest_saved_with_avalanche": float(round(
            snowball_interest - avalanche_interest, 2
        ))
    }

    return summary, snowball_results, avalanche_results