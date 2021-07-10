import pandas
import warnings
warnings.filterwarnings('ignore')
ground = "Perth Stadium"
pandas.set_option("display.max_rows", None, "display.max_columns", None)
pandas.set_option('display.width', 1000)
data = pandas.read_csv(r'C:\Cricket Adda\T20 Data\Test Data in CSV\all_tests.csv')
df = pandas.DataFrame(data, columns = ['match_id', 'season', 'venue', 'innings', 'batting_team', 'bowling_team', 'runs_off_bat', 'extras', 'wicket_type'])
df = df[(df['venue']==ground) & (df['match_id']>=0)]
avg_innings_runs = [None] * 5
avg_innings_wickets = [None] * 5
matches = []
for i in range(1,5):
    k = 0
    runs = 0
    wickets = 0
    runs1 = 0
    runs2 = 0
    index = 0
    matches = []
    df1 = (df[(df['innings']== i )])
    runs1 = df1['runs_off_bat'].sum() 
    runs2 = df1['extras'].sum()
    runs = (runs1) + (runs2)
    matches = df1['match_id'].unique()
    k = len(matches)
    avg_innings_runs[i] = ((runs / k).round(decimals=0))
    df2 = df1[(df1['wicket_type']=='caught') | (df['wicket_type'] == 'bowled') | (df1['wicket_type']=='lbw') | (df['wicket_type'] == 'caught and bowled') | (df['wicket_type'] == 'stumped') | (df['wicket_type'] == 'hit wicket') | (df['wicket_type'] == 'run out')]
    index = df2.index
    wickets = len(index)
    avg_innings_wickets[i] = (wickets / k)
print("Venue:", ground)
for i in range(1,5):
    print("Average Score for Innings", i,":", avg_innings_runs[i])
    #print("Wickets: ", round(avg_innings_wickets[i], 0))
