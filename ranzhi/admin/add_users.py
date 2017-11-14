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
driver.maximize_window()
time.sleep(1)
#点击后台管理
driver.find_element_by_xpath('//*[@id="s-menu-superadmin"]/button').click()
#点击组织
driver.switch_to.frame('iframe-superadmin')
driver.find_element_by_xpath('//*[@id="mainNavbar"]/ul/li[2]/a').click()

#批量创建50个用户
for i in range(0,50,1):
    # 点击添加成员
    driver.find_element_by_link_text( '添加成员' ).click()
    driver.find_element_by_id('account').send_keys('wuzhenguo'+str(i))
    driver.find_element_by_id('realname').send_keys('吴振国的第'+str(i)+'个账号')
    role = Select(driver.find_element_by_id('role'))
    role.select_by_value('support')
    driver.find_element_by_id('password1').send_keys('123456')
    driver.find_element_by_id('password2').send_keys('123456')
    driver.find_element_by_id('email').send_keys('wuzhenguo'+str(i)+'@qq.com')
    driver.find_element_by_id('submit').click()
    driver.implicitly_wait(2)
#创建50个完毕，关闭浏览器
driver.close()