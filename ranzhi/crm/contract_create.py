from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select


#打开Chrome浏览器，进入本地网址
driver = webdriver.Chrome()
driver.get('http://localhost/ranzhi/www')
#输入登录用户名密码，点击登录
driver.find_element_by_css_selector('#account').send_keys('admin')
driver.find_element_by_css_selector('#password').send_keys('jaychou')
driver.find_element_by_css_selector('#submit').click()
time.sleep(2)
#全屏浏览器
# driver.maximize_window()
time.sleep(1)
#点击合同菜单
driver.find_element_by_xpath('//*[@id="mainNavbar"]/div/ul[2]/li[5]/a').click()
time.sleep(1)
#切换iframe，点击创建合同按钮
driver.switch_to.frame('iframe-dashboard')
driver.find_element_by_xpath('//*[@id="menuActions"]/a').click()
time.sleep(1)
#返回文档框架，进入创建合同框架
driver.switch_to.default_content()
driver.switch_to.frame('iframe-1')
#选择客户列表框，找到选择项
driver.find_element_by_class_name("chosen-single").click()
driver.find_element_by_xpath('//*[@id="customer_chosen"]/div/ul/li[1]').click()
# select_customer =driver.find_element_by_xpath("//*[@id='customer']")
# select_customer.select_by_value('8')
#输入合同名称
driver.find_element_by_xpath('//*[@id="name"]').send_keys('吴振国的第三个合同')
#输入合同编号
driver.find_element_by_xpath('//*[@id="code"]').send_keys('HT20171111')
#输入金额
driver.find_element_by_xpath('//*[@id="amount"]').send_keys('8000')
#输入签署人
driver.find_element_by_xpath('//*[@id="signedBy_chosen"]').click()
driver.find_element_by_xpath('//*[@id="signedBy_chosen"]/div/ul/li[7]').click()
#提交保存
# driver.switch_to.parent_frame()
# driver.find_element_by_id('win-1').send_keys(Keys.DOWN)
# driver.find_element_by_xpath('//*[@id="submit"]').click()
# driver.find_element_by_css_selector('#deliveredDate').send_keys('2017-11-09')
# driver.switch_to.frame('iframe-1')
driver.find_element_by_xpath('//*[@id="fileBox2"]/tbody/tr/td[2]/input').send_keys(Keys.DOWN)
driver.find_element_by_id('submit').click()
driver.close()




