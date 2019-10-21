import pandas as pd
from sqlalchemy import create_engine

connection_string = "postgres://postgres:postgres@127.0.0.1:5432/suicide_rates_db"
engine = create_engine(connection_string)
engine.execute("TRUNCATE suicide_merge CASCADE")

suicide_info = pd.read_csv('../input/CleanMerge.csv')
suicide_info.to_sql("suicide_merge", engine, if_exists="append")
