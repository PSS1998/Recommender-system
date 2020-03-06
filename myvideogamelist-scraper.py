from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import config



#options = FirefoxOptions()
#options.add_argument("--headless")
driver = webdriver.Firefox()
driver.implicitly_wait(5)

main_url = f'https://myvideogamelist.com/mylist/{config.MYVIDEOGAMELIST_USERNAME}'
driver.get(main_url)
games = driver.find_elements_by_css_selector('td > a')

list_games = []
for game in games:
	list_games.append(game.text)

driver.quit()

with open('games.txt', 'w') as f:
	for item in list_games:
		f.write("%s\n" % item)