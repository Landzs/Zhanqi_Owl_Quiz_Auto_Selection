from selenium import webdriver
from time import sleep
import random


chromeOpitons = webdriver.ChromeOptions()
chromeOpitons.add_argument('--user-data-dir=/home/shuo/.config/google-chrome/Default')  # 设置成用户自己的数据目录

wd = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chromeOpitons)
Url = 'https://www.zhanqi.tv/topic/owl'
wd.get(Url)

# sleep(60)#等待Cookies加载
# cookies = wd.get_cookies()
# pickle.dump(wd.get_cookies() , open("cookies.pkl","wb"))
# print(cookies)
# for cookie in cookies:
#     req.cookies.set(cookie['name'],cookie['value'])

# cookies = pickle.load(open("cookies.pkl", "rb"))
# for cookie in cookies:
#     wd.add_cookie(cookie)
# sleep(random.uniform(0, 1) * 3)
# wd.refresh()


sleep(random.uniform(0, 1)*3)
wd.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/ul/li[4]/a').click() #代币活动

sleep(random.uniform(0, 1)*3)
wd.find_element_by_xpath('//*[@id="js-owl-sign"]').click()#签到

sleep(random.uniform(0, 1)*3)
wd.find_element_by_xpath('//*[@id="js-time-scores"]').click()#领取

sleep(random.uniform(0, 1)*3)
wd.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/ul/li[2]/a').click()#皮肤兑换

sleep(random.uniform(0, 1)*3)
wd.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/ul/li[2]/a').click()#皮肤兑换