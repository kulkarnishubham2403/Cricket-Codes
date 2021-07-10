import pandas as pd
import warnings
warnings.filterwarnings('ignore')
data = pd.read_csv(r'C:\Cricket Adda\T20 Data\Test Data in CSV\all_tests.csv')
df = pd.DataFrame(data, columns = ['bowler', 'ball', 'runs_off_bat', 'wicket_type', 'wides', 'noballs', 'match_id', 'innings', 'extras', 'legbyes', 'byes', 'striker'])
result = pd.DataFrame(columns = ['Runs', 'Balls','Outs', 'Average', 'Strike-rate'])
df = df[df['match_id']>=0]
bowler_name = "N Wagner"
batsman_name = "AM Rahane"
df1 = (df[(df['bowler']==bowler_name) & (df['striker']==batsman_name)])
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
finalrows = rows - finalwides
average = runs/wickets
strikerate = (runs/finalrows)*100
economy = (runs/finalrows)*6
print(batsman_name , "vs ", bowler_name)
df3 = pd.DataFrame({"Runs":[runs], "Balls":[finalrows], "Outs":[wickets], "Average":[average], "Strike-rate":[strikerate]})
result = result.append(df3)
#print(result)
print("Runs: ", runs)
print("Outs: ", wickets)
print("Balls: ", finalrows)
print("Average: ", round(average,2))
print("Strike-rate: ", round(strikerate,2))
