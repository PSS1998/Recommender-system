from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import config



#options = FirefoxOptions()
#options.add_argument("--headless")
driver = webdriver.Firefox()
driver.implicitly_wait(5)


main_url = f'https://letterboxd.com/{config.LETTERBOXD_USERNAME}/films/'

driver.get(main_url)

list_movie = []

for i in range(100):
	movies = driver.find_elements_by_css_selector('.frame')
	count = 0
	for movie in movies:
		count += 1
		if count == 2:
			continue
		list_movie.append(movie.get_attribute('data-original-title'))
	try:
		driver.find_element_by_css_selector('.next').click()
	except:
		break

driver.quit()

with open('movies.txt', 'w') as f:
	for item in list_movie:
		f.write("%s\n" % item)
