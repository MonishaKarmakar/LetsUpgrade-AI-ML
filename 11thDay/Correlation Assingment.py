import pandas as pd
from scipy.stats import pearsonr
dataset=pd.read_csv("general_data.csv")
print(dataset.columns)
a1=dataset.Attrition
a2=dataset. Age
stat, p = pearsonr(a1,a2)
print("Correlation analysis bwtween Attrition and Age")
print(stat, p)

b1=dataset.Attrition
b2=dataset.DistanceFromHome
stat, p = pearsonr(b1,b2)
print("Correlation analysis bwtween Attrition and DistanceFromHome")
print(stat, p)
c1=dataset.Attrition
c2=dataset.Education
stat, p = pearsonr(c1,c2)
print("Correlation analysis bwtween Attrition and Education")
print(stat, p)

d1=dataset.Attrition
d2=dataset.JobLevel
stat, p = pearsonr(d1,d2)
print("Correlation analysis bwtween Attrition and JobLevel")
print(stat, p)
e1=dataset.Attrition
e2=dataset.MonthlyIncome
stat, p = pearsonr(e1,e2)
print("Correlation analysis bwtween Attrition and MonthlyIncome")
print(stat, p)
f1=dataset.Attrition
f2=dataset.PercentSalaryHike
stat, p = pearsonr(f1,f2)
print("Correlation analysis bwtween Attrition and PercentSalaryHike")
print(stat, p)
g1=dataset.Attrition
g2=dataset.TrainingTimesLastYear
stat, p = pearsonr(g1,g2)
print("Correlation analysis bwtween Attrition and TrainingTimesLastYear")
print(stat, p)
h1=dataset.Attrition
h2=dataset.YearsSinceLastPromotion
stat, p = pearsonr(h1,h2)
print("Correlation analysis bwtween Attrition and YearsSinceLastPromotion")
print(stat, p)

