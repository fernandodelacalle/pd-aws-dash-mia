import pandas as pd

df = pd.read_csv(
    'data/market_data.txt', 
    sep=';',
    usecols=['FECHA', 'VALOR', 'VOLUMEN', 'PRECIO', 'HORAEJEC']
)
print(df)

df.loc[:, 'TIME'] = pd.to_datetime(
    df.loc[:, 'FECHA'].map(str) + ' ' + df.loc[:, 'HORAEJEC']
)
df = df.drop(['FECHA', 'HORAEJEC'], axis=1)
df['VALOR'] = df['VALOR'].str.strip()
df = df.loc[df['VALOR'].isin(['SAN','TEF', 'IDX'])]
print(df)

#data = pd.read_csv(f's3://{bucket}/{key}')
#print(data)