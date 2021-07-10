import pandas
import warnings
warnings.filterwarnings('ignore')
data = pandas.read_csv(r'C:\Cricket Adda\T20 Data\All T20 Data\ipl_all_matches.csv')
df = pandas.DataFrame(data, columns = ['bowler', 'ball', 'runs_off_bat', 'wicket_type', 'wides', 'noballs', 'match_id', 'innings', 'extras', 'legbyes', 'byes', 'striker'])
df = df[df['match_id']>=300000]
df1 = (df[(df['bowler']=='A Flintoff') & (df['striker']=='AB de Villiers')])
index = df1.index
rows = len(index)
df2 = df1[(df1['wicket_type']=='caught') | (df['wicket_type'] == 'bowled') | (df1['wicket_type']=='lbw') | (df['wicket_type'] == 'caught and bowled') | (df['wicket_type'] == 'stumped') | (df['wicket_type'] == 'hit wicket')]
index = df2.index
wickets = len(index)
runs = df1['runs_off_bat'].sum()
runs3 = df1['noballs'].sum() 
noofwides = df1[df1['wides']> 0]
index = noofwides.index
finalwides = len(index)
finalrows = rows - finalwides - runs3
average = runs/wickets
strikerate = (runs/finalrows)*100
economy = (runs/finalrows)*6
name = df1['bowler'].iloc[1]
name2 = df1['striker'].iloc[1]
print(name , "vs ", name2)
print("Runs: ", runs)
print("Outs: ", wickets)
print("Overs: ", int(finalrows/6)+(finalrows%6)/10)
print("Average: ", round(average,2))
print("Economy: ", round(economy,2))
print("Strike-rate: ", round(strikerate,2))
