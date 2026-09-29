import pandas as pd

file_path = "C:/Users/CC/Downloads/employee_dirty_data_30 - Copy.csv"
df = pd.read_csv(file_path)
# Wrapped df in str() to satisfy linter type constraints
print("Dataset imported successfully! \n", str(df))

# 2. Remove duplicates
duplicate_count = df.duplicated().sum()
print(f"Number of duplicate values: {duplicate_count}")
df_cleaned = df.drop_duplicates().copy()

print("\nMissing values per column before cleaning: ")
# Wrapped series in str() to fix __str__ or __repr__ warnings
print(str(df_cleaned.isnull().sum()))

# Calculate and fill missing values for Age
median_age = df_cleaned["Age"].median()
df_cleaned["Age"] = df_cleaned["Age"].fillna(median_age).astype(int)

# Calculate and fill missing values for Salary
mean_salary = df_cleaned["Salary"].mean()
df_cleaned["Salary"] = df_cleaned["Salary"].fillna(mean_salary)

# Clean Text Fields
df_cleaned["Department"] = df_cleaned["Department"].fillna("Unassigned").str.strip().str.title()
df_cleaned["Full Name"] = df_cleaned["Full Name"].str.strip().str.title()

# Process Dates and Names
df_cleaned["Join_Date"] = pd.to_datetime(df_cleaned["Join_Date"], format="mixed", errors="coerce")
df_cleaned[["First_Name", "Last_Name"]] = df_cleaned["Full Name"].str.split(" ", n=1, expand=True)
df_cleaned["Join_Year"] = df_cleaned["Join_Date"].dt.year.astype("Int64")

df_cleaned = df_cleaned.drop(columns=["Full Name"])

# Reorder Columns
ordered_columns = [
    "Employee_ID", "First_Name", "Last_Name",
    "Department", "Age", "Salary", "Join_Date", "Join_Year"
]
ordered_columns = [col for col in ordered_columns if col in df_cleaned.columns]
df_cleaned = df_cleaned[ordered_columns]

# Output Results
print("\n -------- processed dataframe --------")
# Wrapped df_cleaned in str() to clear warning
print(str(df_cleaned))

print("\n---------- data types info--------")
# Wrapped dtypes in str() to clear warning
print(str(df_cleaned.dtypes))

# Excluded index column from final export
df_cleaned.to_csv("output.csv", index=False)