import pandas
import warnings
warnings.filterwarnings('ignore')
pandas.set_option("display.max_rows", None, "display.max_columns", None)
pandas.set_option('display.width', 1000)
data = pandas.read_csv(r'C:\Cricket Adda\T20 Data\All T20 Data\ipl_all_matches.csv')
df = pandas.DataFrame(data, columns = ['bowler', 'ball', 'runs_off_bat', 'wicket_type', 'wides', 'noballs', 'match_id', 'innings', 'bowling_team'])
df = df[df['match_id']>=1100000]
pp_result = pandas.DataFrame(columns = ['Bowler', 'Wickets', 'Runs', 'Overs', 'Average', 'Economy', 'Strike-rate'])
for i in df['bowler'].unique():
    df1 = (df[(df['bowler']== i) & (df['ball'] > 15) & (df['ball'] < 21) & (df['innings'] < 3)])
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
    if finalrows>0 :
        economy = (runs/finalrows)*6
        strikerate = finalrows/wickets
    if finalrows/6>15 :
        df3 = pandas.DataFrame({"Bowler":[i], "Wickets":[wickets], "Runs":[runs], "Overs":[int(finalrows/6)+(finalrows%6)/10], "Average":[average], "Economy":[economy], "Strike-rate":[strikerate]})
        pp_result = pp_result.append(df3)
pp_result.sort_values(by=['Economy'], inplace=True, ascending=True)
final = pp_result.round(decimals=2)
print(final)
#final.to_excel(r'C:\Cricket Adda\T20 Data\PP Bowlers\IPL PP Bowlers.xlsx', index = False)


