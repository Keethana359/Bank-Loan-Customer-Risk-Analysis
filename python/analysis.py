import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("bank.csv")

print(df.head())

# Rename columns
df.rename(columns={'age': 'customer_age'}, inplace=True)

# Age distribution
df['customer_age'].plot(kind='hist', bins=20, title='Customer Age Distribution')
plt.show()

# Loan subscription count
loan_status = df['y'].value_counts()
print(loan_status)

loan_status.plot(kind='bar', title='Loan Subscription')
plt.show()

# Job vs loan approval
job_loan = pd.crosstab(df['job'], df['y'])
print(job_loan)