from selenium import webdriver
from selenium.webdriver.common.keys import Keys

target_urls = ['https://boards.greenhouse.io/khanacademy/jobs/15827']

def fill_in_info():
	driver = webdriver.Chrome()
	driver.get('https://boards.greenhouse.io/khanacademy/jobs/15827')

fill_in_info()