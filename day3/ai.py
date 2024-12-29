import pandas as pd
import numpy as np
df=pd.read_excel('50rowssuperstore.xlsx')
print(df.groupby("Region")["Sales"].sum())
print(df.groupby(["Region","State"])["Sales"].sum())
print(df.groupby(["Region","State"])["Sales"].sum().reset_index())
print(df.groupby(["Region","State"])["Sales"].sum().sort_values())
print(df.groupby(["Region","State"])["Sales"].sum().sort_values(ascending=False).reset_index())
list1=[1,2,3,4,5,6,7,8,9,10]
print(list1)
list1.append(11)
print(list1)
print(dir(list1))

df["Sales"]=df["Sales"].replace(0,np.nan)
df["Quantity"]=df["Quantity"].replace(0,np.nan)
df["Result"]=df["Sales"]/df["Quantity"]
df.to_csv("answer.csv")
#df["Division"]=np.where