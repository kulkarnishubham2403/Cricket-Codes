import pandas
import warnings
warnings.filterwarnings('ignore')
pandas.set_option("display.max_rows", None, "display.max_columns", None)
pandas.set_option('display.width', 1000)
data = pandas.read_csv(r'C:\Cricket Adda\T20 Data\All T20 Data\cpl_all_matches.csv')
df = pandas.DataFrame(data, columns = ['striker', 'ball', 'runs_off_bat', 'player_dismissed', 'match_id', 'innings', 'non_striker', 'other_player_dismissed', 'wides', 'extras', 'bowling_team'])
df = df[(df['match_id']>=1100000) & (df['match_id']<=1300000)]
pp_result = pandas.DataFrame(columns = ['Batsman', 'Runs', 'Balls', 'Average', 'Strike-rate', 'DBP', 'BP6', 'BP4', 'RPO', 'BPD', 'PIB'])
for i in df['striker'].unique():
    df1 = (df[((df['striker']== i) | (df['non_striker']== i))  & (df['ball'] > 0) & (df['ball'] < 6)  & (df['innings'] < 3)])
    df2 = df1[(df1['player_dismissed']== i) | (df['other_player_dismissed'] == i)]
    index = df2.index
    outs = len(index)
    df3 = (df[(df['striker']== i) & (df['ball'] > 0) & (df['ball'] < 6)  & (df['innings'] < 3)])
    runs = df3['runs_off_bat'].sum() 
    index = df3.index
    balls = len(index)
    noofwides = df3[df3['wides']>0]
    index = noofwides.index
    finalwides = len(index)
    finalballs = balls - finalwides
    extra = df3[df3['extras']>0]
    index = extra.index
    finalextras = len(index)
    dots = df3[df3['runs_off_bat'] == 0]
    index = dots.index
    dotballs = len(index) - finalwides
    six = df3[df3['runs_off_bat'] == 6]
    index = six.index
    sixes = len(index)
    four = df3[df3['runs_off_bat'] == 4]
    index = four.index
    fours = len(index)
    average = runs/outs
    pib = ((fours*4 + sixes*6)/runs)*100
    if outs == 0:
        bpd = 0
    else:
        bpd = finalballs/outs
    if finalballs>0 :
        strikerate = (runs/finalballs)*100
        dbp = (dotballs/finalballs)*100
        rr = (runs/finalballs)*6
    if sixes>0 :
        bp6 = (finalballs/sixes)
    if fours>0 :
        bp4 = (finalballs/fours)
    if runs>50 :
        df4 = pandas.DataFrame({"Batsman":[i], "Runs":[runs], "Balls":[finalballs], "Average":[average], "Strike-rate":[strikerate], "DBP":[dbp], "BP6":[bp6], "BP4":[bp4], "RPO":[rr], "BPD":[bpd], "PIB":[pib]})
        pp_result = pp_result.append(df4)
pp_result.sort_values(by=['Strike-rate'], inplace=True, ascending=False)
final = pp_result.round(decimals=2)
print(final)
#final.to_excel(r'C:\Cricket Adda\T20 Data\PP Bowlers\IPL PP Batsmen.xlsx', index = False)



