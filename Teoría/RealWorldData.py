import csv, sqlite3

con = sqlite3.connect("RealWorldData.db")
cur = con.cursor()


!pip install -q pandas==1.1.5

%load_ext sql

%sql sqlite:///RealWorldData.db

