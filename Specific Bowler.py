import pandas
import warnings
warnings.filterwarnings('ignore')
data = pandas.read_csv(r'C:\Cricket Adda\T20 Data\All T20 Data\ntb_all_matches.csv')
df = pandas.DataFrame(data, columns = ['bowler', 'ball', 'runs_off_bat', 'wicket_type', 'wides', 'noballs', 'match_id', 'innings', 'extras', 'legbyes', 'byes', 'season', 'venue'])
#df = df[(df['match_id']>=1250000) & (df['match_id']<=1300000)]
i = input("Enter the Bowler's Name: ")
df1 = (df[(df['bowler']==i) & (df['ball'] > 6) & (df['ball'] < 15) & (df['innings'] < 3)])
index = df1.index
rows = len(index)
df2 = df1[(df1['wicket_type']=='caught') | (df['wicket_type'] == 'bowled') | (df1['wicket_type']=='lbw') | (df['wicket_type'] == 'caught and bowled') | (df['wicket_type'] == 'stumped') | (df['wicket_type'] == 'hit wicket')]
index = df2.index
wickets = len(index)
runs1 = df1['runs_off_bat'].sum() 
runs2 = df1['wides'].sum()
runs3 = df1['noballs'].sum()
runs = (runs1) + (runs2) + (runs3)
noofwides = df1[df1['wides']> 0]
index = noofwides.index
finalwides = len(index)
finalrows = rows - finalwides - runs3
average = runs/wickets
strikerate = finalrows/wickets
economy = (runs/finalrows)*6
name = df1['bowler'].iloc[1]
print("Bowler: ", name)
print("Runs: ", runs)
print("Wickets: ", wickets)
print("Overs: ", int(finalrows/6)+(finalrows%6)/10)
print("Average", round(average,2))
print("Economy", round(economy,2))
print("Strike-rate", round(strikerate,2))



 