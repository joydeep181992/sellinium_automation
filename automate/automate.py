from selenium import webdriver
from selenium.webdriver.support.ui import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome("../drivers/chromedriver")
driver.get(
    "https://3278629.findlaw2.flsitebuilder.com/safe")

# wait = WebDriverWait(driver, 10000000)
# element = wait.until(EC.element_to_be_clickable((By.ID, 'safeLoginbtn')))

a = input('adasdka')


# elem = driver.find_element_by_name("s")
# elem.clear()
# elem.send_keys("*3278629")
# elem.send_keys(Keys.RETURN)


elem = driver.find_element(
    By.XPATH, '//*[@id="dashboard_right_now"]/div/div/ul/li[1]/a').click()

# elem = driver.find_element(
#     By.XPATH, '//*[@id="wpbody-content"]/div[3]/p/a[2]').click()


elem = driver.find_element(By.XPATH, '//*[@id="wpbody-content"]/div[3]/ul/li[2]/a').click()
# links = driver.execute_script('row-title')

# links = driver.execute_script('''
#     let list = window.document.querySelector("#the-list")
#     var listoflinks = window.document.querySelectorAll("#the-list a.row-title")
#     var links = []
#     Array.prototype.forEach.call(listoflinks, function(el){ 
#         links.push(el.href)
#     } )
    
# ''')

# print(links)

link = driver.find_elements_by_class_name('row-title')
links = []
for elem in link:
    links.append(elem.get_attribute("href"))

# print(links)

for i in links:

    # links = driver.find_elements_by_class_name('row-title')
    
    driver.get(f'{i}')
    # driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    # driver.close()

    select = Select(driver.find_element_by_name('pagegoals'))
    select.select_by_value('goal4')

    select = Select(driver.find_element_by_name('pagetype'))
    select.select_by_value('marketing')

    driver.execute_script('window.document.querySelector("#publish").click()')

    driver.implicitly_wait(15)




# driver.execute_script("window.history.go(-1)")


# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')


# actionChains = ActionChains(driver)

# actionChains.context_click(links[0]).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.RETURN).perform()

# .find_element(By.CSS_SELECTOR, '')

# select = Select(driver.find_element_by_name('pagegoals'))
# select.select_by_value('goal4')
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')


# elem = driver.find_element(
#     By.XPATH, '//*[@id="post-48480"]/td[1]/strong/a').click()

# select = Select(driver.find_element_by_name('pagegoals'))

# select.select_by_value('goal4')
# driver.close()
