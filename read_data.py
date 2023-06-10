import pandas as pd
import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-F726TKR;"
    "Database=works;"
    )

sql_query = "SELECT * FROM batter"
df = pd.read_sql(sql_query, conn)

print(df)

