from tkinter import DoubleVar
from tokenize import Double
from unicodedata import decimal
from xml.dom import minidom
import xml.etree.ElementTree as ET
import pymysql

path = 'AstralBattles.Core.CardDefinitions.xml'

tree = ET.parse(path)
root = tree.getroot()


connection = pymysql.connect(host="localhost",user="Giveng",passwd="Fybcbvjdf2002",database="astrall_battles" )
cursor = connection.cursor()
cursor.execute(f"select count(card_id) from cards")
rows = cursor.fetchall()
count_rows = rows[0][0]
cursor.close()
card_id = count_rows

for card in root:
    if "CreatureCard" in card.get('{http://www.w3.org/2001/XMLSchema-instance}type') and card.find('ElementType').text != "Neutral":
        print(card.get('{http://www.w3.org/2001/XMLSchema-instance}type'))
        print("Base name: " + card.find('Name').text.lower())
        print("Element: " + card.find('ElementType').text)
        print("Cost: " + card.find('Cost').text)
        print("Damage: " + card.find('Damage').text)
        print("Health: " + card.find('Health').text)
        if card.find('Skills').text != "":
            try:
                print("Skills: " + card.find('Skills').text)
            except:
                print("Skills: " )
        localiazation = card.find('Localization')
        en = localiazation.find('en-US')
        print("Card name: " + en.find('DisplayName').text)
        print("Description: " + en.find('Description').text)
        print()

        card_id += 1
        image_path = card.find('Name').text.lower()
        damage = int(card.find('Damage').text)
        health = int(card.find('Health').text)
        element = card.find('ElementType').text
        card_name = en.find('DisplayName').text
        description = en.find('Description').text.replace('\'', '')
        cost = float(card.find('Cost').text)
        try:
            skills = card.find('Skills').text
        except:
            skills = None
        try:
            level = int(card.find('Level').text)
        except:
            level = None

        cursor = connection.cursor()
        query = f"insert into cards (card_id, image_path, damage, health, element, card_name, description, cost, skills, level) values({card_id}, '{image_path}', {damage}, {health}, '{element}', '{card_name}', '{description}', {cost}, '{skills}', {level})"
        cursor.execute(query)
        cursor.close()
        connection.commit()

print(len(root))
connection.close()