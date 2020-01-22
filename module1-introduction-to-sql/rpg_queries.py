import pandas as pd
import sqlite3


# Total Characters
conn = sqlite3.connect('rpg_db.sqlite3')

curs = conn.cursor()

query1 = '''SELECT SUM(character_id)
FROM charactercreator_character;'''

print('Total Characters:')
print(curs.execute(query1).fetchall())

conn.commit()
conn.close()

# Total Clerics
conn = sqlite3.connect('rpg_db.sqlite3')

curs = conn.cursor()

query2cleric = '''SELECT sum(character_ptr_id)
from charactercreator_cleric;'''

print('Total Clerics:')
print(curs.execute(query2cleric).fetchall())

conn.commit()
conn.close()

# Total Fighters
conn = sqlite3.connect('rpg_db.sqlite3')

curs = conn.cursor()

query2fighter = '''SELECT sum(character_ptr_id)
from charactercreator_fighter;'''

print('Total Fighters:')
print(curs.execute(query2fighter).fetchall())

conn.commit()
conn.close()

# Total Mages
conn = sqlite3.connect('rpg_db.sqlite3')

curs = conn.cursor()

query2mage = '''SELECT sum(character_ptr_id)
from charactercreator_mage;'''

print('Total Mages:')
print(curs.execute(query2mage).fetchall())

conn.commit()
conn.close()

# Total Necromancers
conn = sqlite3.connect('rpg_db.sqlite3')

curs = conn.cursor()

query2necromancer = '''SELECT sum(mage_ptr_id)
from charactercreator_necromancer;'''

print('Total Necromancers:')
print(curs.execute(query2necromancer).fetchall())

conn.commit()
conn.close()

# Total Thieves
conn = sqlite3.connect('rpg_db.sqlite3')

curs = conn.cursor()

query2thief = '''SELECT sum(character_ptr_id)
from charactercreator_thief;'''

print('Total Thieves:')
print(curs.execute(query2thief).fetchall())

conn.commit()
conn.close()

# Total Items
conn = sqlite3.connect('rpg_db.sqlite3')

curs = conn.cursor()

query3 = '''SELECT COUNT (*)
FROM armory_item;'''

print('Total Items:')
print(curs.execute(query3).fetchall())

conn.commit()
conn.close()

# Total Weapons
conn = sqlite3.connect('rpg_db.sqlite3')

curs = conn.cursor()

query4 = '''SELECT COUNT(DISTINCT item_id)FROM armory_item
WHERE item_id NOT IN (SELECT item_ptr_id FROM armory_weapon);'''

print('Total Weapons:')
print(curs.execute(query4).fetchall())

conn.commit()
conn.close()

# How many items each character has
conn = sqlite3.connect('rpg_db.sqlite3')

curs = conn.cursor()

query5 = '''SELECT character_id, count(id)
FROM charactercreator_character_inventory
GROUP by character_id
LIMIT 20;'''

print('Total Items per Character:')
print(curs.execute(query5).fetchall())

conn.commit()
conn.close()

# How many weapons each character has
conn = sqlite3.connect('rpg_db.sqlite3')

curs = conn.cursor()

query6 = '''SELECT character_id, count(item_ptr_id)
FROM charactercreator_character_inventory,
armory_weapon
GROUP by character_id
LIMIT 20;'''

print('Total weapons per Character:')
print(curs.execute(query6).fetchall())

conn.commit()
conn.close()


'''########################Part 2##########################'''

df = pd.read_csv('buddymove_holidayiq.csv')

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

df.to_sql('buddymove_holiday', conn)
