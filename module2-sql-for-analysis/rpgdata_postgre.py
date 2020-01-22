import sqlite3
import psycopg2


# Part One, upload rpg data into a PostgreSQL database
# Kwargs I need for psycopg2
dbname = 'sgklcusy'
user = 'sgklcusy'
password = 'xZ0qK9VtLPIf1rCaodKdLD5632VybMfY'
host = 'rajje.db.elephantsql.com'

# Use psycopg2 to connect to PostgreSQL database
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor()
pg_conn.commit()


# Connect rpg_db.sqlite3 to PostgreSQL database
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

row_count = 'SELECT COUNT(*) FROM charactercreator_character'
sl_curs.execute(row_count).fetchall()

get_characters = 'SELECT * FROM charactercreator_character'
characters = sl_curs.execute(get_characters).fetchall()

sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()

drop_table = '''DROP TABLE charactercreator_character;'''
pg_curs.execute(drop_table)

create_character_table = """
CREATE TABLE charactercreator_character (
  character_id SERIAL PRIMARY KEY,
  name VARCHAR(30),
  level INT,
  exp INT,
  hp INT,
  strength INT,
  intelligence INT,
  dexterity INT,
  wisdom INT
);
"""

pg_curs.execute(create_character_table)
pg_conn.commit()
