# Nonprofit Grant Reporting Data System
# Data Cleaning and Exploratory Data Analysis
# Author: David Niyigena

import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("../data/grant_reporting_data.csv")

# Preview data
print("First five rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nDataset information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Check duplicate records
duplicate_count = df.duplicated().sum()
print(f"\nDuplicate records: {duplicate_count}")

# Create spending rate
df["spending_rate"] = (df["amount_spent"] / df["grant_amount"]) * 100

# Create remaining balance
df["remaining_balance"] = df["grant_amount"] - df["amount_spent"]

# Create performance category
def categorize_spending(rate):
    if rate >= 90:
        return "High Spending"
    elif rate >= 70:
        return "On Track"
    else:
        return "Needs Follow-Up"

df["spending_category"] = df["spending_rate"].apply(categorize_spending)

# Summary statistics
print("\nSummary statistics:")
print(df[["grant_amount", "amount_spent", "remaining_balance", "beneficiaries_reached", "spending_rate"]].describe())

# Grant amount by donor
donor_summary = (
    df.groupby("donor")[["grant_amount", "amount_spent"]]
    .sum()
    .reset_index()
)

donor_summary["spending_rate"] = (
    donor_summary["amount_spent"] / donor_summary["grant_amount"]
) * 100

print("\nGrant summary by donor:")
print(donor_summary)

# Spending by program area
program_area_summary = (
    df.groupby("program_area")[["grant_amount", "amount_spent", "beneficiaries_reached"]]
    .sum()
    .reset_index()
)

program_area_summary["spending_rate"] = (
    program_area_summary["amount_spent"] / program_area_summary["grant_amount"]
) * 100

print("\nProgram area summary:")
print(program_area_summary)

# Reporting status summary
reporting_status_summary = (
    df["reporting_status"]
    .value_counts()
    .reset_index()
)

reporting_status_summary.columns = ["reporting_status", "count"]

print("\nReporting status summary:")
print(reporting_status_summary)

# Compliance issue summary
compliance_summary = (
    df["compliance_issue"]
    .value_counts()
    .reset_index()
)

compliance_summary.columns = ["compliance_issue", "count"]

print("\nCompliance issue summary:")
print(compliance_summary)

# Grants needing follow-up
follow_up_grants = df[
    (df["spending_rate"] < 70) |
    (df["reporting_status"].isin(["Delayed", "Incomplete"])) |
    (df["compliance_issue"] == "Yes")
]

print("\nGrants needing follow-up:")
print(follow_up_grants[[
    "grant_id",
    "grant_name",
    "donor",
    "program_area",
    "reporting_status",
    "compliance_issue",
    "spending_rate"
]])

# Save cleaned dataset
df.to_csv("../data/cleaned_grant_reporting_data.csv", index=False)

print("\nCleaned dataset saved to data/cleaned_grant_reporting_data.csv")
