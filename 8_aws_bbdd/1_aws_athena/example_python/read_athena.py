


from pyathena import connect
import pandas as pd

conn = connect(s3_staging_dir='s3://atheneastaging', region_name='eu-west-3')
df = pd.read_sql('SELECT * FROM "test_db"."marke_data" limit 100', conn)
print(df)


