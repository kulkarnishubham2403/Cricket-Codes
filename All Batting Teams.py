import pandas
import warnings
warnings.filterwarnings('ignore')
pandas.set_option("display.max_rows", None, "display.max_columns", None)
pandas.set_option('display.width', 1000)
data = pandas.read_csv(r'C:\Cricket Adda\T20 Data\All T20 Data\bbl_all_matches.csv')
df = pandas.DataFrame(data, columns = ['striker', 'wicket_type', 'ball', 'runs_off_bat', 'noballs', 'match_id', 'innings', 'other_player_dismissed', 'wides', 'extras', 'batting_team', 'venue'])
df = df[(df['match_id']>=1150000) & (df['match_id']<=1300000)]  
pp_result = pandas.DataFrame(columns = ['Team', 'Wickets', 'Runs', 'Overs', 'Average', 'RPO', 'Strike-rate','Fours','Sixes','DotBalls', 'DBP', 'BP6', 'BP4'])
for i in df['batting_team'].unique():
    df1 = (df[(df['batting_team']== i ) & (df['ball'] > 0) & (df['ball'] < 6) & (df['innings'] < 3)])
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
    extra = df1[df1['extras']>0]
    index = extra.index
    finalextras = len(index)
    dots = df1[df1['runs_off_bat'] == 0]
    index = dots.index
    dotballs = len(index) - finalextras
    six = df1[df1['runs_off_bat'] == 6]
    index = six.index
    sixes = len(index)
    four = df1[df1['runs_off_bat'] == 4]
    index = four.index
    fours = len(index)
    if wickets>0 :
        average = runs/wickets
    if finalrows>0 :
        rpo = (runs/finalrows)*6
        strikerate = (runs / finalrows)*100
        dbp = (dotballs/finalrows)*100
    if sixes>0 :    
        bp6 = (finalrows/sixes)
    else:
        bp6 = 0
    if fours>0 :
        bp4 = (finalrows/fours)
    if finalrows/6>0 :
        df3 = pandas.DataFrame({"Team":[i], "Wickets":[wickets], "Runs":[runs], "Overs":[int(finalrows/6)+(finalrows%6)/10], "Average":[average], "RPO":[rpo], "Strike-rate":[strikerate], "Fours":[fours],"Sixes":[sixes],"DotBalls":[dotballs], "DBP":[dbp], "BP6":[bp6], "BP4":[bp4]})
        pp_result = pp_result.append(df3)   
pp_result.sort_values(by=['Average'], inplace=True, ascending=False)
final = pp_result.round(decimals=2)
print(final)
final.to_excel(r'C:\Cricket Adda\T20 Data\BBL PP Teams.xlsx', index = False)

