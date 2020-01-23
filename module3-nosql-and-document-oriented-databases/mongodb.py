"""I like using pymongo better than postgres, I feel like it feels more intuitive this way
and you don't have to keep track of too many cursors. I also feel like
the code is more simple
"""

import pymongo
import sqlite3

# First, connect to pymongo
client = pymongo.MongoClient(
    "mongodb://ADMIN:@cluster0-shard-00-00-aen9r.mongodb.net:27017,cluster0-shard-00-01-aen9r.mongodb.net:27017,cluster0-shard-00-02-aen9r.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test


# Make rpg_db.sqlite3 character table
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

row_count = 'SELECT COUNT(*) FROM charactercreator_character'
sl_curs.execute(row_count).fetchall()

get_characters = 'SELECT * FROM charactercreator_character'
characters = sl_curs.execute(get_characters).fetchall()

sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()

# So I can run the script multiple times without it giving an error
drop_table = '''DROP TABLE charactercreator_character;'''
sl_curs.execute(drop_table)

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

sl_curs.execute(create_character_table)
sl_conn.commit()

# Fill table with characters
for character in characters:
    insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
    sl_curs.execute(insert_character)
    sl_conn.commit()

# Make character_table a document

character_query = "SELECT * FROM charactercreator_character;"
charactercreator_character = sl_curs.execute(character_query).fetchone()
# Different variable name here to avoid confusion
all_characters = sl_curs.execute(character_query).fetchall()

first_character = all_characters[0]


rpg_doc = {
    'sql_key': all_characters[0],
    'name': all_characters[1],
    'level': all_characters[2],
    'exp': all_characters[3],
    'hp': all_characters[4],
    'strenth': all_characters[5],
    'intelligence': all_characters[6],
    'dexterity': all_characters[7],
    'wisdom': all_characters[8]
}

db.test.insert_one(rpg_doc)

list(db.test.find(rpg_doc))

print(all_characters)
