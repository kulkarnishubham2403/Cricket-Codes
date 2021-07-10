import pandas
import warnings
warnings.filterwarnings('ignore')
data = pandas.read_csv(r'C:\Cricket Adda\T20 Data\All T20 Data\ipl_all_matches.csv')
df = pandas.DataFrame(data, columns = ['striker', 'wicket_type', 'ball', 'runs_off_bat', 'noballs', 'match_id', 'innings', 'other_player_dismissed', 'wides', 'extras', 'batting_team', 'venue'])
df = df[df['match_id'] >= 1250000]
i = 'Sunrisers Hyderabad'
df1 = (df[(df['batting_team']==i) & (df['ball'] > 15) & (df['ball'] > 15) & (df['innings'] < 3) & (df['venue']=='MA Chidambaram Stadium, Chepauk, Chennai')])
df2 = df1[(df1['wicket_type']=='caught') | (df['wicket_type'] == 'bowled') | (df1['wicket_type']=='lbw') | (df['wicket_type'] == 'caught and bowled') | (df['wicket_type'] == 'stumped') | (df['wicket_type'] == 'hit wicket') | (df['wicket_type'] == 'run out')]
index = df2.index
outs = len(index)
runs1 = df1['runs_off_bat'].sum() 
runs2 = df1['extras'].sum()
runs = (runs1) + (runs2) 
index = df1.index
balls = len(index)
noofwides = df1[df1['wides']>0]
index = noofwides.index
finalwides = len(index)
noball = df1[df1['noballs']>0]
index = noball.index
finalnoballs = len(index)
finalballs = balls - finalwides - finalnoballs
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
average = runs/outs
strikerate = (runs/finalballs)*100
dbp = (dotballs/finalballs)*100
bp6 = (finalballs/sixes)
bp4 = (finalballs/fours)
rpo = (runs/finalballs)*6
print("Team: ", i)
print("Runs: ", runs)
print("Overs: ", int(finalballs/6)+(finalballs%6)/10)
#print("Fours: ", fours)
#print("Sixes: ", sixes)
print("Wickets: ", outs)
print("Average: ", round(average,2))
print("Strike-rate: ", round(strikerate,2))
print("DBP: ", round(dbp,2),"%")
print("BP6: ", round(bp6,2))
print("BP4: ", round(bp4,2))
print("RPO: ", round(rpo,2))

