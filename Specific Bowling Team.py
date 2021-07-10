import pandas
import warnings
warnings.filterwarnings('ignore')
data = pandas.read_csv(r'C:\Cricket Adda\T20 Data\All T20 Data\ipl_all_matches.csv')
df = pandas.DataFrame(data, columns = ['bowler', 'ball', 'runs_off_bat', 'wicket_type', 'wides', 'noballs', 'match_id', 'innings', 'extras', 'legbyes', 'byes', 'bowling_team'])
df = df[df['match_id']>=1200000]
df1 = (df[(df['bowling_team']=='Rajasthan Royals') & (df['ball'] > 15) & (df['ball'] > 15) & (df['innings'] < 3)])
index = df1.index
rows = len(index)
df2 = df1[(df1['wicket_type']=='caught') | (df['wicket_type'] == 'bowled') | (df1['wicket_type']=='lbw') | (df['wicket_type'] == 'caught and bowled') | (df['wicket_type'] == 'stumped') | (df['wicket_type'] == 'hit wicket') | (df['wicket_type'] == 'run out')]
index = df2.index
wickets = len(index)
runs1 = df1['runs_off_bat'].sum() 
runs2 = df1['extras'].sum()
runs = (runs1) + (runs2) 
noofwides = df1[df1['wides']> 0]
index = noofwides.index
finalwides = len(index)
noofnoballs = df1[df1['noballs'] > 0]
index = noofnoballs.index
finalnoballs = len(index)
finalrows = rows - finalwides - finalnoballs
average = runs/wickets
strikerate = finalrows/wickets
economy = (runs/finalrows)*6
name = df1['bowling_team'].iloc[1]
print("Team: ", name)
print("Runs: ", runs)
print("Wickets: ", wickets)
print("Overs: ", int(finalrows/6)+(finalrows%6)/10)
print("Average", round(average,2))
print("Economy", round(economy,2))
print("Strike-rate", round(strikerate,2))

