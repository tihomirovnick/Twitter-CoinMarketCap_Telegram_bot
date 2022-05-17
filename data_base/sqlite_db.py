import sqlite3 as sq

def sql_start():
	global base, cur
	base = sq.connect('twitter.db')
	cur = base.cursor()
	if base:
		print("DataBase connected")
	base.execute('CREATE TABLE IF NOT EXISTS main(id TEXT)')
	base.commit()

async def sql_add_command():
	cur.execute("INSERT INTO main VALUES ('1')")
	base.commit()

async def sql_edit_command(element):
	cur.execute('UPDATE main SET id = ?', (element,))
	base.commit()

async def sql_read():
	a = []
	for ret in cur.execute('SELECT * FROM main WHERE rowid == 1').fetchall():
		a.append((f'{ret[0]}'))
		break
	return a[0]