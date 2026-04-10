# test_utils.py
# simple tests to check that the main functions work correctly
# Run with: pytest test_utils.py

import pandas as pd
import pytest
from utils import clean_data, avg_sales_by_discount, run_regression


def make_fake_df():
    """Create a small dataset similar to the real one."""
    return pd.DataFrame({
        "Sales":    [100.0, 200.0, 50.0, 400.0, 150.0],
        "Discount": [0.0,   0.2,   0.4,  0.0,   0.2],
        "Profit":   [20.0,  30.0,  -5.0, 80.0,  25.0],
        "Category": ["Furniture", "Technology", "Furniture", "Technology", "Office Supplies"],
        "ExtraCol": ["a", "b", "c", "d", "e"],
    })


# --- unit tests ---

def test_clean_data_columns():
    """Check that only the relevant columns are kept."""
    df = clean_data(make_fake_df())
    assert list(df.columns) == ["Sales", "Discount", "Profit", "Category"]


def test_clean_data_removes_missing():
    """Check that rows with missing values are removed."""
    df = make_fake_df()
    df.loc[0, "Sales"] = None
    df_clean = clean_data(df)
    assert len(df_clean) == 4


def test_avg_sales_by_discount():
    """Check average sales per discount level."""
    df = clean_data(make_fake_df())
    avg = avg_sales_by_discount(df)

    # we expect 3 discount levels: 0.0, 0.2, 0.4
    assert len(avg) == 3

    # check that average for discount = 0 is correct
    val = avg.loc[avg["Discount"] == 0.0, "avg_sales"].values[0]
    assert val == pytest.approx(250.0)


def test_run_regression_keys():
    """Check that regression returns expected keys."""
    df = clean_data(make_fake_df())
    res = run_regression(df)

    for key in ["slope", "intercept", "r_squared", "p_value"]:
        assert key in res


def test_run_regression_r_squared():
    """Check that R-squared is between 0 and 1."""
    df = clean_data(make_fake_df())
    res = run_regression(df)

    assert 0.0 <= res["r_squared"] <= 1.0


# --- integration test ---

def test_full_pipeline():
    """Check that the full pipeline runs without error."""
    df_raw = make_fake_df()
    df = clean_data(df_raw)
    avg = avg_sales_by_discount(df)
    res = run_regression(df)

    assert not avg.empty
    assert res["r_squared"] >= 0