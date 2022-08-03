import pandas as pd

df1 = pd.read_csv("C:\\Users\\n.titov\\Desktop\\grids-20220729T130712Z-001\\grids\\22_2_f.dat", header=None, sep=' ', names = ['CDP_X', 'Depth', 'Vs'])
df1['CDP_X'] = df1['CDP_X'].apply(lambda x: round(x))

df2 = pd.read_csv("C:\\Users\\n.titov\\Desktop\\grids-20220729T130712Z-001\\grids\\22_midpnt_dataset", header=0, sep = '0 ', engine='python', names = ['CDP_X', 'CDP_Y'])
df2['CDP_X'] = df2['CDP_X'].apply(lambda x: round(x))
df2['CDP_Y'] = df2['CDP_Y'].apply(lambda x: round(x))

df_out = pd.merge(left = df1, right = df2, how = 'inner', on = 'CDP_X')
df_out = df_out[['CDP_X', 'CDP_Y', 'Depth', 'Vs']]
df_out.to_csv("C:\\Users\\n.titov\\Desktop\\grids-20220729T130712Z-001\\grids\\22_2_f_out.csv", sep = ' ', index = None)

# print(df1.head())
# print(df2.head())
# print(df_out.head())
# print(df_out.tail())

