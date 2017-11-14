from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#打开Chrome浏览器，进入本地网址
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('http://localhost/ranzhi/www')
driver.implicitly_wait(2)
#输入登录用户名密码，点击登录
driver.find_element_by_css_selector('#account').send_keys('admin')
driver.find_element_by_css_selector('#password').send_keys('jaychou')
driver.find_element_by_css_selector('#submit').click()
driver.implicitly_wait(2)
driver.maximize_window()
#点击文档-首页-点击创建文档库
driver.find_element_by_xpath('//*[@id="s-menu-12"]/button').click()
driver.switch_to.frame('iframe-12')
driver.find_element_by_link_text('首页').click()
driver.find_element_by_id('createButton').click()
driver.implicitly_wait(2)
#编辑文档库并并保存
Select(driver.find_element_by_id('libType')).select_by_value('custom')
driver.find_element_by_id('name').send_keys('曹锡山的第1个文档库')
# driver.find_element_by_id('private').click()
driver.find_element_by_xpath('//*[@id="users_chosen"]').click()
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="users_chosen"]/div/ul/li[6]').click()
driver.find_element_by_xpath('//*[@id="groups1"]').click()
driver.find_element_by_xpath('//*[@id="groups2"]').click()
driver.find_element_by_xpath('//*[@id="groups5"]').click()
driver.find_element_by_xpath('//*[@id="submit"]').click()
driver.implicitly_wait(1)