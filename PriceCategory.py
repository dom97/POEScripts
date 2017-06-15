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

path = //*[contains(text(),'Show all')]

browser.find_element_by_xpath(path).click()

rows = browser.find_elements_by_tag_name('tr')
del row[0]

for row in rows
    #here is a good place to parse each row and only print out the name and price in chaos
    #probably the easiest way to do this is to split by space and grab all text prior to "wiki"
    # to grab price either count back spaces in the split or find the span without style in the class "text-right" 
    print(row.text)
    parts = row.split(' ')
    index = -1
    price_index = -1
    for idx, part in enumerate(parts):
        if part.lower() == 'wiki':
    	    index = idx
        elif part.lower() == 'x' and idx == (len(parts) - 1):
            price_index = idx - 1
        item_name = ' '.join(parts[0:index])
        price = parts[price_index]
        print(item_name + price)
