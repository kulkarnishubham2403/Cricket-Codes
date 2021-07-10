import pandas as pd
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', 1000)
runs = 0 
balls = 0
finalwides = 0
finalballs = 0
finalextras = 0
sixes = 0
fours = 0
dotballs = 0
finalextras = 0
data = pd.read_csv(r'C:\Cricket Adda\T20 Data\All T20 Data\ipl_all_matches.csv')
df = pd.DataFrame(data, columns = ['striker', 'ball', 'runs_off_bat', 'player_dismissed', 'match_id', 'innings', 'non_striker', 'other_player_dismissed', 'wides', 'extras', 'bowling_team'])
df = df[(df['match_id']>=1250000) & (df['match_id']<=1300000)]
result = pd.DataFrame(columns = ['Batsman', 'Runs', 'Balls','SR', 'DBP', 'BPB'])
for k in df['striker'].unique():
    runs = 0 
    balls = 0
    finalwides = 0
    finalballs = 0
    finalextras = 0
    sixes = 0
    fours = 0
    dotballs = 0
    finalextras = 0
    df1 = (df[((df['striker']== k)  & (df['innings'] < 3))])
    df2 = df1['match_id'].unique()
    for i in range (0,len(df2)):
            df3 = df1[(df1['match_id']==df2[i])]
            index = df3.index
            df3['balls_faced'] = df3.reset_index().index + 1
            df4 = df3[(df3['balls_faced'] < 11) & (df3['balls_faced'] < 11)]
            runs = runs + df4['runs_off_bat'].sum() 
            index = df4.index
            balls = balls + len(index)
            noofwides = df4[df4['wides']>0]
            index = noofwides.index
            finalwides = finalwides + len(index)
            finalballs = balls - finalwides
            extra = df4[df4['extras']>0]
            index = extra.index
            finalextras = finalextras + len(index)
            dots = df4[df4['runs_off_bat'] == 0]
            index = dots.index
            dotballs = dotballs + len(index)
            six = df4[df4['runs_off_bat'] == 6]
            index = six.index
            sixes = sixes + len(index)
            four = df4[df4['runs_off_bat'] == 4]
            index = four.index
            fours = fours + len(index)
    dotballs = dotballs - finalwides
    strikerate = (runs/finalballs)*100
    if finalballs == 0:
        dbp = 0
    else:
        dbp = (dotballs/finalballs)*100
    if sixes == 0:
        bp6 = 0
    else:
        bp6 = (finalballs/sixes)
    if fours == 0:
        bp4=0
    else:
        bp4 = (finalballs/fours)
    if fours+sixes == 0:
        bpb = 0
    else:
        bpb = (finalballs/(fours+sixes))
    if (strikerate>80) & (runs>50) :
        df5 = pd.DataFrame({"Batsman":[k], "Runs":[runs], "Balls":[finalballs], "SR":[strikerate], "DBP":[dbp], "BPB":[bpb]})
        result = result.append(df5)
result.sort_values(by=['SR'], inplace=True, ascending=False)
final = result.round(decimals=2)
print(final)
#plt.scatter(final.SR, final.BPB)
#final.to_excel(r'C:\Cricket Adda\T20 Data\PP Bowlers\IPL PP Batsmen.xlsx', index = False)
