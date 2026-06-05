import pandas as pd

def load_data():

    inventory = pd.read_csv("inventory.csv")

    sales = pd.read_csv("sales.csv")

    complaints = pd.read_csv("complaints.csv")

    return inventory, sales, complaints
