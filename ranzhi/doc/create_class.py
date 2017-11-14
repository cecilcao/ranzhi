# 打开火狐浏览器
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# 输入网址
driver.get('http://localhost/ranzhi/www')
# 加入休眠时间，让代码等一下浏览器去加载页面内容
sleep(1)
# 对用户名输入框进行定位
ele_name = driver.find_element_by_id('account')
# 往输入框内输入用户名
ele_name.send_keys('admin')
# 定位密码输入框和往输入框内输入内容
driver.find_element_by_name('password').send_keys('jaychou')
# 点击登录按钮
driver.find_element_by_class_name('btn-primary').click()
sleep(1)

driver.get('http://localhost/ranzhi/www/doc/tree-browse-doc-0-3.html')
driver.maximize_window()
sleep(3)
ele_iframe12 = driver.find_element_by_name('iframe-12')
driver.switch_to.frame(ele_iframe12)
sleep(1)
# driver.find_element_by_xpath(".//*[@name='children[820035]']").send_keys('建筑')
# driver.find_element_by_xpath(".//*[@name='children[820036]']").send_keys('自然')
# ele_leimus = driver.find_elements_by_xpath(".//*[@id='children[]']")
# for leimu in ele_leimus:
#     print(leimu.get_attribute('name'))
#     if leimu.get_attribute('name') == 'children[820035]':
#         leimu.send_keys('自然')
#     elif leimu.get_attribute('name') == 'children[820036]':
#         leimu.send_keys('建筑')
#     elif leimu.get_attribute('name') == 'children[820037]':
#         leimu.send_keys('音乐')
ele_leimus = driver.find_elements_by_xpath(".//*[@id='children[]']")
for leimu in ele_leimus:
    print(leimu)
    for i in range(820035, 820038, 1):
        if leimu.get_attribute('name')==('children[%d]'%i):
            leimu.send_keys('name%s'%i)