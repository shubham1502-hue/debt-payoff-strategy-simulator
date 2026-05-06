# Debt Payoff Strategy Simulator

## Problem This Solves

Borrowers and fintech teams often know the names of debt payoff strategies but cannot see the month-by-month trade-off between psychological momentum and interest minimization. The problem is turning multiple loans into a clear repayment decision.

## How It Helps

- Compares Snowball and Avalanche payoff strategies on payoff months, total interest, and interest saved.
- Exports repayment schedules so users can inspect the exact month-by-month balance path.
- Gives fintech, lending, and personal finance teams a forkable simulator for customer-facing debt payoff planning.

## When To Fork This

- Fork this if you are building a personal finance, lending, debt counseling, or credit education workflow.
- Fork it when users need to compare repayment strategies using their own loan balances, interest rates, minimum payments, and extra monthly payment.
- Add more strategies, user input, or a dashboard layer once the basic simulator matches your product use case.

A Python-based financial analytics project that simulates different debt repayment strategies across multiple loans. The simulator compares the **Snowball** and **Avalanche** payoff methods to determine which strategy minimizes interest and reduces payoff time.

This project demonstrates financial modeling, simulation-based strategy evaluation, and data-driven analysis using Python.

---

## Project Overview

Many individuals carry multiple forms of debt such as credit cards, personal loans, and auto loans. Choosing the right repayment strategy can significantly reduce the **total interest paid** and **time required to become debt-free**.

This simulator models monthly loan repayment dynamics including:

- Interest accumulation
- Minimum payments
- Extra payment allocation
- Strategy-driven prioritization of loans

By running simulations across repayment strategies, the system generates repayment schedules, payoff timelines, and interest comparisons.

---

## Repayment Strategies Implemented

### Snowball Method

Loans are prioritized by **smallest balance first**.

Benefits:

- Provides quick psychological wins
- Eliminates smaller debts early

Trade-off:

- May result in higher total interest compared to interest-optimized strategies.

### Avalanche Method

Loans are prioritized by **highest interest rate first**.

Benefits:

- Minimizes total interest paid
- Mathematically optimal repayment strategy

Trade-off:

- Progress may feel slower initially.

---

## Project Architecture

The system is modular and organized into separate components that mirror a real analytics workflow.

```
dept-payoff-simulator
│
├── data
│   └── loans.csv
│
├── src
│   ├── loan.py
│   ├── strategies.py
│   ├── simulator.py
│   ├── analytics.py
│   └── main.py
│
├── outputs
│   ├── snowball_schedule.csv
│   └── avalanche_schedule.csv
│
├── README.md
└── requirements.txt
```

### Module Responsibilities

**loan.py**  
Defines the Loan class and models loan behavior including interest accumulation and payment processing.

**strategies.py**  
Implements repayment prioritization logic for Snowball and Avalanche strategies.

**simulator.py**  
Runs the monthly repayment simulation and updates loan balances over time.

**analytics.py**  
Compares strategy results and calculates metrics such as total interest paid and payoff duration.

**main.py**  
Executes the simulation and visualizes repayment results.

---

## Key Features

- Financial modeling of multi-loan repayment scenarios
- Simulation of debt payoff strategies
- Strategy comparison through analytical metrics
- Visualization of repayment timelines
- Exportable repayment schedules for further analysis

---

## Example Output

Running the simulator generates:

- Strategy comparison metrics
- Repayment timeline data
- Visualization of debt payoff curves

Example metrics:

```
Snowball payoff months: 64
Avalanche payoff months: 63
Snowball total interest: 9552
Avalanche total interest: 8937
Interest saved with avalanche: 615
```

The system also exports repayment schedules to CSV files for further analysis.

---

## Installation

Clone the repository:

```
git clone https://github.com/shubham1502-hue/debt-payoff-strategy-simulator.git
cd debt-payoff-strategy-simulator
```

Install dependencies:

```
python3 -m pip install -r requirements.txt
```

---

## Running the Project

Execute the main simulation script:

```
python3 src/main.py
```

The program will:

1. Load loan data
2. Run repayment simulations
3. Compare payoff strategies
4. Generate visualizations
5. Export repayment schedules

---

## Why This Project Matters

Financial institutions and fintech platforms often simulate repayment scenarios to help users optimize debt payoff decisions.

This project demonstrates core concepts used in financial analytics systems:

- Financial modeling
- Strategy optimization
- Simulation systems
- Data analysis workflows
- Visualization of financial outcomes

---

## Future Improvements

Potential enhancements include:

- Interactive dashboard using Streamlit
- User-input loan scenarios
- Additional repayment strategies
- Monte Carlo simulations for uncertainty modeling

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Financial modeling techniques

---

## Author

Shubham Singh
