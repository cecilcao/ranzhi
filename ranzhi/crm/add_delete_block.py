from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

# 打开Chrome浏览器，进入本地网址
driver = webdriver.Chrome()
driver.get( 'http://localhost/ranzhi/www' )
# 输入登录用户名密码，点击登录
driver.find_element_by_css_selector( '#account' ).send_keys( 'admin' )
driver.find_element_by_css_selector( '#password' ).send_keys( 'jaychou' )
driver.find_element_by_css_selector( '#submit' ).click()
time.sleep( 2 )
# 全屏浏览器
driver.maximize_window()
time.sleep( 1 )


def create_block(blocktype, type, orderby):
    # 点击客户管理
    driver.implicitly_wait(3)
    driver.switch_to.default_content()
    driver.find_element_by_xpath( '//*[@id="s-menu-1"]' ).click()
    # 进入iframe-1
    driver.switch_to.frame('iframe-1')
    # driver.implicitly_wait(3)
    print('进入iframe-1成功')
    time.sleep(3)
    # 点击创建区块按钮
    driver.find_element_by_css_selector( 'a.btn' ).click()
    driver.implicitly_wait(2)
    # 选择区块类型为订单
    ele_blocktype = Select( driver.find_element_by_id( 'blocks' ) )
    ele_blocktype.select_by_value( blocktype )
    driver.implicitly_wait( 2 )
    # 输入区块名称
    block_name = driver.find_element_by_id( 'title' )
    block_name.clear()
    block_name.send_keys( "我的%s列表" % blocktype )
    # 选择外观宽度
    ele_width = Select( driver.find_element_by_id( 'grid' ) )
    ele_width.select_by_value( '4' )
    # 选择外观颜色
    driver.find_element_by_css_selector( '.dropdown-toggle' ).click()
    driver.implicitly_wait( 1 )
    ele_color = driver.find_element_by_css_selector( 'div.dropdown-menu > li:nth-child(1) > button:nth-child(1)' )
    ele_color.click()
    # 选择类型
    driver.find_element_by_css_selector( '#paramstype_chosen' ).click()
    ele_type = driver.find_element_by_css_selector(
        '#paramstype_chosen > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)' )
    ele_type.send_keys( type )
    ele_type.send_keys( Keys.ENTER )
    driver.implicitly_wait(1)
    # 输入数量
    ele_num = driver.find_element_by_xpath( '//*[@id="params[num]"]' )
    ele_num.clear()
    ele_num.send_keys( '10' )
    # 选择排序方式
    driver.find_element_by_css_selector( '#paramsorderBy_chosen' ).click()
    ele_orderby = driver.find_element_by_css_selector(
        '#paramsorderBy_chosen > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)' )
    ele_orderby.send_keys( orderby )
    ele_orderby.send_keys( Keys.ENTER )
    # 点击保存
    driver.find_element_by_id( 'submit' ).click()
    driver.implicitly_wait( 2 )
def delete_block():
    for i in range(1,10,1):
        driver.implicitly_wait( 1 )
        driver.switch_to.default_content()
        driver.find_element_by_xpath( '//*[@id="s-menu-1"]' ).click()
        # 进入iframe-1
        driver.switch_to.frame( 'iframe-1' )
        driver.implicitly_wait( 2 )
        print( '进入iframe-1成功' )
        if isElementExist('block%d'%i):
            ele_block_button= driver.find_element_by_css_selector('#block%d > div.panel-heading > div > div > button'%i)
            ele_block_button.click()
            driver.implicitly_wait(2)
            ele_delete_buttons= driver.find_element_by_css_selector('#block%d > div.panel-heading > div > div > ul > li:nth-child(2) > a'%i)
            ele_delete_buttons.click()
            driver.implicitly_wait(2)
            driver.switch_to.alert.accept()
            driver.implicitly_wait(2)
            print('删除block%d成功'%i)
        else:
            print('找不到block%d\n'%i)
def isElementExist(element):
    flag = True
    try:
        driver.find_element_by_id(element)
        return flag
    except:
        flag=False
        return flag

create_block('order','由我创建','ID 递增')
create_block('contract', '由我交付', '金额递增')
create_block('customer','本周联系', 'ID 递减')
driver.get('http://localhost/ranzhi/www/crm/dashboard/')
delete_block()