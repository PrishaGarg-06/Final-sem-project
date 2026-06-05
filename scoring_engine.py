import numpy as np
import pandas as pd

def calculate_priority(df):

    df["complaint_rate"] = (
        df["complaints_l7d"]
        /
        df["qty_sold_l7d"]
        .replace(0,1)
    )

    df["expiry_score"] = np.where(
        df["days_to_expiry"] < 0,
        50,
        15 - df["days_to_expiry"]
    )

    df["complaint_score"] = (
        df["complaints_l7d"] * 5
    )

    df["sales_score"] = (
        df["qty_sold_l7d"] / 10
    )

    df["inventory_score"] = np.where(
        df["inventory_qty"] > 50,
        10,
        5
    )

    df["priority_score"] = (
        df["expiry_score"] * 0.4
        +
        df["complaint_score"] * 0.3
        +
        df["sales_score"] * 0.2
        +
        df["inventory_score"] * 0.1
    )

    return df
