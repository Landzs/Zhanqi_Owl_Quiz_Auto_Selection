from selenium import webdriver
from time import sleep
import random

#####################################################
#          Initialize Webdirve Class                #
#####################################################
class Webdrive:

    #####################################################
    #          Initialize Object                        #
    #####################################################
    def __init__(self):

        #####################################################
        #          Initialize                               #
        #####################################################
        self.OPTIONS = webdriver.ChromeOptions()
        self.OPTIONS.add_argument('--user-data-dir=/home/shuo/.config/google-chrome/Default')  # 设置成用户自己的数据目录
        self.WEBDRIVER = webdriver.Chrome("/usr/bin/chromedriver",
                                          chrome_options=self.OPTIONS)
        self.URL = 'https://www.zhanqi.tv/topic/owl'


    #####################################################
    #               Start                               #
    #####################################################
    def start(self):
        self.WEBDRIVER.get(self.URL)


    #####################################################
    #               Save Cookies                        #
    #####################################################
    def save_cookies(self):
        sleep(60)#等待Cookies加载
        cookies = self.WEBDRIVER.get_cookies()
        pickle.dump(self.WEBDRIVER.get_cookies(),
                    open("cookies.pkl","wb"))
        print(cookies)


    #####################################################
    #               Read Cookies                        #
    #####################################################
    def read_cookies(self):
        cookies = pickle.load(open("cookies.pkl",
                                   "rb"))
        for cookie in cookies:
            self.WEBDRIVER.add_cookie(cookie)
        sleep(random.uniform(0, 1) * 3)
        self.WEBDRIVER.refresh()

    #####################################################
    #               Daily Sign-in                       #
    #####################################################
    def daliy_sign_in(self):
        sleep(random.uniform(0, 1) * 3)

        if self.WEBDRIVER.find_element_by_xpath('//*[@id="js-fans-sign-btn"]'):
            self.WEBDRIVER.find_element_by_xpath('//*[@id="js-fans-sign-btn"]').click()  # 签到

        sleep(random.uniform(0, 1) * 3)
        self.WEBDRIVER.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/ul/li[4]/a').click()  # 代币活动

        # sleep(random.uniform(0, 1) * 3)
        # if self.WEBDRIVER.find_element_by_xpath('//*[@id="js-owl-sign"]'):
        #     self.WEBDRIVER.find_element_by_xpath('//*[@id="js-owl-sign"]').click()  # 签到
        #
        # sleep(random.uniform(0, 1) * 3)
        # if self.WEBDRIVER.find_element_by_xpath('//*[@id="js-fans-sign-btn"]'):
        #     self.WEBDRIVER.find_element_by_xpath('//*[@id="js-fans-sign-btn"]').click()  # 领取

        sleep(random.uniform(0, 1) * 3)
        self.WEBDRIVER.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/ul/li[2]/a').click()  # 皮肤兑换

        # sleep(random.uniform(0, 1)*3)
        # self.WEBDRIVER.find_element_by_xpath('//*[@id="js-room-super-panel"]/div/div[2]/div[3]/div[2]/div[2]/ul/li[1]/a/i[2]').click() #我的
        #
        # sleep(random.uniform(0, 1)*3)
        # self.WEBDRIVER.find_element_by_xpath('//*[@id="js-room-super-panel"]/div/div[2]/div[3]/div[1]/div/ul/li[1]/a/p').click() #任务
        #
        # sleep(random.uniform(0, 1) * 3)
        # self.WEBDRIVER.find_element_by_xpath('//*[@id="js-room-task-panel"]/div[2]/div[3]/div[2]/div/ul/li[1]/div[2]/div[2]/a').click()  # 领取
    #####################################################
    #               Close                       #
    #####################################################
    def close(self):
        self.WEBDRIVER.close()

    #####################################################
    #               Quiz Selection                      #
    #####################################################
    # def quiz_selection(self):
    #     while True:
            



#####################################################
#                Main Function                      #
#####################################################
if __name__ == "__main__":
    wd = Webdrive()
    wd.start()
    wd.daliy_sign_in()
    # wd.quiz_selection()
    wd.close()