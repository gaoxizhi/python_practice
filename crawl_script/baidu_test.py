#-*-encoding=utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 初始化一个浏览器（使用Chrome需安装chromedriver）
driver = webdriver.Chrome()
# 初始化一个无界面的浏览器
# driver = webdriver.PhantomJS()

try:
    # 请求网页
    driver.get("https://www.baidu.com")
    # 查找id值为kw的节点对象（搜索输入框）
    input_field = driver.find_element_by_id("kw")
    # 模拟键盘输入内容
    input_field.send_keys("python3")
    # 模拟键盘点击回车键
    input_field.send_keys(Keys.ENTER)
    # 显式等待，设置最长10s
    wait = WebDriverWait(driver, 10)
    # 等待条件：10s内必须有id属性值为content_left节点加载出来，否则抛出异常
    wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))

    # 输出响应信息
    print(driver.current_url)
    print(driver.get_cookies())
    # print(driver.page_source)

finally:
    # 关闭浏览器
    # driver.close()
    pass