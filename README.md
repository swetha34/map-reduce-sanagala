# Map-Reduce-Gahana Swetha
- For lagre python datasets using the map-reduce 
# Data Description:
- I used data from kaggle website (https://www.kaggle.com/prasertk/qs-world-university-rankings-2021) Based on World Universities and raniking
- Data I have taken is Universities and the ranking by country,city,region and year.Attending top universities and colleges can help you build influential networks that open doors after graduation.So I reduce all the universities based on the scores or ranking from 133 records.After I have taken the top 10 universities and ploted the chart accordingly.
# Powershell Command:
- cat QS_World_University_Rankings_2022.csv | py 21mapper.py | sort |py 22reducer.py > swetha.txt 
# Summary Of Data
- By checking the final ouput I have reduced the Univerisites based on the scores and showed in Pareto chart plots the distributions of data in descending order of frequency with a cumulative line on a secoundary axis as a percentage of the total.

![Chart Plot](/image/Chart.PNG)
