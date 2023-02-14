import pandas as pd
df=pd.read_csv("studentdetails.csv",usecols=["Roll No","Student Name"])
print(df)
#print(df.head())
#print(df.tail())
#print(df[["Segment","Country"]].head())
