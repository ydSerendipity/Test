# 方便延时加载
import time
from selenium import webdriver

# 模拟浏览器打开网站
browser = webdriver.Chrome()
browser.get('https://www.ctguqmx.com')
# 将窗口最大化
browser.maximize_window()

# 根据路径找到按钮,并模拟进行点击
browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/span/a[1]').click()
# 延时2秒，以便网页加载所有元素，避免之后找不到对应的元素
time.sleep(2)

# 格式是PEP8自动转的
# 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
browser.find_element_by_xpath(
    "//*[@id='aw-login-user-name']").send_keys("1837074495@qq.com")
browser.find_element_by_xpath(
    "//*[@id='aw-login-user-password']").send_keys("woshiyd0808")
# 在输入用户名和密码之后,点击登陆按钮
browser.find_element_by_xpath("//*[@id='login_submit']").click()
time.sleep(2)

# 点击登陆后的页面中的签到,跳转到签到页面
browser.find_element_by_xpath("/html/body/div[1]/div/div[5]/a").click()
time.sleep(2)

# 点击签到,实现功能
browser.find_element_by_xpath("//*[@id='qd_button']").click()
time.sleep(2)

# 这个print其实没事什么用,如果真的要测试脚本是否运行成功，可以用try来抛出异常
print("签到成功")

# 脚本运行成功,退出浏览器
browser.quit()
