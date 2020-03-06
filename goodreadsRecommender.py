import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions



def goodreads_recommender(query):
	options = FirefoxOptions()
	options.add_argument("--headless")
	driver = webdriver.Firefox(options=options)
	driver.implicitly_wait(5)

	url = "https://www.goodreads.com/"

	driver.get(url)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
	time.sleep(1)
	search_box = driver.find_element_by_css_selector('#sitesearch_field')
	search_box.send_keys(query)
	driver.find_elements_by_css_selector('#headerSearchForm img')[1].click()

	driver.find_element_by_css_selector('tr:nth-child(1) .bookTitle span').click()

	driver.find_element_by_css_selector('.bookCarousel+ .seeMoreLink').click()

	books = driver.find_elements_by_css_selector('.gr-d-lg-none+ div .listWithDividers .gr-h3--noMargin span , .gr-boxBottomDivider .gr-h3--noMargin span')
	book_list = []
	count = 0
	for book in books:
		count += 1
		if count%3 == 1:
			book_list.append(book.text)

	driver.quit()

	return book_list

#print(goodreads_recommender("Angels & Demons"))