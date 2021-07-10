import pandas as pd
import warnings
warnings.filterwarnings('ignore')
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', 1000)
phase = ['1-6', '7-11', '12-15', '16-20']
phase_runs = [0,0,0,0]
phase_balls = [0,0,0,0]
phase_sr = [0,0,0,0]
phase_outs = [0,0,0,0]
phase_avg = [0,0,0,0]
phase_fours = [0,0,0,0]
phase_sixes = [0,0,0,0]
phase_dots = [0,0,0,0]
phase_bp4 = [0,0,0,0]
phase_bp6 = [0,0,0,0]
phase_dbp = [0,0,0,0]
data = pd.read_csv(r'C:\Cricket Adda\T20 Data\All T20 Data\ipl_all_matches.csv')
df = pd.DataFrame(data, columns = ['bowler', 'ball', 'runs_off_bat', 'wicket_type', 'wides', 'noballs', 'match_id', 'innings', 'extras', 'legbyes', 'byes', 'striker', 'player_dismissed'])
result = pd.DataFrame(columns = ['Batsman','Phase', 'Runs', 'Balls','Average', 'SR', 'BP4', 'BP6', 'DBP'])
df = df[(df['match_id']>=1100000) & (df['match_id']<=1300000)]
k = 'V Kohli'
df1 = (df[((df['striker']== k)  & (df['innings'] < 3))])
df2 = df1['match_id'].unique()
for i in range (0,len(df2)):
    df3 = df[(df['match_id']==df2[i])]
    df8 = df3[(((df3['wicket_type']=='caught') | (df3['wicket_type'] == 'bowled') | (df3['wicket_type'] == 'run out') | (df3['wicket_type']=='lbw') | (df3['wicket_type'] == 'caught and bowled') | (df3['wicket_type'] == 'stumped') | (df3['wicket_type'] == 'hit wicket')) & (df3['player_dismissed'] == k))]
    index = df8.index
    outs = len(index)
    df4 = pd.DataFrame(df3, columns = ['striker', 'ball'])
    df5 = df4[(df4['striker']== k)] 
    balls_faced = df5['ball'].unique()
    entry_point = balls_faced[0]
    df6 = df3[(df3['striker']==k)]
    runs = df6['runs_off_bat'].sum()
    index = df6.index
    rows = len(index)
    runs3 = df6['noballs'].sum() 
    noofwides = df6[df6['wides']> 0]
    index = noofwides.index
    finalwides = len(index)
    finalrows = rows - finalwides - runs3
    strikerate = (runs/finalrows)*100
    fours_df = df6[df6['runs_off_bat'] == 4]
    index = fours_df.index
    fours = len(index)
    sixes_df = df6[df6['runs_off_bat']== 6]
    index = sixes_df.index
    sixes = len(index)
    dots_df = df6[df6['runs_off_bat'] == 0]
    index = dots_df.index
    dots = len(index) - finalwides
    if entry_point < 6:
        phase_runs[0] = phase_runs[0] + runs
        phase_balls[0] = phase_balls[0] + finalrows
        phase_outs[0] = phase_outs[0] + outs                
        phase_sr[0] = round((phase_runs[0]/phase_balls[0])*100,2)
        phase_avg[0] = round(phase_runs[0]/phase_outs[0],2)
        phase_fours[0] = phase_fours[0] + fours
        phase_sixes[0] = phase_sixes[0] + sixes
        phase_dots[0] = phase_dots[0] + dots
        phase_bp4[0] = round(phase_balls[0]/phase_fours[0],2)
        phase_bp6[0] = round(phase_balls[0]/phase_sixes[0],2)
        phase_dbp[0] = round(phase_dots[0]*100/phase_balls[0],2)
    elif entry_point > 6 and entry_point < 11:
        phase_runs[1] = phase_runs[1] + runs
        phase_balls[1] = phase_balls[1] + finalrows
        phase_outs[1] = phase_outs[1] + outs
        phase_sr[1] = round((phase_runs[1]/phase_balls[1])*100,2)
        phase_avg[1] = round(phase_runs[1]/phase_outs[1],2)
        phase_fours[1] = phase_fours[1] + fours
        phase_sixes[1] = phase_sixes[1] + sixes
        phase_dots[1] = phase_dots[1] + dots
        phase_bp4[1] = round(phase_balls[1]/phase_fours[1],2)
        phase_bp6[1] = round(phase_balls[1]/phase_sixes[1],2)
        phase_dbp[1] = round(phase_dots[1]*100/phase_balls[1],2)
    elif entry_point > 11 and entry_point < 15:
        phase_runs[2] = phase_runs[2] + runs
        phase_balls[2] = phase_balls[2] + finalrows
        phase_outs[2] = phase_outs[2] + outs
        phase_sr[2] = round((phase_runs[2]/phase_balls[2])*100,2)
        phase_avg[2] = round(phase_runs[2]/phase_outs[2],2)
        phase_fours[2] = phase_fours[2] + fours
        phase_sixes[2] = phase_sixes[2] + sixes
        phase_dots[2] = phase_dots[2] + dots
        phase_bp4[2] = round(phase_balls[2]/phase_fours[2],2)
        phase_bp6[2] = round(phase_balls[2]/phase_sixes[2],2)
        phase_dbp[2] = round(phase_dots[2]*100/phase_balls[2],2)
    else:
        phase_runs[3] = phase_runs[3] + runs
        phase_balls[3] = phase_balls[3] + finalrows
        phase_outs[3] = phase_outs[3] + outs
        phase_sr[3] = round((phase_runs[3]/phase_balls[3])*100,2)
        phase_avg[3] = round(phase_runs[3]/phase_outs[3],2)
        phase_fours[3] = phase_fours[3] + fours
        phase_sixes[3] = phase_sixes[3] + sixes
        phase_dots[3] = phase_dots[3] + dots
        phase_bp4[3] = round(phase_balls[3]/phase_fours[3],2)
        phase_bp6[3] = round(phase_balls[3]/phase_sixes[3],2)
        phase_dbp[3] = round(phase_dots[3]*100/phase_balls[3],2)
for i in range(0,4):
   df7 = pd.DataFrame({"Batsman":[k], "Phase":[phase[i]], "Runs":[phase_runs[i]], "Balls":[phase_balls[i]], "Average":[phase_avg[i]], "SR":[phase_sr[i]], "BP4":[phase_bp4[i]], "BP6":[phase_bp6[i]], "DBP":[phase_dbp[i]]})
   result = result.append(df7)
print(result)
    
    
    
