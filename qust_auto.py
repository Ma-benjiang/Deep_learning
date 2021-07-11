#!usr/bin/python3
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

# stu_password = "zhouhao123098"
# stu_name = "1803040631"
class Qust:
    def __init__(self):
        # self.url = "http://jwglxt.qust.edu.cn/jwglxt/xtgl/login_slogin.html"
        self.url="https://wvpn.qust.edu.cn/http/77726476706e69737468656265737421f9e7408f347e79456d1cc7a99c406d3609/tpass/login?service=https%3A%2F%2Fwvpn.qust.edu.cn%2Flogin%3Fcas_login%3Dtrue#act=portal/viewhome"
        self.browser = webdriver.Chrome('./chromedriver.exe')
    def log_in(self):
        browser = self.browser
        browser.get(self.url)
        browser.implicitly_wait(10)
        input1 = browser.find_element_by_id('un')
        input1.clear()
        input1.send_keys("1701010717")
        input2 = browser.find_element_by_id('pd')
        input2.send_keys("308518")
        bottom = browser.find_element_by_class_name("login_box_landing_btn")
        # time.sleep(3)
        bottom.click()
        lib = browser.find_element_by_xpath("//*[@id='app_a'][3]")
        lib.click()
        # time.sleep(3)
        # time.sleep(25)
        # check=browser.find_element_by_xpath(u'//a[text()="中文资源"]')
        # check.click()
        # che=browser.find_element_by_partial_link_text("中文")
        # che.click()

        # infcheck.click()
        # time.sleep(4)
        # print(browser.get_cookies())
        # cookies = {i["name"]: i["value"] for i in browser.get_cookies()}
        # print(cookies)
        # time.sleep(4)
        # select=Select(browser.find_element_by_name("dropdown-toggle"))
        # time.sleep(2)
        # select.select_by_index(5)
        time.sleep(110)
        # self.browser.quit()

if __name__ == "__main__":
    qust = Qust()  # 实例化
    qust.log_in()  # 之后调用登陆方法