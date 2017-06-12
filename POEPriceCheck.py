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

item = " ".join(sys.argv[2:])
path = "//span[contains(text(), '" + item + "')]/ancestor::tr/descendant::img[@title='Chaos Orb']/parent::span"

try:
    price = browser.find_element_by_xpath(path).text
    print(item + ":" + price)
except selenium.common.exceptions.NoSuchElementException as  e:
    print('cant find item')
price = browser.find_element_by_xpath(path).text

browser.quit()