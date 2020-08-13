from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time




#If you are on a personal machine you can hard code your credientials here
userName = input("Enter Time Clock User Name: ")
password = getpass.getpass("Enter Time Clock Password: ")


driver = webdriver.Chrome()

driver.get("https://www.opentimeclock.com/free.html")
#assert "opentimeclock" in driver.title
elem = driver.find_element_by_id("txtUser")
elem.clear()
elem.send_keys(userName)
elem.send_keys(Keys.RETURN)

elem = driver.find_element_by_id("txtPassword")
elem.clear()
elem.send_keys(password)

time.sleep(2)
elem.send_keys(Keys.RETURN)


 