import pandas as pd
import warnings
warnings.filterwarnings('ignore')
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', 1000)
data = pd.read_csv(r'C:\Cricket Adda\T20 Data\All T20 Data\ipl_all_matches.csv')
df = pd.DataFrame(data, columns = ['bowler', 'ball', 'runs_off_bat', 'wicket_type', 'wides', 'noballs', 'match_id', 'innings', 'extras', 'legbyes', 'byes', 'striker'])
result = pd.DataFrame(columns = ['Bowler','Runs', 'Balls','Outs', 'Average', 'Strike-rate'])
df = df[df['match_id']>=110000]
batsman_name = "KL Rahul"
df1 = (df[(df['striker']==batsman_name)])
for i in df1['bowler'].unique():
    df2 = (df1[(df1['bowler']== i)])
    index = df2.index
    rows = len(index)
    df3 = df2[(df2['wicket_type']=='caught') | (df2['wicket_type'] == 'bowled') | (df2['wicket_type']=='lbw') | (df2['wicket_type'] == 'caught and bowled') | (df2['wicket_type'] == 'stumped') | (df2['wicket_type'] == 'hit wicket')]
    index = df3.index
    wickets = len(index)
    runs = df2['runs_off_bat'].sum()
    runs3 = df2['noballs'].sum() 
    noofwides = df2[df2['wides']> 0]
    index = noofwides.index
    finalwides = len(index)
    finalrows = rows - finalwides
    average = runs/wickets
    strikerate = (runs/finalrows)*100
    economy = (runs/finalrows)*6
    df4 = pd.DataFrame({"Bowler":[i], "Runs":[runs], "Balls":[finalrows], "Outs":[wickets], "Average":[average], "Strike-rate":[strikerate]})
    result = result.append(df4)
result.sort_values(by=['Outs'], inplace=True, ascending=False)
final = result.round(decimals=2)
print("Batsman: ", batsman_name, "vs All Bowlers")
print(final)


