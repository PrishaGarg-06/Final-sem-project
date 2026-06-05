from data_loader import load_data
from audit_engine import identify_candidates
from scoring_engine import calculate_priority
from task_generator import generate_tasks

inventory, sales, complaints = load_data()

df = inventory.merge(
    sales,
    on=["outlet_id","item_id"],
    how="left"
)

df = df.merge(
    complaints,
    on=["outlet_id","item_id"],
    how="left"
)

df["qty_sold_l7d"] = (
    df["qty_sold_l7d"]
    .fillna(0)
)

df["complaints_l7d"] = (
    df["complaints_l7d"]
    .fillna(0)
)

candidates = identify_candidates(df)

scored = calculate_priority(
    candidates
)

tasks = generate_tasks(
    scored
)

tasks.to_csv(
    "audit_tasks.csv",
    index=False
)

print("=" * 50)
print("INVENTORY AUDIT AUTOMATION")
print("=" * 50)

print(
    f"Inventory Records Processed : {len(df)}"
)

print(
    f"Audit Candidates : {len(candidates)}"
)

print(
    f"Tasks Generated : {len(tasks)}"
)

print(
    f"Outlets Covered : "
    f"{tasks['outlet_id'].nunique()}"
)

print(
    f"Average Priority Score : "
    f"{round(tasks['priority_score'].mean(),2)}"
)

print("\nTop 10 Audit Tasks\n")

print(
    tasks[
        [
            "outlet_id",
            "item_id",
            "item_name",
            "priority_score"
        ]
    ]
    .head(10)
)
