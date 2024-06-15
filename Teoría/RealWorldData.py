import csv, sqlite3

con = sqlite3.connect("RealWorldData.db")
cur = con.cursor()


!pip install -q pandas==1.1.5

%load_ext sql

%sql sqlite:///RealWorldData.db

import pandas
df = pandas.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.csv")
df.to_sql("CHICAGO_PUBLIC_SCHOOLS_DATA", con, if_exists='replace', index=False, method="multi")

