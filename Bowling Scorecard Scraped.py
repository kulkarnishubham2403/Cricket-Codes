import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', 1000)
def extract_bowling_data(series_id, match_id):

    URL = 'https://www.espncricinfo.com/series/'+ str(series_id) + '/scorecard/' + str(match_id)
    page = requests.get(URL)
    bs = BeautifulSoup(page.content, 'lxml')

    table_body=bs.find_all('tbody')
    bowler_df = pd.DataFrame(columns=['Name', 'Overs', 'Maidens', 'Runs', 'Wickets',
                                      'Econ', 'Dots', '4s', '6s', 'Wd', 'Nb','Team'])
    for i, table in enumerate(table_body[1:4:2]):
        rows = table.find_all('tr')
        for row in rows:
            cols=row.find_all('td')
            cols=[x.text.strip() for x in cols]
            bowler_df = bowler_df.append(pd.Series([cols[0], cols[1], cols[2], cols[3], cols[4], cols[5], 
                                                    cols[6], cols[7], cols[8], cols[9], cols[10], (i==0)+1], 
                                                   index=bowler_df.columns ), ignore_index=True)
    return bowler_df

temp = extract_bowling_data(series_id = 8048, match_id = 1254082)
print(temp)
#temp.to_excel(r'C:\Cricket Adda\T20 Data\Scorecards\IPL 2021 Match 8 Bowling.xlsx', index = False)
