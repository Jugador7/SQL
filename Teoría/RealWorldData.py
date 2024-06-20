import csv, sqlite3

con = sqlite3.connect("RealWorldData.db")
cur = con.cursor()


!pip install -q pandas==1.1.5

%load_ext sql

%sql sqlite:///RealWorldData.db

import pandas
df = pandas.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.csv")
df.to_sql("CHICAGO_PUBLIC_SCHOOLS_DATA", con, if_exists='replace', index=False, method="multi")

# type in your query to retrieve list of all tables in the database
%sql SELECT name FROM sqlite_master WHERE type='table'

# type in your query to retrieve the number of columns in the SCHOOLS table
%sql SELECT count(name) FROM PRAGMA_TABLE_INFO('CHICAGO_PUBLIC_SCHOOLS_DATA');

# type in your query to retrieve all column names in the SCHOOLS table along with their datatypes and length
%sql SELECT name,type,length(type) FROM PRAGMA_TABLE_INFO('CHICAGO_PUBLIC_SCHOOLS_DATA');

#Elementary schools in the dataset:

%sql SELECT COUNT(*) FROM CHICAGO_PUBLIC_SCHOOLS_DATA where "Elementary, Middle, or High School"='ES'

#Max safety score:
%sql select MAX(SAFETY_SCORE) from CHICAGO_PUBLIC_SCHOOLS_DATA

#Which schools have highest Safety Score?
%sql select Name_of_School, Safety_Score from CHICAGO_PUBLIC_SCHOOLS_DATA where \
  Safety_Score= (select MAX(Safety_Score) from CHICAGO_PUBLIC_SCHOOLS_DATA)

# What are the top 10 schools with the highest "Average Student Attendance"?
%sql select Name_of_School, Average_Student_Attendance from CHICAGO_PUBLIC_SCHOOLS_DATA \
    order by Average_Student_Attendance desc nulls last limit 10 

##### Retrieve the list of 5 Schools with the lowest Average Student Attendance sorted in ascending order based on attendance
%sql SELECT Name_of_School, Average_Student_Attendance  \
     from CHICAGO_PUBLIC_SCHOOLS_DATA \
     order by Average_Student_Attendance \
     LIMIT 5

##### Now remove the '%' sign from the above result set for Average Student Attendance column

%sql SELECT Name_of_School, REPLACE(Average_Student_Attendance, '%', '') \
     from CHICAGO_PUBLIC_SCHOOLS_DATA \
     order by Average_Student_Attendance \
     LIMIT 5

##### Which Schools have Average Student Attendance lower than 70%?

%sql SELECT Name_of_School, Average_Student_Attendance  \
     from CHICAGO_PUBLIC_SCHOOLS_DATA \
     where CAST ( REPLACE(Average_Student_Attendance, '%', '') AS DOUBLE ) < 70 \
     order by Average_Student_Attendance

##### Get the total College Enrollment for each Community Area
%sql select Community_Area_Name, sum(College_Enrollment) AS TOTAL_ENROLLMENT \
   from CHICAGO_PUBLIC_SCHOOLS_DATA \
   group by Community_Area_Name 

  ##### Get the 5 Community Areas with the least total College Enrollment  sorted in ascending order
%sql select Community_Area_Name, sum(College_Enrollment) AS TOTAL_ENROLLMENT \
   from CHICAGO_PUBLIC_SCHOOLS_DATA \
   group by Community_Area_Name \
   order by TOTAL_ENROLLMENT asc \
   LIMIT 5 

##### List 5 schools with lowest safety score.

%sql SELECT name_of_school, safety_score \
FROM CHICAGO_PUBLIC_SCHOOLS_DATA  where safety_score !='None' \
ORDER BY safety_score \
LIMIT 5

##### Get the hardship index for the community area which has the highest value for College Enrollment

%%sql
SELECT community_area_name 
FROM CHICAGO_CENSUS_DATA
WHERE community_area_number = (
    SELECT community_area_number 
    FROM CHICAGO_CRIME_DATA 
    GROUP BY community_area_number
    ORDER BY COUNT(community_area_number) DESC
    LIMIT 1
)
LIMIT 1;
