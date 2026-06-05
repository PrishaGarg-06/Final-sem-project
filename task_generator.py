from datetime import datetime

def generate_tasks(df):

    df = df.sort_values(
        "priority_score",
        ascending=False
    )

    df["outlet_rank"] = (
        df.groupby("outlet_id")
        ["priority_score"]
        .rank(
            ascending=False,
            method="dense"
        )
    )

    tasks = df[
        df["outlet_rank"] <= 5
    ].copy()

    tasks["task_type"] = (
        "Expiry Audit"
    )

    tasks["task_status"] = (
        "OPEN"
    )

    tasks["created_at"] = (
        datetime.now()
    )

    return tasks
