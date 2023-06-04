
import pypyodbc as odbc
driver_name = 'SQL SERVER'
sever_name = 'DESKTOP-F726TKR'
data_base = 'works'
connection_string = f"""
DRIVER={{{driver_name}}};
SERVER={sever_name};
DATA_BASE={data_base};
trusted_connection=yes;
"""
conn = odbc.connect(connection_string)
print(conn)
insert_query = """
use works;
insert into dbo.usd (time_stamp, INR, EU)
select ?,?,?
"""
insert_list = ['123','567','asd']
cursor = conn.cursor()
cursor.execute(insert_query, insert_list)
conn.commit()
cursor.close()
conn.close()