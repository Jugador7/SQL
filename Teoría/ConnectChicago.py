#Connect

%load_ext sql

import csv, sqlite3

con = sqlite3.connect("socioeconomic.db")
cur = con.cursor()
!pip install -q pandas==1.1.5

%sql sqlite:///socioeconomic.db

#Store the dataset in a Table
#In many cases the dataset to be analyzed is available as a .CSV (comma separated values) file, perhaps on the internet. To analyze the data using SQL, it first needs to be stored in the database.
#We will first read the csv files from the given url into pandas dataframes
#Next we will be using the df.to_sql() function to convert each csv file to a table in sqlite with the csv data loaded in it.

import pandas
df = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
df.to_sql("chicago_socioeconomic_data", con, if_exists='replace', index=False,method="multi")

%sql SELECT * FROM chicago_socioeconomic_data limit 5;

#How many rows are in the dataset

%sql SELECT COUNT(*) FROM chicago_socioeconomic_data;

#How many community areas in Chicago have a hardship index greater than 50.0?

%sql SELECT COUNT(community_area_name) FROM chicago_socioeconomic_data WHERE hardship_index > 50.0;

#What is the maximum value of hardship index in this dataset?

%sql SELECT MAX(hardship_index) FROM chicago_socioeconomic_data;

#Which community area which has the highest hardship index?

%sql SELECT community_area_name FROM chicago_socioeconomic_data where hardship_index = ( select max(hardship_index) from chicago_socioeconomic_data );

#Which Chicago community areas have per-capita incomes greater than $60,000?

%sql SELECT community_area_name FROM chicago_socioeconomic_data where per_capita_income_ > 60000;

#Create a scatter plot using the variables per_capita_income_ and hardship_index. Explain the correlation between the two variables.

import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

income_vs_hardship = %sql SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;
plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())
