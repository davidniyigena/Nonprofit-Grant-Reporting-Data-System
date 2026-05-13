# Project Summary: Nonprofit Grant Reporting Data System

## 1. Project Purpose

This project demonstrates how data analytics can support nonprofit grant reporting, donor accountability, compliance monitoring, and program performance tracking.

The goal is to show how grant data can be organized, cleaned, analyzed, summarized, and visualized to help nonprofit organizations manage donor-funded grants more effectively.

---

## 2. Background

Nonprofit organizations often manage multiple grants across donors, program areas, regions, and reporting periods. Each grant may include budget amounts, spending progress, reporting status, compliance requirements, and beneficiary reach.

Without a structured data system, it can be difficult to answer important questions such as:

- Which donors provide the largest grant amounts?
- Which program areas have the highest spending?
- Which grants have low spending rates?
- Which grants have delayed or incomplete reporting?
- Are there compliance issues that need follow-up?
- How many beneficiaries were reached by program area?
- Which grants require management attention?

This project creates a structured example of how Python, SQL, and dashboard-style reporting can support nonprofit grant management.

---

## 3. Dataset Description

The dataset used in this project is a sample nonprofit grant reporting dataset. It includes information about grants, donors, program areas, grant amounts, spending, beneficiaries, compliance issues, reporting status, regions, and reporting periods.

Key fields include:

- Grant ID
- Grant name
- Donor
- Program area
- Region
- Reporting period
- Grant amount
- Amount spent
- Beneficiaries reached
- Reporting status
- Compliance issue

Dataset file: `data/grant_reporting_data.csv`

---

## 4. Methods

This project uses a structured data analytics workflow.

### Data Cleaning

The Python script loads the dataset, checks missing values, reviews duplicate records, standardizes column names, creates calculated fields, and saves a cleaned dataset.

Script file: `scripts/01_data_cleaning_and_eda.py`

### SQL Analysis

SQL queries are used to summarize and analyze grant reporting data. The SQL file includes queries for donor funding, spending rates, program-area spending, compliance issues, reporting status, beneficiaries reached, and grants needing follow-up.

SQL file: `sql/grant_reporting_queries.sql`

### Visualization

The visualization script creates charts for grant amount by donor, amount spent by program area, spending rate by donor, reporting status, compliance issues, beneficiaries reached, and reporting-period spending trends.

Visualization script: `scripts/02_visualizations.py`

---

## 5. Key Analysis Questions

This project is designed to answer the following questions:

1. Which donors provide the highest total grant amounts?
2. Which program areas have the highest spending?
3. Which grants have low spending rates and may need follow-up?
4. Which grants have delayed or incomplete reporting?
5. Which grants have compliance issues?
6. How many beneficiaries were reached by program area?
7. How does spending progress change across reporting periods?

---

## 6. Expected Insights

This project is expected to produce insights such as:

- Some donors may contribute larger total grant amounts than others.
- Certain program areas may account for most grant spending.
- Grants with spending rates below 70% may require follow-up.
- Delayed or incomplete reports may signal reporting risks.
- Compliance issues may require additional documentation or review.
- Beneficiary reach can help connect financial reporting with program impact.

---

## 7. Tools Used

- Python
- SQL
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- CSV data files

---

## 8. Skills Demonstrated

This project demonstrates the following skills:

- Data cleaning
- Data transformation
- Exploratory data analysis
- SQL querying
- Grant reporting analytics
- Donor reporting
- Compliance monitoring
- Program performance tracking
- Beneficiary analysis
- Data visualization
- Dashboard planning
- Portfolio documentation

---

## 9. Portfolio Relevance

This project connects nonprofit grant management with data analytics and monitoring and evaluation. It demonstrates how structured data workflows can help organizations improve donor reporting, track spending, monitor compliance, and understand program reach.

This project is relevant for roles involving nonprofit data analytics, monitoring and evaluation, grants management, program reporting, donor reporting, compliance analytics, and social impact measurement.

---

## 10. Next Steps

Future improvements to this project may include:

- Adding generated chart images to the `visuals/` folder
- Updating the README with sample visualizations
- Creating a full Jupyter Notebook version of the analysis
- Adding a dashboard plan
- Building an interactive Google Looker Studio dashboard
- Expanding the dataset with more donors, grants, and reporting periods
- Adding predictive modeling to flag grants at risk of delayed reporting or low spending
