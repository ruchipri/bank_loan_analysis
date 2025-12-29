#Bank loan  Analysis 
#Import  required libraries 
import pandas  as pd 
##pd.set_option('display.max_columns', None)
##pd.set_option('display.width', None)
import numpy as np

#import openpyxl as op
import matplotlib.pyplot as plt 
#import seaborn as sns
#import warnings 
#import plotly.express  as px

#import data set 
df = pd.read_excel("C:/Users/ruchi/Downloads/financial_loan.xlsx")
print(df.head())
#META DATA  OF DATA 
print("Numbers of row:", df.shape[0])
print("Numbers of columns :" ,df.shape[1])
#Total loan  appliaction
total_loan_appliacation = df['id'].count()
print("Total loan application:",total_loan_appliacation )
# Month to date total Loan Appliaction
latest_issue_date = df['issue_date'].max()
print(latest_issue_date)
latest_year = latest_issue_date.year
print(latest_year)
latest_month = latest_issue_date.month
print(latest_month)
latest_year = latest_issue_date.year
mtd_data = df[(df['issue_date'].dt.year == latest_year) & (df['issue_date'].dt.month == latest_month)]
print(mtd_data)
mtd_application = mtd_data['id'].count()
print(mtd_application)
print(f"MTD loan application for {latest_issue_date.strftime('%b %Y')}: {mtd_application}")

# Total funded  amount 
total_funded_amount = df['loan_amount'].sum()
print(" Total funded  amount:" ,total_funded_amount)
total_funded_amount_millions = total_funded_amount/1000000
print("Total funded Amount: ${:.2f}M".format(total_funded_amount_millions))

# Month to date total funded  amount 
latest_issue_date = df['issue_date'].max()
latest_year = latest_issue_date.year
latest_month = latest_issue_date.month

mtd_data = df[(df['issue_date'].dt.year == latest_year) & (df["issue_date"].dt.month == latest_month)]
print(mtd_data)
mtd_total_funded_amount = mtd_data['loan_amount'].sum()
mtd_total_funded_amount_million = mtd_total_funded_amount /1000000
print(" Total_funded_amount_millions ${:.2f}M".format(mtd_total_funded_amount_million))

#Average  Interst rate
avg_interst_rate = df['int_rate'].mean()*100
print(" Average Interest rate :{: .2f}%".format(avg_interst_rate))

#Average debt to income ratio (DTI)
avg_debt_to_interest_ratio = df['dti'].mean()*100
print(" Average Idebt to income ratio :{: .2f}%".format(avg_debt_to_interest_ratio))

# Good loan matrix 
good_loan = df[df['loan_status'].isin (["Current", "Fully Paid"])]
print("good loan 1:" , good_loan ,(df["loan_status"]))

total_loans = df['id'].count()
print( "Total loans :",total_loans)
total_good_loans = good_loan['id'].count()
print("total good loans :" ,total_good_loans)
good_loan_funded_amount = good_loan['loan_amount'].sum()
good_loan_funded_amount_millions = good_loan_funded_amount/1000000
good_loan_received_amount = good_loan['total_payment'].sum()
good_loan_received_amount_millions = good_loan_received_amount/1000000
percentage_of_good_loans = total_good_loans/total_loans *100
print("Good loan appliaction :" , total_good_loans )
print(" Good loan funded  amount  : ${:.2f}M".format(good_loan_funded_amount_millions))
print(" Good loan recieved amount : ${:.2f}M".format(good_loan_received_amount_millions))
print("percentage_of_good_loans : {:.2f}%".format(percentage_of_good_loans ))

## Monthly trend by issue  dates for total funded  amount 
import matplotlib.pyplot as plt
import numpy as np
monthly_trend = df.sort_values('issue_date').assign(month_name = lambda x: x['issue_date'].dt.strftime('%b %Y')).groupby('month_name',sort = False)['loan_amount'].sum().div(1000000).reset_index(name= 'loan_amount_millions')
print("P", monthly_trend)
plt.plot(monthly_trend['month_name'], monthly_trend['loan_amount_millions'],marker = 'o', color = 'b', ls = '-')
plt.fill_between(monthly_trend['month_name'], monthly_trend['loan_amount_millions'], color ='green', alpha =.5)
for i, row in  monthly_trend.iterrows():
    plt.text(i,row['loan_amount_millions'] +.1, f"{row['loan_amount_millions']: .2f}", ha ='center' , va = 'bottom', fontsize=9, color ='b')
plt.xlabel('Month')
plt.ylabel('Loan amount')
plt.show()

## Monthly trend by issue  dates for total received amount 
monthly_recieved_amount = df.sort_values('issue_date').assign(month_name = lambda x: x['issue_date'].dt.strftime('%b %Y')).groupby('month_name',sort = False)['loan_amount'].sum().div(1000000).reset_index(name = "amount_recieved_millions")
print(monthly_recieved_amount)
plt.plot(monthly_recieved_amount['month_name'],monthly_recieved_amount['amount_recieved_millions'], marker ='o', color ='green', ls =':')
plt.fill_between(monthly_recieved_amount['month_name'],monthly_recieved_amount['amount_recieved_millions'], color ='pink', alpha = .5)
plt.title('Amount  recieved monthly', fontsize =10, color = 'green')
plt.xlabel('Month_name', color  ='Black', fontsize = 10)
plt.ylabel('Amount_recieved_millions', color = 'Black', fontsize= 10) 
for i, row in monthly_recieved_amount.iterrows():
    plt.text(i, row['amount_recieved_millions'] +.1, f"{row['amount_recieved_millions'] : .2f}",  ha = 'center', va= 'bottom', color = 'green', fontsize = 5)
plt.show()

Regional  Analysis by  state
state_funding= df.groupby('address_state')['loan_amount'].sum().sort_values(ascending= False)
state_funding_thousands = state_funding/1000
print(state_funding)

##loan term analysis 
loan = df.groupby('term')['loan_amount'].count().sort_values(ascending = False)
print(loan)
## employee lenght  total funded  amount 
employee_lenght = df.groupby('emp_length')['loan_amount'].sum().sort_values(ascending= False).div(1000)

print(employee_lenght)

