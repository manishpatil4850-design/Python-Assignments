import numpy as np
import pandas as pd
df = pd.read_csv("output.csv")
df.columns = df.columns.str.strip()
df["Department"] = df["Department"].astype(str).str.strip().str.upper()
df["Join_Date"] = pd.to_datetime(df["Join_Date"], format="mixed", errors="coerce")
df["Join_Year"] = df["Join_Date"].dt.year
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# 1. Filtering: High-earning IT professionals
high_earning_engineers = df[(df["Department"] == "IT") & (df["Salary"] > 30000)].copy()

# 2. Sorting: By Join_Year & Salary (Descending), Age (Ascending)
sorted_df = df.sort_values(
    by=["Join_Year", "Salary", "Age"],
    ascending=[False, False, True]
)

# 3. Conditional selection: Top Performance (Joined <= 2018)
top_performers = df.loc[df["Join_Year"] <= 2018, ["Department", "Salary"]].copy()

# 4. Conditional Column Insertion
df["Bonus_Eligible"] = np.where(df["Join_Year"] <= 2018, "Yes", "No")

# --- DISPLAY RESULTS ---
print("=== Filtered: High Earning Engineers ===")
print(high_earning_engineers.to_string())

print("\n=== Sorted : By Join_Year & Salary (Descending), Age (Ascending) ===")
print(sorted_df.to_string())

print("\n=== Conditional Selection : Top Performance (Joined <= 2018) ===")
print(top_performers.to_string())

print("\n=== Final DataFrame with conditional Column ===")
print(df.to_string())