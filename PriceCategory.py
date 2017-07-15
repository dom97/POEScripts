#! python3
# POEPriceCheck.py - checks price of item in poe
# works with prophecies, divination cards, unique maps, flasks, weapons, armours, 
#TODO get it to hit the show all
import selenium, sys

from selenium import webdriver
from tinydb import TinyDB, Query

db = TinyDB('db.json')
#probably flip these to name the db table
categories = {'prophecy':'prophecies', 'div':'divinationcards', 'map':'unique-maps', 'jewel':'unique-jewels', 'flask':'unique-flasks', 'weapon':'unique-weapons', 'armour':'unique-armours', 'accessory':'unique-accessories'}
urls = ['prophecies', 'divinationcards', 'unique-maps', 'unique-jewels', 'unique-flasks', 'unique-weapons', 'unique-armours', 'unique-accessories']
browser = webdriver.Firefox()
for url in urls:
    table = db.table(url)
    
    browser.get('http://poe.ninja/challenge/' + url)

    path = "//*[contains(text(),'Show all')]"
    try:
        browser.find_element_by_xpath(path).click()
    except(Exception):
        pass

    rows = browser.find_elements_by_tag_name('tr')
    del rows[0]

    for row in rows:
        parts = row.text.splitlines()
        item_name = parts[0]
        chaos_price = parts[len(parts)-2]
        table.insert({'name': item_name, 'price': chaos_price})
        #print(item_name + ':' + chaos_price)
browser.close()