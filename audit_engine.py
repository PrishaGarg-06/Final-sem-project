import pandas as pd

def identify_candidates(df):

    today = pd.Timestamp.today().normalize()

    df["expiry_date"] = pd.to_datetime(
        df["expiry_date"]
    )

    df["days_to_expiry"] = (
        df["expiry_date"] - today
    ).dt.days

    conditions = [
        df["days_to_expiry"] < 0,
        df["days_to_expiry"].between(0,7),
        df["days_to_expiry"].between(8,15)
    ]

    values = [
        "Expired",
        "Critical",
        "Near Expiry"
    ]

    df["expiry_status"] = "Good"

    for condition, value in zip(
        conditions,
        values
    ):
        df.loc[
            condition,
            "expiry_status"
        ] = value

    audit_candidates = df[
        (
            df["expiry_status"]
            != "Good"
        )
        &
        (
            df["inventory_qty"] > 0
        )
    ].copy()

    return audit_candidates
