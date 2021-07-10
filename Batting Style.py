import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', 1000)
data = pd.read_csv(r'C:\Cricket Adda\T20 Data\Scorecards\IPL Batsmen.csv')
df = pd.DataFrame(data, columns = ['Batsmen'])
player = df.Batsmen[0]
n = player[0]
m = 1
s = 0
lookingfor = " "
cricinfo_search_generic_url='https://search.espncricinfo.com/ci/content/site/search.html?search={};type=player'
def get_player_profile(player):
    ##Collect the results in a dataframe
    player_df=pd.DataFrame()
        
    '''Function to get the player profile details from ESPN Cricinfo'''
    ##Modify the search page by adding the player parameter
    cricinfo_search_url=cricinfo_search_generic_url.format(player)
    ##Get the contents of the search page
    search_page=requests.get(cricinfo_search_url)
    ##Process the contents of the search page
    search_soup=soup(search_page.text,'html.parser')
    ##Get the list of player URLs
    player_list=[a['href'] for a in search_soup.find_all('a') if 'content/player' in a['href']]
    ##Process the list to get exact player profile URLs
    player_list=['https://search.espncricinfo.com/'+str(p) for p in player_list if 'https' not in p]
        
    ##If the requests have not been successful
    if len(player_list)==0:
        player_df=pd.DataFrame({'player':[player],'exception':['Parsing error in URL']})
        print(" No Value")
    else:
        for p in player_list:
            ##Iterate through each of the possible player links in the page
            player_request=requests.get(p)
            ##Get the soup of the profile page
            profile_soup=soup(player_request.text,'html.parser')
            ##Locate the elements needed for the player data collection, which are under the "P" class 
            
            headers=[p.text for p in profile_soup.find_all('p',{'class':'text-uppercase gray-700 mb-0 pb-0-5 player-card-heading'})]
            
            ##Locate the elements needed for the player data attributes, which are under H5 headers
            
            values=[p.text for p in profile_soup.find_all('h5',{'class':'player-card-description gray-900'})]
            
            pdf=pd.DataFrame(values).T
            
            pdf.columns=headers
            
            player_df=pd.concat([player_df,pdf])
            strings = player_df['Full Name']
            strings1 = player_df['Batting Style']
            arr1 = strings1.to_numpy()
            arr = strings.to_numpy()
            if m==1:
                print( player)
                #print((player_df['Batting Style']).to_string(index=False))
                print(arr1[0])

    return arr
    #return player_df


for i in range (0,50):
    player = df.Batsmen[i]
    n = player[0]
    m = 1
    s = 0
    lookingfor = " "
    if player[1] == lookingfor:
        m=0
        playername = player[2:30] + "," + " " + player[0]
        player_name = player[2:30]
        player = player_name
    #print(player)
    #print(m)
    temp = (get_player_profile(player))
    #print(temp)
    if m==0:
        for i in range (0,len(temp)):
            if temp[i][0]==n:
                player = temp[i]
                #print(player)
                for k in range (0,len(player)):
                    if player[k]==lookingfor:
                        s=s+1
                        r=k
                for k in range (0,len(player)):
                    if player[k]==lookingfor:
                        t=k
                        break
                if s==2:
                    player = player[0:t] + player[r:len(player)] 
                    #print(player)
                m=1
                get_player_profile(player)


