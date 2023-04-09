import pandas as pd
import numpy as np

d={'fst_name': ['Jane','Jaslean','Deena','Vallery','Bonnell','Darisha','Corneisha','Isabellia','Giannamarie','Wilna','Brucie','Zaidah','Jamiemarie','Ponda', 'John'], 
   'fast_name': ['Doe', 'Yathziri', 'Chandara', 'Terrisa', 'Oluwateniola', 'Eztli', 'Shailin', 'Jazel', 'Oluwadunmininu', 'Tiwana', 'Garnett', 'Surenity', 'Honor', 'Midge', 'Doe'], 
   'avg_score': np.array([11,8,3,9,11,8,1,5,10,3,12,3,11,3,5]), 
   'curr_exam_grade': np.array([9,8,5,8,12,3,11,7,10,9,1,4,2,12,3]), 
   'num_attempts': np.array([1,4,4,4,1,3,4,5,1,2,1,2,1,3,2])}

df = pd.DataFrame(d)

#df=df.drop(columns='admis_nxt_semest')
df.insert(5, 'admis_nxt_semest',np.array([1,1,1,1,0,1,1,1,1,0,0,1,1,1,1]))
print(df.describe())

print('avg_score min: ', df['avg_score'].min())
print('avg_score max: ', df['avg_score'].max())
print('avg_score mean: ', df['avg_score'].mean())
print('avg_score median: ', df['avg_score'].median())

rslt_df = df[df['num_attempts']==1]
print(rslt_df)

df['fast_name']
print(type(df['fast_name']))