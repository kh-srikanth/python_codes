import socket

import pyodbc as odbc
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
connection_string = odbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-F726TKR;"
    "Database=works;"
    )
conn = connection_string
insert_query = """
use works;
insert into dbo.batter (id,type)
select ?,?
"""
tables = pd.read_sql("SELECT * FROM batter", conn)
print(tables)
conn.close()
conn.cursor()

