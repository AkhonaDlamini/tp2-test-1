#3.1 Write a program that will load the “football.csv” dataset into a dataframe called 
#“foot_ball”.   

import pandas as pd

data = pd.read_csv("C://Users//27789//Downloads//dataset - 2020-09-24.csv")

#3.2 inspect the dataframe by listing and displaying the last 7 rows of the dataframe using a 
#single python statement. 
print(data.tail(7))

"""3.3 Write python statements to: 
3.3.1 Access and display the "Nationality" and "Club" columns for the first all players.  (2) 
3.3.2 Access and display the data for the tenth player in the dataset using row index.        
(2) 
3.3.3 Access and display the "Goals" and "Appearances" for players with index positions 
100 to 110.            
(2) 
3.3.4 Add a new column named "Goals per Appearance" that is calculated by dividing 
"Goals" by "Appearances"; and display the first 5 rows of the updated dataset.   
(3) 
3.3.5 Select and display a subset of the dataframe containing only the players from "Arsenal" 
club.                                                                                                                                      
(2) 
3.3.6 Perform a filtering operation to display players who have scored more than 5.  
"""

print(data['Nationality'])
print(data['Club'])