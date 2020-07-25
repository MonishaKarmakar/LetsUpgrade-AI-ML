import numpy as np
import pandas as pd
dataset=pd.read_csv("general_data.csv")
print(dataset.head())
print(dataset.columns)
print("staticall analysis")
print("One sample t Test: where we compare Sample mean with population mean")
from scipy.stats import ttest_1samp
a= dataset.MonthlyIncome
stat,p=ttest_1samp(a,65)
print(stat,p)
print("One sample f Test: when dependent variable continous and independent variable is categorical")
import statsmodels.api as sm
from statsmodels.formula.api import ols
model=ols('Attrition~C(Age)',dataset).fit()
oneway=sm.stats.anova_lm(model,typ=2)
print(oneway)
mode2=ols('Attrition~C(MonthlyIncome)',dataset).fit()
oneway2=sm.stats.anova_lm(mode2,typ=2)
print(oneway2)