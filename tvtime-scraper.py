from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import config



#options = FirefoxOptions()
#options.add_argument("--headless")
driver = webdriver.Firefox()
driver.implicitly_wait(5)

main_url = 'https://www.tvtime.com/'
driver.get(main_url)
driver.find_element_by_css_selector('.jeNIEE .iLlEYj').click()
form = driver.find_elements_by_css_selector('.dEGBOo')
form[0].send_keys(config.TVTIME_USERNAME)
form[1].send_keys(config.TVTIME_PASSWORD)
driver.find_element_by_css_selector('.cZrFfs').click()

driver.find_element_by_css_selector('.profile a').click()

driver.find_element_by_css_selector('.icon-tvst-arrow_down').click()
driver.find_element_by_css_selector('.up-to-date').click()

shows = driver.find_elements_by_css_selector('#all-shows .poster-details a')

list_shows = []
for show in shows:
	list_shows.append(show.text)

driver.quit()

with open('tvshows.txt', 'w') as f:
	for item in list_shows:
		f.write("%s\n" % item)