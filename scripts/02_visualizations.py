# Nonprofit Grant Reporting Data System
# Visualization Script
# Author: David Niyigena

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../data/grant_reporting_data.csv")

# Create spending rate
df["spending_rate"] = (df["amount_spent"] / df["grant_amount"]) * 100

# 1. Total grant amount by donor
grant_by_donor = (
    df.groupby("donor")["grant_amount"]
    .sum()
    .reset_index()
    .sort_values(by="grant_amount", ascending=False)
)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=grant_by_donor,
    x="donor",
    y="grant_amount"
)
plt.title("Total Grant Amount by Donor")
plt.xlabel("Donor")
plt.ylabel("Total Grant Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../visuals/grant_amount_by_donor.png")
plt.close()

# 2. Amount spent by program area
spent_by_program_area = (
    df.groupby("program_area")["amount_spent"]
    .sum()
    .reset_index()
    .sort_values(by="amount_spent", ascending=False)
)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=spent_by_program_area,
    x="program_area",
    y="amount_spent"
)
plt.title("Amount Spent by Program Area")
plt.xlabel("Program Area")
plt.ylabel("Amount Spent")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../visuals/amount_spent_by_program_area.png")
plt.close()

# 3. Spending rate by donor
spending_rate_by_donor = (
    df.groupby("donor")[["grant_amount", "amount_spent"]]
    .sum()
    .reset_index()
)

spending_rate_by_donor["spending_rate"] = (
    spending_rate_by_donor["amount_spent"] / spending_rate_by_donor["grant_amount"]
) * 100

spending_rate_by_donor = spending_rate_by_donor.sort_values(
    by="spending_rate",
    ascending=False
)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=spending_rate_by_donor,
    x="donor",
    y="spending_rate"
)
plt.title("Spending Rate by Donor")
plt.xlabel("Donor")
plt.ylabel("Spending Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../visuals/spending_rate_by_donor.png")
plt.close()

# 4. Reporting status summary
reporting_status_summary = (
    df["reporting_status"]
    .value_counts()
    .reset_index()
)

reporting_status_summary.columns = ["reporting_status", "count"]

plt.figure(figsize=(8, 5))
sns.barplot(
    data=reporting_status_summary,
    x="reporting_status",
    y="count"
)
plt.title("Reporting Status Summary")
plt.xlabel("Reporting Status")
plt.ylabel("Number of Grants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../visuals/reporting_status_summary.png")
plt.close()

# 5. Compliance issue summary
compliance_summary = (
    df["compliance_issue"]
    .value_counts()
    .reset_index()
)

compliance_summary.columns = ["compliance_issue", "count"]

plt.figure(figsize=(6, 4))
sns.barplot(
    data=compliance_summary,
    x="compliance_issue",
    y="count"
)
plt.title("Compliance Issue Summary")
plt.xlabel("Compliance Issue")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.savefig("../visuals/compliance_issue_summary.png")
plt.close()

# 6. Beneficiaries reached by program area
beneficiaries_by_program_area = (
    df.groupby("program_area")["beneficiaries_reached"]
    .sum()
    .reset_index()
    .sort_values(by="beneficiaries_reached", ascending=False)
)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=beneficiaries_by_program_area,
    x="program_area",
    y="beneficiaries_reached"
)
plt.title("Beneficiaries Reached by Program Area")
plt.xlabel("Program Area")
plt.ylabel("Beneficiaries Reached")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../visuals/beneficiaries_by_program_area.png")
plt.close()

# 7. Spending rate by reporting period
spending_by_period = (
    df.groupby("reporting_period")[["grant_amount", "amount_spent"]]
    .sum()
    .reset_index()
)

spending_by_period["spending_rate"] = (
    spending_by_period["amount_spent"] / spending_by_period["grant_amount"]
) * 100

plt.figure(figsize=(8, 5))
sns.lineplot(
    data=spending_by_period,
    x="reporting_period",
    y="spending_rate",
    marker="o"
)
plt.title("Spending Rate by Reporting Period")
plt.xlabel("Reporting Period")
plt.ylabel("Spending Rate (%)")
plt.tight_layout()
plt.savefig("../visuals/spending_rate_by_reporting_period.png")
plt.close()

print("Visualization files created successfully in the visuals folder.")
