# utils.py
# Helper functions used in the notebook.
# The goal is to keep things simple: load data, clean it, plot, and run a basic regression.

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def load_data(filepath):
    """
    Load the CSV file.

    Parameters:
        filepath (str): path to the CSV file

    Returns:
        pd.DataFrame: raw dataset
    """
    df = pd.read_csv(filepath, encoding="latin1")
    return df


def clean_data(df):
    """
    Keep only useful columns and remove missing values.

    Parameters:
        df (pd.DataFrame): raw dataset

    Returns:
        pd.DataFrame: cleaned dataset
    """
    # we keep only the columns needed for the analysis
    cols = ["Sales", "Discount", "Profit", "Category"]
    df_clean = df[cols].copy()

    # we drop missing values to avoid issues in later steps (plots, regression)
    df_clean = df_clean.dropna()

    return df_clean


def avg_sales_by_discount(df):
    """
    Compute average sales for each discount level.

    Parameters:
        df (pd.DataFrame): cleaned dataset

    Returns:
        pd.DataFrame: average sales per discount
    """
    result = df.groupby("Discount")["Sales"].mean().reset_index()
    result.columns = ["Discount", "avg_sales"]

    # sort values to make plots easier to read
    result = result.sort_values("Discount")

    return result


def plot_scatter(df):
    """
    Scatter plot: Discount vs Sales.

    Parameters:
        df (pd.DataFrame): cleaned dataset
    """
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.scatter(df["Discount"], df["Sales"], alpha=0.3, s=15, color="steelblue")

    ax.set_title("Discount vs Sales (one point = one transaction)")
    ax.set_xlabel("Discount rate")
    ax.set_ylabel("Sales (USD)")

    # we cap extreme values to keep the plot readable
    # without this, a few large sales dominate the chart
    ax.set_ylim(0, 5000)

    ax.grid(True, linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.show()


def plot_avg_sales(avg_df):
    """
    Bar chart: average sales per discount level.

    Parameters:
        avg_df (pd.DataFrame): output of avg_sales_by_discount
    """
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(
        avg_df["Discount"].astype(str),
        avg_df["avg_sales"],
        color="steelblue",
        edgecolor="white"
    )

    ax.set_title("Average Sales by Discount Level")
    ax.set_xlabel("Discount rate")
    ax.set_ylabel("Average Sales (USD)")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def run_regression(df):
    """
    Run a simple linear regression: Sales ~ Discount.

    Parameters:
        df (pd.DataFrame): cleaned dataset

    Returns:
        dict: regression results
    """
    slope, intercept, r_value, p_value, std_err = stats.linregress(
        df["Discount"], df["Sales"]
    )

    return {
        "slope": slope,
        "intercept": intercept,
        "r_squared": r_value ** 2,
        "p_value": p_value,
        "std_err": std_err,
    }


def print_regression_summary(res):
    """
    Print regression results in a readable way.

    Parameters:
        res (dict): output of run_regression
    """
    print("OLS regression: Sales ~ Discount")
    print("-" * 38)
    print(f"  Intercept  (b0) : {res['intercept']:.2f}")
    print(f"  Slope      (b1) : {res['slope']:.2f}")
    print(f"  R-squared       : {res['r_squared']:.4f}")
    print(f"  p-value         : {res['p_value']:.4f}")
    print(f"  Std error       : {res['std_err']:.2f}")
    print("-" * 38)