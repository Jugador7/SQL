#Load the `pandas` and `sqlite3` libraries and establish a connection to `FinalDB.db`

%load_ext sql

import pandas, csv, sqlite3

con = sqlite3.connect("FinalDB.db")
cur = con.cursor()

#Load the SQL magic module

%sql sqlite:///FinalDB.db

##### Find the total number of crimes recorded in the CRIME table.

%sql SELECT COUNT(*) FROM CHICAGO_CRIME_DATA;

##### List community area names and numbers with per capita income less than 11000.

%sql SELECT community_area_name, community_area_number FROM CHICAGO_CENSUS_DATA WHERE per_capita_income < 11000;

##### List all case numbers for crimes involving minors?(children are not considered minors for the purposes of crime analysis) 

%sql SELECT case_number FROM CHICAGO_CRIME_DATA WHERE description LIKE "%minor%";

##### List all kidnapping crimes involving a child?

%sql SELECT * FROM CHICAGO_CRIME_DATA WHERE primary_type = "KIDNAPPING" and description LIKE "%child%";

##### List the kind of crimes that were recorded at schools. (No repetitions)

%sql SELECT distinct primary_type FROM CHICAGO_CRIME_DATA WHERE location_description like "%SCHOOL%";

##### List the type of schools along with the average safety score for each type.

%sql SELECT "Elementary, Middle, or High School", AVG(safety_score) FROM CHICAGO_PUBLIC_SCHOOLS GROUP BY "Elementary, Middle, or High School"

##### List 5 community areas with highest % of households below poverty line

%sql SELECT community_area_name, PERCENT_HOUSEHOLDS_BELOW_POVERTY FROM CHICAGO_CENSUS_DATA ORDER BY PERCENT_HOUSEHOLDS_BELOW_POVERTY DESC limit 5;

##### Which community area is most crime prone? Display the coumminty area number only.

%sql SELECT community_area_number, count(*) as "Crime number" FROM CHICAGO_CRIME_DATA GROUP BY community_area_number order by "Crime number" desc limit 1;

##### Use a sub-query to find the name of the community area with highest hardship index

%sql SELECT community_area_name FROM CHICAGO_CENSUS_DATA where hardship_index = ( select max(hardship_index) from CHICAGO_CENSUS_DATA);

##### Use a sub-query to determine the Community Area Name with most number of crimes?

%sql SELECT community_area_number FROM (SELECT community_area_number, count(*) as "Crime number" FROM CHICAGO_CRIME_DATA GROUP BY community_area_number order by "Crime number" desc limit 1)


