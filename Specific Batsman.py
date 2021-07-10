import pandas
import warnings
warnings.filterwarnings('ignore')
data = pandas.read_csv(r'C:\Cricket Adda\T20 Data\All T20 Data\ipl_all_matches.csv')
df = pandas.DataFrame(data, columns = ['striker', 'ball', 'runs_off_bat', 'player_dismissed', 'match_id', 'innings', 'non_striker', 'other_player_dismissed', 'wides', 'extras', 'bowling_team'])
df = df[(df['match_id']>=1200000) & (df['match_id']<=1350000)]
i = 'S Dhawan'
df1 = (df[((df['striker']== i) | (df['non_striker']== i))  & (df['ball'] < 21) & (df['ball'] < 21) & (df['innings'] < 3)])
df2 = df1[(df1['player_dismissed']== i) | (df['other_player_dismissed'] == i)]
index = df2.index
outs = len(index)
df3 = (df[(df['striker']== i) & (df['ball'] < 21) & (df['ball'] < 21) & (df['innings'] < 3)])
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
strikerate = (runs/finalballs)*100
dbp = (dotballs/finalballs)*100
bp6 = (finalballs/sixes)
bp4 = (finalballs/fours)
bpb = (finalballs/(fours+sixes))
rpo = (runs/finalballs)*6
print("Batsman: ", i)
print("Runs: ", runs)
print("Balls: ", finalballs)
print("Fours: ", fours)
print("Sixes: ", sixes)
print("Average: ", round(average,2))
print("Strike-rate: ", round(strikerate,2))
print("DBP: ", round(dbp,2),"%")
print("BP6: ", round(bp6,2))
print("BP4: ", round(bp4,2))
print("BPB: ", round(bpb,2))
print("RPO: ", round(rpo,2))




