import sqlite3
db_file = 'db.file'
connection = sqlite3.connect(db_file)

def check_tables(table_name):
	with connection:
		ret = connection.execute("SELECT * FROM sqlite_master WHERE name ='%s' and type='table';" % table_name)
	print(ret)

def init():
	# table_name column_name
	table_name = 'mark_video'
	
	with connection:
		connection.execute('''
	CREATE TABLE IF NOT EXISTS FRAMES
	       (ID	    INT     PRIMARY KEY     NOT NULL,
	       VIDEO        INT     NOT NULL,
	       FRAMES       TEXT    NOT NULL,
	       MARK_POINT   TEXT    NULL);

		''')	
		connection.execute('''
	CREATE TABLE IF NOT EXISTS VIDEOS
		(ID	    INT    PRIMARY KEY	    NOT NULL,
		NAME	    TEXT   NOT NULL,
		MATRIX	    TEXT   NOT NULL);
		''')
 
def select_by_frameId(id):
	with connection:
		cursor = connection.execute('SELECT * from')
	pass
def select_by_videoname(name):
	pass

init('makr_video')
