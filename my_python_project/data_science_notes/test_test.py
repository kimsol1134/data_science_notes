import numpy as np

pd.read_excel('data/seoul_park.csv')

df['요일'] = df['요일'].map(week)

df['날씨'] = df['날씨'].apply(weather)

df.groupby(['컬럼1','컬럼2'])['컬럼3'].mean()

df.loc[(df['어른']>1000| df['어린이']>1000), ['날짜', '공휴일','어른']]

df.sort_values("컬럼이름", ascending = True)

pd.merge(df1, df2, on =  '컬럼이름', how = 'inner')


sns.heatmap(df_corr)

df_corr = df.corr(numeric=True)