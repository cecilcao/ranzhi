from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

#打开Chrome浏览器，进入本地网址
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('http://localhost/ranzhi/www')
driver.implicitly_wait(2)
#输入登录用户名密码，点击登录
driver.find_element_by_css_selector('#account').send_keys('admin')
driver.find_element_by_css_selector('#password').send_keys('jaychou')
driver.find_element_by_css_selector('#submit').click()
driver.maximize_window()
driver.implicitly_wait(2)
#点击文档-首页-进入文档库
driver.find_element_by_xpath('//*[@id="s-menu-12"]/button').click()
driver.switch_to.frame('iframe-12')
driver.find_element_by_link_text('首页').click()
driver.find_element_by_link_text('曹锡山的第1个文档库').click()
driver.implicitly_wait(2)
#点击创建文档按钮
driver.find_element_by_xpath('//*[@id="menuActions"]/a').click()
driver.implicitly_wait(2)
#编辑文档并保存
Select(driver.find_element_by_id('module')).select_by_visible_text('/科学')
#授权用户
# driver.find_element_by_xpath('//*[@id="users_chosen"]/ul').click()
# driver.implicitly_wait(1)
# driver.find_element_by_xpath('//*[@id="users_chosen"]/div/ul/li[4]').click()
# driver.find_element_by_xpath('//*[@id="users_chosen"]/ul').click()
#driver.implicitly_wait(1)
# driver.find_element_by_xpath('//*[@id="users_chosen"]/div/ul/li[6]').click()
driver.find_element_by_xpath('//*[@id="userTR"]/td').click()
driver.implicitly_wait(1)
users = driver.find_element_by_xpath('//*[@id="users_chosen"]/ul/li/input')
users.send_keys('小草001')
users.send_keys(Keys.ENTER)
users.send_keys('小草002')
users.send_keys(Keys.ENTER)
#授权分组
driver.find_element_by_id('groups1').click()
driver.find_element_by_id('groups2').click()
#选择文本还是链接,2选1
driver.find_element_by_id('typetext').click()
#driver.find_element_by_id('typeurl').click()

#输入文档标题
driver.find_element_by_id('title').send_keys('曹锡山的第3个文档标题')
#进入文档正文所在iframe
driver.switch_to.frame('ueditor_0')
#编辑正文内容
driver.implicitly_wait(1)
content = '在使用selenium webdriver进行元素定位时，' \
          '通常使用findElement或findElements方法结合By类返回的元素句柄来定位元素。' \
          '其中By类的常用定位方式共八种，现分别介绍如下。'
driver.find_element_by_xpath('/html/body').send_keys(content)
document = driver.find_element_by_xpath('html/body')
ActionChains(driver).move_to_element(document).perform()
ActionChains(driver).key_down(document)
driver.implicitly_wait(1)
driver.switch_to.parent_frame()
#将页面滚动条拖到底部
# js="var q = document.body.scrollTop=100000"
# driver.execute_script(js)
# driver.implicitly_wait(3)
#编辑关键字
driver.find_element_by_xpath('//*[@id="keywords"]').send_keys('webdriver')
driver.find_element_by_xpath('//*[@id="keywords"]').send_keys(Keys.DOWN)
#上传附件
driver.find_element_by_xpath('//*[@id="fileBox1"]/tbody/tr/td[1]/div/input').send_keys(r'C:\Users\hzpower\Desktop\CecilCAO\CAO.jpg')
#保存提交
driver.implicitly_wait(1)
driver.find_element_by_id('submit').click()



