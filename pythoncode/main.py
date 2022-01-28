import pymysql

db = pymysql.connect(
	host = '127.0.0.1',
	port = 3306,
	user = 'root',
	password = 'root',
	db = 'xinkongapp',
)

cursor = db.cursor()

sql = "SELECT * FROM STUDENTS"

cursor.execute(sql)

data = cursor.fetchall()

for tup in data:
	print(tup)