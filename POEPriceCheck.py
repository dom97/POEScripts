#! python3
# POEPriceCheck.py - checks price of item in poe
import selenium, sys

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://poe.ninja/challenge/prophecies')

item = " ".join(sys.argv[1:])
path = "//span[contains(text(), '" + item + "')]/ancestor::tr/descendant::img[@title='Chaos Orb']/parent::span"

price = browser.find_element_by_xpath(path).text

print(price)
