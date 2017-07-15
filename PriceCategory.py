#! python3
# POEPriceCheck.py - checks price of item in poe
# works with prophecies, divination cards, unique maps, flasks, weapons, armours, 
#TODO get it to hit the show all
import selenium, sys

from selenium import webdriver

categories = {'prophecy':'prophecies', 'div':'divinationcards', 'map':'unique-maps', 'jewel':'unique-jewels', 'flask':'unique-flasks', 'weapon':'unique-weapons', 'armour':'unique-armours', 'accessory':'unique-accessories'}
end_url = categories[sys.argv[1]]

browser = webdriver.Firefox()
browser.get('http://poe.ninja/challenge/' + end_url)

path = "//*[contains(text(),'Show all')]"

browser.find_element_by_xpath(path).click()

rows = browser.find_elements_by_tag_name('tr')
del rows[0]

for row in rows:
    parts = row.text.splitlines()
    item_name = parts[0]
    chaos_price_index = len(parts)-2
    print(parts[0] + ':' + parts[chaos_price_index])
browser.close()