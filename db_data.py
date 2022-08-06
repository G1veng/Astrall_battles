import pymysql

def get_path(name):
	connection = pymysql.connect(host="localhost",user="Giveng",passwd="Fybcbvjdf2002",database="astrall_battles" )
	cursor = connection.cursor()
	cursor.execute(f"select image_path from cards where card_name = '{name}'")
	rows = cursor.fetchall()
	connection.close()
	return rows[0][0]

def collect_path(image):
	return f"D:\\Python\\Astrall_battles\\Images\\" + str(image) + ".bmp"

def collect_head_path(id):
	return f"D:\\Python\\Astrall_battles\\Images\\Faces\\face" + str(id) + ".bmp"

def get_description(name):
	connection = pymysql.connect(host="localhost",user="Giveng",passwd="Fybcbvjdf2002",database="astrall_battles" )
	cursor = connection.cursor()
	cursor.execute(f"select description from cards where card_name = '{name}'")
	rows = cursor.fetchall()
	connection.close()
	return rows[0][0]

def get_path_via_index(index):
	connection = pymysql.connect(host="localhost",user="Giveng",passwd="Fybcbvjdf2002",database="astrall_battles" )
	cursor = connection.cursor()
	cursor.execute(f"select image_path from cards where card_id = {index}")
	rows = cursor.fetchall()
	connection.close()
	return rows[0][0]

def get_name(index):
	connection = pymysql.connect(host="localhost",user="Giveng",passwd="Fybcbvjdf2002",database="astrall_battles" )
	cursor = connection.cursor()
	cursor.execute(f"select card_name from cards where card_id = {index}")
	rows = cursor.fetchall()
	connection.close()
	return rows[0][0]

def get_count_row():
	connection = pymysql.connect(host="localhost",user="Giveng",passwd="Fybcbvjdf2002",database="astrall_battles" )
	cursor = connection.cursor()
	cursor.execute(f"select count(card_id) from cards")
	rows = cursor.fetchall()
	connection.close()
	return rows[0][0]

def get_healt(name):
	connection = pymysql.connect(host="localhost",user="Giveng",passwd="Fybcbvjdf2002",database="astrall_battles" )
	cursor = connection.cursor()
	cursor.execute(f"select health from cards where card_name = '{name}'")
	rows = cursor.fetchall()
	connection.close()
	return rows[0][0]

def get_cost(name):
	connection = pymysql.connect(host="localhost",user="Giveng",passwd="Fybcbvjdf2002",database="astrall_battles" )
	cursor = connection.cursor()
	cursor.execute(f"select cost from cards where card_name = '{name}'")
	rows = cursor.fetchall()
	connection.close()
	return rows[0][0]

def get_damage(name):
	connection = pymysql.connect(host="localhost",user="Giveng",passwd="Fybcbvjdf2002",database="astrall_battles" )
	cursor = connection.cursor()
	cursor.execute(f"select damage from cards where card_name = '{name}'")
	rows = cursor.fetchall()
	connection.close()
	return rows[0][0]

def get_head_path(id):
	connection = pymysql.connect(host="localhost",user="Giveng",passwd="Fybcbvjdf2002",database="astrall_battles" )
	cursor = connection.cursor()
	cursor.execute(f"select head_path from heads where head_id = '{id}'")
	rows = cursor.fetchall()
	connection.close()
	return rows[0][0]

def get_head_health(id):
	connection = pymysql.connect(host="localhost",user="Giveng",passwd="Fybcbvjdf2002",database="astrall_battles" )
	cursor = connection.cursor()
	cursor.execute(f"select head_health from heads where head_id = '{id}'")
	rows = cursor.fetchall()
	connection.close()
	return rows[0][0]	

def get_element(name):
	connection = pymysql.connect(host="localhost",user="Giveng",passwd="Fybcbvjdf2002",database="astrall_battles" )
	cursor = connection.cursor()
	cursor.execute(f"select element from cards where card_name = '{name}'")
	rows = cursor.fetchall()
	connection.close()
	return rows[0][0]

def get_head(id):
	connection = pymysql.connect(host="localhost",user="Giveng",passwd="Fybcbvjdf2002",database="astrall_battles" )
	cursor = connection.cursor()
	cursor.execute(f"select head_path from heads where head_id = '{id}'")
	rows = cursor.fetchall()
	connection.close()
	return rows[0][0]

def get_count_of_heads():
	connection = pymysql.connect(host="localhost",user="Giveng",passwd="Fybcbvjdf2002",database="astrall_battles" )
	cursor = connection.cursor()
	cursor.execute(f"select count(head_id) from heads")
	rows = cursor.fetchall()
	connection.close()
	return rows[0][0]