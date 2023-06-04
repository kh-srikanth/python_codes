import socket

import pypyodbc as odbc
import pyodbc
import json
import pandas as pd
import sqlalchemy

cook = """{
	"id": "0001",
	"type": "donut",
	"name": "Cake",
	"ppu": 0.55,
	"batters":
		{
			"batter":
				[
					{ "id": "1001", "type": "Regular" },
					{ "id": "1002", "type": "Chocolate" },
					{ "id": "1003", "type": "Blueberry" },
					{ "id": "1004", "type": "Devil's Food" }
				]
		},
	"topping":
		[
			{ "id": "5001", "type": "None" },
			{ "id": "5002", "type": "Glazed" },
			{ "id": "5005", "type": "Sugar" },
			{ "id": "5007", "type": "Powdered Sugar" },
			{ "id": "5006", "type": "Chocolate with Sprinkles" },
			{ "id": "5003", "type": "Chocolate" },
			{ "id": "5004", "type": "Maple" }
		]
}"""
cooking = json.loads(cook)
batters = cooking["batters"]
batter = batters["batter"]
#print(batter)
batter_data = pd.json_normalize(batter)
#print(batter_data)
topping = cooking["topping"]
#print(topping)
topping_data = pd.json_normalize(topping)
#print(topping_data)
connection_string = f"""
DRIVER={{{'SQL SERVER'}}};
SERVER={'DESKTOP-F726TKR'};
DATA_BASE={'works'};
trusted_connection=yes;
"""
conn = odbc.connect(connection_string)
#print(pyodbc.drivers())
conn1 = sqlalchemy.create_engine(f'mssql+pyodbc://{socket.gethostname()}/batter?trusted_connection=yes&driver=ODBC Driver 17 for SQL Server')
print(conn1)
table = 'batter'
df=pd.DataFrame(batter_data)
print(df)
#df.to_sql(table,con=conn1,if_exists='append',index=False)

# insert_query = """
# use works;
# insert into dbo.batter (id,type)
# select ?,?
# """
# cursor = conn.cursor()
# cursor.executemany(insert_query,df)
# conn.commit()
# cursor.close()
# conn.close()
