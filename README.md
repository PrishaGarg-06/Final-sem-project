# Final-sem-project

Project Overview

Inventory quality plays a critical role in retail and quick-commerce operations. Products approaching expiry or already expired can lead to customer dissatisfaction, increased complaints, inventory losses, and operational inefficiencies.

This project automates the identification of high-risk inventory items by analyzing inventory, sales, and complaint data. The system evaluates product expiry status, calculates priority scores, and automatically generates audit tasks for store teams to review and take corrective actions.

The project demonstrates how data-driven decision making can be used to improve inventory quality monitoring and streamline audit operations.

Problem Statement : Traditional inventory audits are often conducted manually and depend on store personnel identifying products that require attention. Due to the large number of SKUs handled daily, manual audits can become inconsistent and time-consuming.

As a result:
1. Expired products may remain on shelves.
2. Near-expiry inventory may not be identified proactively.
3. Customer complaints related to product quality may increase.
4. Audit efforts may not focus on the most critical items.

To address these challenges, this project automates the audit candidate identification process and prioritizes products based on inventory risk indicators.

Solution Approach :-

The system follows a multi-step workflow:

Load inventory, sales, and complaint datasets.
Merge all datasets into a unified view.
Calculate remaining days to expiry for each product.
Classify products into risk categories: Expired / Critical / Near Expiry / Good
Calculate a weighted priority score using: Expiry severity, Customer complaints, Sales velocity, Inventory quantity
Rank products within each outlet.
Generate audit tasks for the highest priority products.
Export audit tasks for operational use.


Project Structure :
inventory-audit-automation/
│
├── inventory.csv
├── sales.csv
├── complaints.csv
│
├── data_loader.py
├── audit_engine.py
├── scoring_engine.py
├── task_generator.py
├── main.py
│
├── audit_tasks.csv
├── requirements.txt
└── README.md


Input Datasets:- 
1. Inventory Dataset : Contains product-level inventory information.

Column	Description
outlet_id	Store identifier
item_id	Product identifier
item_name	Product name
inventory_qty	Available inventory quantity
expiry_date	Product expiry date
shelf_life	Product shelf life

2. Sales Dataset : Contains recent product sales information.

Column	Description
outlet_id	Store identifier
item_id	Product identifier
qty_sold_l7d	Quantity sold in last 7 days

3. Complaint Dataset : Contains customer complaint information.

Column	Description
outlet_id	Store identifier
item_id	Product identifier
complaints_l7d	Complaints received in last 7 days

4. Audit Logic :
Expiry Classification

Products are categorized based on remaining shelf life:
Days_to_expiry	Status
< 0	Expired
0 - 7	Critical
8 - 15	Near Expiry
> 15	Good

Only products classified as Expired, Critical, or Near Expiry are considered for audit generation.


Priority Scoring - The system calculates a priority score using multiple risk indicators.
Expiry Score - Higher risk is assigned to products closer to expiry.
Complaint Score - Products with more customer complaints receive higher scores.
Sales Score - Fast-selling products are prioritized because they impact more customers.
Inventory Score - Products with larger inventory quantities receive additional weight due to higher potential inventory loss.
The final score is calculated using weighted components to determine audit priority.

After scoring:
Products are ranked within each outlet.
Top-ranked products are selected.
Audit tasks are generated automatically.
Tasks are assigned an OPEN status.
Results are exported to a CSV file.

Sample output:
outlet_id	item_id	item_name	priority_score	task_status
1001	10004	Curd	34.5	OPEN
1002	10007	Juice	32.8	OPEN
1007	10031	Cake	31.4	OPEN

Technologies Used : 
1. Python
2. Pandas
3. NumPy
4. CSV Data Processing

Key Features :
Automated audit candidate identification
Expiry risk monitoring
Complaint-based prioritization
Sales-driven audit ranking
Outlet-level task generation
Modular pipeline architecture
Exportable audit task output
Future Enhancements
Dashboard for audit monitoring
Automated email notifications
Real-time inventory integration
Machine learning based risk prediction
Store performance analytics
Automated audit scheduling

How to Run :
1. Install dependencies: pip install -r requirements.txt
2. Run the project: python main.py
3. Generated audit tasks will be available in: audit_tasks.csv
