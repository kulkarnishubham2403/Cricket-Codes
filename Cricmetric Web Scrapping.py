from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import date
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', 1000)
player_name = 'Virat Kohli'
player_role = 'batsman' # 'batsman' or 'bowler' or 'all'
format = 'TWENTY20' # 'Test' or 'ODI' or 'T20I' or 'TWENTY20' or 'T10' or 'all'
grouping = 'opp_player_type' #overs or opp_player_type or opp_player opp_team or inning or year or venue or batpos
start_date = '2018-01-01'
end_date = date.today()
start_over = 0
end_over = 21
headings = []
column1 = []
column2 = []
column3 = []
column4 = []
column5 = []
column6 = []
column7 = []
column8 = []
column9 = []
column10 = []
column11 = []
URL = (f'http://www.cricmetric.com/playerstats.py?player={player_name}&role={player_role}&format={format}&groupby={grouping}&start_date={start_date}&end_date={end_date}&start_over={start_over}&end_over={end_over}')
#URL = 'http://www.cricmetric.com/playerstats.py?player=B+Kumar&role=bowler&format=TWENTY20&groupby=opp_player_type&start_date=2018-01-01&end_date=2021-05-15&start_over=0&end_over=9999'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'lxml')
info = soup.find('table')
#print(info)
column = info.find_all('tbody')
#print(column)
info1 = info.find_all('tr')
info2 = info.find_all('th')
info3 = info.find_all('td')
k = len(info2)
for i in range (0,len(info2)):
    #print(info2[i].text)
    headings.append(info2[i].text)
for i in range (0,len(info2)):
    #print(info3[i].text)
    column1.append(info3[i].text)
for i in range (k,2*k):
    #print(info3[i].text)
    column2.append(info3[i].text)
for i in range (2*k,3*k):
    #print(info3[i].text)
    column3.append(info3[i].text)
final_df = pd.DataFrame(column1).T
final_df.columns = headings
final_df.loc[len(final_df.index)] = column2
final_df.loc[len(final_df.index)] = column3
if len(info3) > 3*k:
    for i in range (3*k,4*k):
        column4.append(info3[i].text)
    final_df.loc[len(final_df.index)] = column4
if len(info3) > 4*k:
    for i in range (4*k,5*k):
        column5.append(info3[i].text)
    final_df.loc[len(final_df.index)] = column5
if len(info3) > 5*k:
    for i in range (5*k,6*k):
        column6.append(info3[i].text)
    final_df.loc[len(final_df.index)] = column6
if len(info3) > 6*k:
    for i in range (6*k,7*k):
        column7.append(info3[i].text)
    final_df.loc[len(final_df.index)] = column7
if len(info3) > 7*k:
    for i in range (7*k,8*k):
        column8.append(info3[i].text)
    final_df.loc[len(final_df.index)] = column8
if len(info3) > 8*k:
    for i in range (8*k,9*k):
        column9.append(info3[i].text)
    final_df.loc[len(final_df.index)] = column9
if len(info3) > 9*k:
    for i in range (9*k,10*k):
        column10.append(info3[i].text)
    final_df.loc[len(final_df.index)] = column10
if len(info3) > 10*k:
    for i in range (10*k,11*k):
        column11.append(info3[i].text)
    final_df.loc[len(final_df.index)] = column11
print(player_role.capitalize(), "Name:",player_name)
print(final_df)
#final_df.to_excel(r'C:\Cricket Adda\T20 Data\Scorecards\Ravi Bishnoi Bowling.xlsx', index = False)




