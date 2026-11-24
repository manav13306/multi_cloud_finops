import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
start_date = datetime(2025, 1, 1)
days = 365
date_range = [start_date + timedelta(days=i) for i in range(days)]

providers = ['AWS', 'Azure', 'GCP']
environments = ['Production', 'Staging', 'Development']
business_units = ['Core Platform', 'Data & AI', 'E-Commerce', 'InfraOps']
service_cats = ['Compute (EC2/VM)', 'Storage (S3/Blob)', 'Database (RDS)', 'Networking']

records = []
for single_date in date_range:
    is_weekend = single_date.weekday() >= 5
    for bu in business_units:
        for prov in providers:
            for _ in range(np.random.randint(1, 4)):
                env = np.random.choice(environments, p=[0.55, 0.25, 0.20])
                service = np.random.choice(service_cats)
                
                base_budget = np.random.uniform(50, 400)
                
                # Weekend idle waste anomaly simulation in dev/staging
                if is_weekend and env in ['Development', 'Staging']:
                    actual_cost = base_budget * np.random.uniform(0.9, 1.4)
                else:
                    actual_cost = base_budget * np.random.uniform(0.7, 1.15)
                
                # Random billing spike anomaly
                if np.random.rand() < 0.003:
                    actual_cost *= 4.5

                records.append({
                    "Date": single_date.strftime('%Y-%m-%d'),
                    "Provider": prov,
                    "Service_Category": service,
                    "Environment": env,
                    "Business_Unit": bu,
                    "Project_ID": f"PRJ-{np.random.randint(101, 108)}",
                    "Account_ID": f"ACC-{abs(hash(bu + prov)) % 100000:05d}",
                    "Budget": round(base_budget, 2),
                    "Actual_Cost": round(actual_cost, 2)
                })

df = pd.DataFrame(records)
df.to_csv("cloud_billing_dataset.csv", index=False)
print("Saved cloud_billing_dataset.csv successfully!")