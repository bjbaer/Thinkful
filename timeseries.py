import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import statsmodels
import statsmodels.api as sm


df = pd.read_csv('LoanStats3b.csv', header=1, low_memory=False)

# converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d']) #creates a new column based on the string
dfts = df.set_index('issue_d_format')  #creates a new variable that is just an array based on the column of the dataframe above
#create a lambda function that takes the year from the input x, multiplies it by 100, then adds the count of months and groups it
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count() 
loan_count_summary = year_month_summary['issue_d'] #creates a new variabel based on the above line issue dates

print loan_count_summary
plt.plot(loan_count_summary)
plt.show()



loan_count_summary_diff = loan_count_summary.diff()
loan_count_summary_diff = loan_count_summary_diff.fillna(0)

plt.plot(loan_count_summary_diff)

loan_count_summary_diff = loan_count_summary_diff + 316


loan_count_summary_diff = loan_count_summary_diff/max(loan_count_summary_diff)

plt.plot(loan_count_summary_diff)
sm.graphics.tsa.plot_acf(loan_count_summary_diff) # autocorrelation
sm.graphics.tsa.plot_pacf(loan_count_summary_diff) # partial autocorrelation
