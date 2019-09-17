from selenium import webdriver
from selenium.webdriver.support.ui import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# Custom made class for the initial site
class Driver():
    driver = webdriver.Chrome("../drivers/chromedriver")
    def __init__(self, site_url, links_archive_css=None, links_from_heading=None):
        self.site_url = site_url
        self.links_archive_css = links_archive_css
        self.links_from_heading = links_from_heading
    
    def get_the_url(self):
        return self.driver.get(self.site_url)

    def get_all_links_from_archive(self):
        link = self.driver.find_elements(By.XPATH, self.links_archive_css)
        links = []
        for elem in link:
            links.append(elem.get_attribute("href"))

        # print(links)
        ul_links = []
        for i in links:
            self.driver.get(i)
            linkk = self.driver.find_elements(By.XPATH, self.links_from_heading)
            for href in linkk:
                ul_links.append(href.get_attribute("href"))
        
        return ul_links

    # driver.close()

site_url = "http://wlgpatfl2.firmsitepreview.com/blog/archives.shtml"
links_archive_css = "/html/body/div[2]/div[2]/div[1]/div/article/div/ul[2]/li/a"
links_from_heading = "/html/body/div[2]/div[2]/div[1]/div/article/article/header/h2/a"

s = Driver(site_url, links_archive_css, links_from_heading)
s.get_the_url()
links = s.get_all_links_from_archive()
# print(links)

with open('links.txt', 'w') as fp:
    for i in links:
        fp.write(i)

# Accessing the Wordpress Site