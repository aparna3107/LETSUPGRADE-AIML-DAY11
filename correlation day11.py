# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt                              
dataset1=pd.read_excel("DS.xlsx",sheet_name=1)


# H(0):THERE IS NO SIGNIFICANT RELATION BETWEEN AGE & EDUCATION
dataset2=dataset1[['Age','Education']].head(40)
from scipy.stats import pearsonr
stats,p=pearsonr(dataset2.Age, dataset2.Education)
print(stats,p)
plt.scatter(dataset2.Age,dataset2.Education)
print(" from observing scatter plot we understood very less correlation between Age n Education")
print("SINCE p>0.05 ACCEPT NULL HYPOTHESIS H(0):THERE IS NO SIGNIFICANT RELATION BETWEEN AGE & EDUCATION")
# CONSIDER A SAMPLE OF 40 DATA; r= 0.0614(from program output);Assume alpha=0.05; dof= 40-2=38;
print(" Calculated value of tstat=0.379, table value of t=2.021, since calculated t value less than table value of t, ACCEPT NULL HYPOTHESIS H(0)")


# H(1):THERE IS NO SIGNIFICANT RELATION BETWEEN AGE & DISTANCE FROM HOME
dataset2=dataset1[['Age','DistanceFromHome']].head(40)
stats,p=pearsonr(dataset2.Age, dataset2.DistanceFromHome)
print(stats,p)
plt.scatter(dataset2.Age,dataset2.DistanceFromHome)
print(" from observing scatter plot we understood very less negatively correlation between Age n DistanceFromHome")
print("SINCE p>0.05 ACCEPT NULL HYPOTHESIS H(1):THERE IS NO SIGNIFICANT RELATION BETWEEN AGE & DISTANCE FROM HOME")
# CONSIDER A SAMPLE OF 40 DATA; r= -0.09(from program output);Assume alpha=0.05; dof= 40-2=38;
print(" Calculated value of tstat=-0.557, table value of t=2.021, since calculated t value less than table value of t, ACCEPT NULL HYPOTHESIS H(1)")


# H(2):THERE IS NO SIGNIFICANT RELATION BETWEEN AGE & JobTime
dataset2=dataset1[['Age','JobTime']].head(40)
stats,p=pearsonr(dataset2.Age, dataset2.JobTime)
print(stats,p)
plt.scatter(dataset2.Age,dataset2.JobTime)
print(" from observing scatter plot we understood less positive correlation between Age n JobTime")
print("SINCE p>0.05 ACCEPT NULL HYPOTHESIS(2):THERE IS NO SIGNIFICANT RELATION BETWEEN AGE & JobTime")
# CONSIDER A SAMPLE OF 40 DATA; r= 0.29(from program output);Assume alpha=0.05; dof= 40-2=38;
print(" Calculated value of tstat=1.867, table value of t=2.021, since calculated t value less than table value of t, ACCEPT NULL HYPOTHESIS H(2)")


# H(3):THERE IS NO SIGNIFICANT RELATION BETWEEN AGE & PREVIOUS EXPERIENCE
dataset2=dataset1[['Age','PrevExep']].head(40)
stats,p=pearsonr(dataset2.Age, dataset2.PrevExep)
print(stats,p)
plt.scatter(dataset2.Age,dataset2.PrevExep)
print(" from observing scatter plot we understood less positive correlation between Age n PrevExep")
print("SINCE p>0.05 ACCEPT NULL HYPOTHESIS H(3):THERE IS NO SIGNIFICANT RELATION BETWEEN AGE & PREVIOUS EXPERIENCE")
# CONSIDER A SAMPLE OF 40 DATA; r= 0.147(from program output);Assume alpha=0.05; dof= 40-2=38;
print(" Calculated value of tstat=0.916, table value of t=2.021, since calculated t value less than table value of t, ACCEPT NULL HYPOTHESIS H(3)")


# H(4):THERE IS NO SIGNIFICANT RELATION BETWEEN AGE & MONTHLY INCOME
dataset2=dataset1[['Age','MonthlyIncome']].head(40)
stats,p=pearsonr(dataset2.Age, dataset2.MonthlyIncome)
print(stats,p)
plt.scatter(dataset2.Age,dataset2.MonthlyIncome)
print(" from observing scatter plot we understood less positive correlation between Age n MONTHLY INCOME")
print("SINCE p>0.05 ACCEPT NULL HYPOTHESIS H(4):THERE IS NO SIGNIFICANT RELATION BETWEEN AGE & MONTHLY INCOME")
# CONSIDER A SAMPLE OF 40 DATA; r= 0.026(from program output);Assume alpha=0.05; dof= 40-2=38;
print(" Calculated value of tstat=0.16, table value of t=2.021, since calculated t value less than table value of t, ACCEPT NULL HYPOTHESIS H(4)")


# H(5):THERE IS NO SIGNIFICANT RELATION BETWEEN AGE & TotalWorkingYears
dataset2=dataset1[['Age','TotalWorkingYears']].head(40)
stats,p=pearsonr(dataset2.Age, dataset2.TotalWorkingYears)
print(stats,p)
plt.scatter(dataset2.Age,dataset2.TotalWorkingYears)
print(" from observing scatter plot we understood less positive correlation between Age n TotalWorkingYears")
print("SINCE p>0.05 ACCEPT NULL HYPOTHESIS  H(6):THERE IS NO SIGNIFICANT RELATION BETWEEN AGE & TotalWorkingYears")
# CONSIDER A SAMPLE OF 40 DATA; r= 0.158(from program output);Assume alpha=0.05; dof= 40-2=38;
print(" Calculated value of tstat=0.986, table value of t=2.021, since calculated t value less than table value of t, ACCEPT NULL HYPOTHESIS H(5)")



# H(6):THERE IS NO SIGNIFICANT RELATION BETWEEN Education & TotalWorkingYears  
dataset2=dataset1[['Education','TotalWorkingYears']].head(40)
stats,p=pearsonr(dataset2.Education, dataset2.TotalWorkingYears)
print(stats,p)
plt.scatter(dataset2.Education,dataset2.TotalWorkingYears)
print(" from observing scatter plot we understood highly positive correlation between Education &  TotalWorkingYears")
print("SINCE p<0.05 REJECT NULL HYPOTHESIS & ACCEPT ALTERNATE HYPOTHESIS  H(A):THERE IS SIGNIFICANT RELATION BETWEEN Education &  TotalWorkingYears")
# CONSIDER A SAMPLE OF 40 DATA; r= 1(from program output);Assume alpha=0.05; dof= 40-2=38;


# H(7):THERE IS NO SIGNIFICANT RELATION BETWEEN Education & MonthlyIncome  
dataset2=dataset1[['Education','MonthlyIncome']].head(40)
stats,p=pearsonr(dataset2.Education, dataset2.MonthlyIncome)
print(stats,p)
plt.scatter(dataset2.Education,dataset2.MonthlyIncome)
print(" from observing scatter plot we understood positive correlation between Education &  MonthlyIncome")
print("SINCE p<0.05 REJECT NULL HYPOTHESIS & ACCEPT ALTERNATE HYPOTHESIS  H(A):THERE IS SIGNIFICANT RELATION BETWEEN Education &  MonthlyIncome")
# CONSIDER A SAMPLE OF 40 DATA; r= 0.45(from program output);Assume alpha=0.05; dof= 40-2=38;
print(" Calculated value of tstat=3.106, table value of t=2.021, since calculated t value greater than table value of t, REJECT NULL HYPOTHESIS H(5) & ACCEPT ALTERNATE HYPOTHESIS H(A):THERE IS SIGNIFICANT RELATION BETWEEN Education & MonthlyIncome  ")


# H(8):THERE IS NO SIGNIFICANT RELATION BETWEEN Education & JobTime  
dataset2=dataset1[['Education','JobTime']].head(40)
stats,p=pearsonr(dataset2.Education, dataset2.JobTime)
print(stats,p)
plt.scatter(dataset2.Education,dataset2.JobTime)
print(" from observing scatter plot we understood positive correlation between Education &  JobTime")
print("SINCE p>0.05 ACCEPT NULL HYPOTHESIS  H(8):THERE IS NO SIGNIFICANT RELATION BETWEEN Education & JobTime   ")
# CONSIDER A SAMPLE OF 40 DATA; r= 0.18(from program output);Assume alpha=0.05; dof= 40-2=38;
print(" Calculated value of tstat=1.128, table value of t=2.021, since calculated t value less than table value of t,accept null hypothesis ")


# H(8):THERE IS NO SIGNIFICANT RELATION BETWEEN Education & CurrentSalary
dataset2=dataset1[['Education','CurrentSalary']].head(40)
stats,p=pearsonr(dataset2.Education, dataset2.CurrentSalary)
print(stats,p)
plt.scatter(dataset2.Education,dataset2.CurrentSalary)
print(" from observing scatter plot we understood positive correlation between Education & CurrentSalary")
print("SINCE p<0.05 REJECT NULL HYPOTHESIS & ACCEPT ALTERNATE HYPOTHESIS H(A):THERE IS SIGNIFICANT RELATION BETWEEN Education & CurrentSalary   ")
# CONSIDER A SAMPLE OF 40 DATA; r= 0.48(from program output);Assume alpha=0.05; dof= 40-2=38;
print(" Calculated value of tstat=3.37, table value of t=2.021, since calculated t value GREATER than table value of t,REJECT null hypothesis & ACCEPT ALTERNATE HYPOTHESIS ")
