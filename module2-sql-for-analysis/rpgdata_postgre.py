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
pg_conn.commit()

# Connect rpg_db.sqlite3 to PostgreSQL database
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
