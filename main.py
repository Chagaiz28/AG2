import mysql.connector as sql
import pandas as pd

db_connection = sql.connect(host="localhost",user='root',password="123456",database="statlog")
db_cursor = db_connection.cursor()

db_cursor.execute("SELECT * FROM germancredit")

table_rows = db_cursor.fetchall()
df = pd.DataFrame(table_rows)
print(df)
table_columns = db_cursor.column_names
print(table_columns)