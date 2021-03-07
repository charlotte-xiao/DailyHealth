'''
Author: charlottexiao123
Date: 2021-03-07 11:31:57
Description: The Author is a clever man.
'''
from selenium import webdriver
import requests
import time


# 健康日报填写
def autofile(ID, passnumber):
    try:
        chromedriver = r'.\chromedriver.exe'
        browser = webdriver.Chrome(chromedriver)
        url = "http://e-office2.nuist.edu.cn/infoplus/form/XNYQSB/start"
        browser.implicitly_wait(10)
        browser.get(url)
        browser.find_element_by_css_selector("#username").send_keys(ID)
        browser.find_element_by_css_selector("#password").send_keys(passnumber)
        browser.find_element_by_css_selector("#login_submit").click()
        browser.find_element_by_css_selector("input[name='fieldCNS']").click()
        browser.find_element_by_css_selector(
            "input[name='fieldSTQKfrtw']").send_keys("36.8")
        browser.execute_script("$('nobr:contains(确认填报)').click()")
        browser.find_element_by_css_selector(
            "button.dialog_button.default.fr").click()
        time.sleep(5)
        check = browser.find_element_by_css_selector(
            "button.dialog_button.default.fr")
        check.click()
        notify("打卡成功")
        browser.close()
    except Exception as e:
        notify("打卡失败")


# Server酱
def notify(text):
    # 填写Server酱的KEY,例如https://sc.ftqq.com/XXXXXXXXXXX.send
    api = "https://sc.ftqq.com/Server酱的KEY.send"
    data = {"text": "健康日报", "desp": text}
    requests.post(api, data=data)


# 填写账号和密码
if __name__ == "__main__":
    autofile("账号", "密码")
