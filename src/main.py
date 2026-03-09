"""
Main Runner Script

This script executes the full debt payoff simulation pipeline:
1. Loads the loan dataset
2. Runs both payoff strategies (snowball and avalanche)
3. Prints summary metrics
4. Visualizes the repayment curves
"""

import matplotlib.pyplot as plt
import os
import sys

# Ensure the src directory is available in Python's module search path
current_dir = os.path.dirname(__file__)
if current_dir not in sys.path:
    sys.path.append(current_dir)

from analytics import compare_strategies


DATA_PATH = os.path.abspath(os.path.join(current_dir, "..", "data", "loans.csv"))
EXTRA_PAYMENT = 500

# Output directory for exported results
OUTPUT_DIR = os.path.abspath(os.path.join(current_dir, "..", "outputs"))

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


def main():

    summary, snowball_df, avalanche_df = compare_strategies(
        DATA_PATH,
        EXTRA_PAYMENT
    )

    print("\nDebt Payoff Strategy Comparison")
    print("=" * 40)

    for key, value in summary.items():
        print(f"{key}: {value}")

    # Export repayment schedules to CSV for further analysis
    snowball_path = os.path.join(OUTPUT_DIR, "snowball_schedule.csv")
    avalanche_path = os.path.join(OUTPUT_DIR, "avalanche_schedule.csv")

    snowball_df.to_csv(snowball_path, index=False)
    avalanche_df.to_csv(avalanche_path, index=False)

    print("\nRepayment schedules exported:")
    print(f"Snowball: {snowball_path}")
    print(f"Avalanche: {avalanche_path}")

    # Visualization

    plt.figure()

    plt.plot(
        snowball_df["month"],
        snowball_df["remaining_balance"],
        label="Snowball Strategy"
    )

    plt.plot(
        avalanche_df["month"],
        avalanche_df["remaining_balance"],
        label="Avalanche Strategy"
    )

    plt.xlabel("Month")
    plt.ylabel("Remaining Debt Balance")
    plt.title("Debt Payoff Strategy Simulation")

    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()
