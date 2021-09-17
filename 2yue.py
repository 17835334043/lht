from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Firefox()
driver.get(' https://www.ctrip.com/')
sleep(2)
driver.find_element_by_class_name('set-text').click()#登录
sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[5]/div[2]/a[2]').click()
sleep(2)
driver.switch_to.window(driver.window_handles[-1])
sleep(2)
kj=driver.find_element_by_css_selector('#ptlogin_iframe')
driver.switch_to.frame(kj)
sleep(5)
driver.find_element_by_id('img_out_3091258714').click()#头像登录
sleep(1)
# ③　携程首页输入西安，对搜索按钮做回车事件（5分）
# 合理的使用最少2种以上定位，跟2题定位方式不一样
# 输入2分，回车事件3分
driver.switch_to.window(driver.window_handles[0])
sleep(1)

driver.find_element_by_id('_allSearchKeyword').send_keys('西安')#输入西安
sleep(1)
driver.find_element_by_id('search_button_global').send_keys(Keys.ENTER)#搜索按钮
sleep(1)
driver.switch_to.window(driver.window_handles[-1])
sleep(1)
# ④　任意选择一个景点，点击预定（5分）
# 最少1种使用class定位方式
# 景点2分，预定3分
driver.find_element_by_link_text('景点').click()#点击景点
sleep(1)
driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[1]/ul/li[1]/p/a').click()#点击详情
sleep(2)
driver.switch_to.window(driver.window_handles[-1])
sleep(1)
driver.execute_script('window.scrollTo(0,700)')
sleep(1)
driver.find_element_by_id('J_DepartDate').click()
sleep(1)
driver.execute_script('window.scrollTo(0,200)')
sleep(1)
driver.find_element_by_class_name('date_num').click()
sleep(1)
driver.find_element_by_link_text('立即预订').click()
sleep(1)
# ⑤　携程首页，点击自由行，输入南京，点击搜索（12分）
# 合理的使用最少4种以上定位，最少1种使用link_text定位方式
# 3种定位 每种3分，link_text定位方式 3分
driver.switch_to.window(driver.window_handles[0])
sleep(1)
driver.find_element_by_link_text('自由行').click()
sleep(1)
driver.find_element_by_class_name('search_txt').send_keys('南京')
sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[1]/div/div[2]/a').click()
sleep(1)
# ⑥　选择1个景点，选择日期，点击立即预定（9分）
# 合理的使用最少3种以上定位，每种定位3分，最少1种使用name定位方式
driver.execute_script('window.scrollTo(0,400)')
sleep(1)
driver.find_element_by_class_name('list_product_pic').click()
sleep(1)
driver.switch_to.window(driver.window_handles[-1])
sleep(1)
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div/i').click()
sleep(1)
driver.find_element_by_class_name('is-allow-hover').click()
sleep(1)
driver.execute_script('window.scrollTo(0,300)')
sleep(1)
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/i').click()
sleep(1)
driver.find_element_by_id('grp-103723-order-order-1790596--').click()#查询资源
sleep(1)

# ⑦　携程首页，点击跟团游，输入秦皇岛，对秦皇岛做全选事件，并复制（15分）
# 合理的使用最少3种以上定位，每种定位3分，全选3分、复制3分
driver.switch_to.window(driver.window_handles[0])
sleep(1)
driver.find_element_by_link_text('跟团游').click()
sleep(1)
driver.find_element_by_class_name('search_txt').send_keys('秦皇岛',Keys.CONTROL,'a')
sleep(1)
driver.find_element_by_class_name('search_txt').send_keys(Keys.CONTROL,'c')
sleep(1)
# # ⑧　点击自由行，将复制的秦皇岛，粘贴到输入框中，并对输入框做回车事件（6分）
# # 粘贴3分，回车3分
driver.find_element_by_class_name('search_txt').send_keys(Keys.CONTROL,'v')
sleep(1)
driver.find_element_by_class_name('search_txt').send_keys(Keys.ENTER)
sleep(1)
# ⑨　鼠标悬停到我的携程，选择我的优惠券（6分）
# 悬停3分，选择3分
driver.switch_to.window(driver.window_handles[0])
sleep(1)
xt=driver.find_element_by_link_text('我的携程')
ActionChains(driver).move_to_element(xt).perform()
sleep(5)
driver.close()
driver.quit()
# ⑩　请对如上操作合理的使用所有你学习的浏览器事件（10分）