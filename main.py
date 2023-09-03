import mysql.connector
from random import choice 

first_name_query = "SELECT first_name.value, region.language FROM first_name INNER JOIN region ON first_name.id_region = region.region_id;"
last_name_query = "SELECT last_name.value, region.language FROM last_name INNER JOIN region ON last_name.id_region = region.region_id;"


database_config = {
    "user": "tournament_user",
    "password": "tournament_pass",
    "database": "name_generator",
    "host": "localhost"
}

first_names = []
last_names = [] 
players_data = []

conn = mysql.connector.connect(**database_config)
cursor = conn.cursor()

cursor.execute(first_name_query)
first_names += cursor.fetchall() # get first names list

cursor.execute(last_name_query)
last_names += cursor.fetchall() # get last names list

conn.close()

for i in range(10000):
    name = ' '.join([choice(first_names)[0], choice(last_names)[0]])