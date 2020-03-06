from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import time

import config



#options = FirefoxOptions()
#options.add_argument("--headless")
driver = webdriver.Firefox()
driver.implicitly_wait(5)

main_url = config.GOODREADS_MYBOOKS_URL
driver.get(main_url)

SCROLL_PAUSE_TIME = 5
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
	# Scroll down to bottom
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	# Wait to load page
	time.sleep(SCROLL_PAUSE_TIME)
	# Calculate new scroll height and compare with last scroll height
	new_height = driver.execute_script("return document.body.scrollHeight")
	if new_height == last_height:
		break
	last_height = new_height

books = driver.find_elements_by_css_selector('.title a')

list_books = []
for book in books:
	list_books.append(book.text)

driver.quit()

with open('books.txt', 'w') as f:
	for item in list_books:
		f.write("%s\n" % item)