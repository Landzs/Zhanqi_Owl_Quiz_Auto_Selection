from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from time import gmtime, strftime
import time
import random
import re
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
        #self.URL = 'https://www.zhanqi.tv/topic/owl'
        self.URL = 'https://www.zhanqi.tv/topic/owl'
        self.START_TIME = 0
        self.EXECUTION_TIME = 0
        self.COINS = 0

    #####################################################
    #               Start                               #
    #####################################################
    def start(self):
        self.WEBDRIVER.get(self.URL)


        #self.WEBDRIVER.get(self.URL)
        self.START_TIME = time.time()
        sleep(random.uniform(0, 1) * 3 + 5)

        #self.WEBDRIVER.refresh()
        self.write_in_txt(strftime("%d %b %Y", time.localtime()))
        #self.COINS = self.check_coins()
        #print(self.COINS)

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
        #self.WEBDRIVER.refresh()

    #####################################################
    #               Check Coins                         #
    #####################################################
    def check_coins(self):
        # sleep(random.uniform(0, 1) * 3 + 5)
        # self.WEBDRIVER.refresh()
        sleep(random.uniform(0, 1) * 3 + 5)
        self.click_xpath('/html/body/div[2]/div[3]/div/div/ul/li[4]/a')  # 代币活动
        sleep(random.uniform(0, 1) * 3 + 5)
        temp_str = self.WEBDRIVER.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[3]/div[2]/div[1]/div/div[2]/span[2]').text
        temp_num = int(temp_str)
        temp_str = 'coins: ' + temp_str + '\n'
        self.write_in_txt(temp_str)
        return temp_num


    #####################################################
    #               Click                               #
    #####################################################
    def click_xpath(self, xpath):
        sleep(random.uniform(0, 1) * 3 + 5)
        element = self.WEBDRIVER.find_element_by_xpath(xpath)
        if element and element.is_displayed():
            element.click()  # 签到


    #####################################################
    #               Click                               #
    #####################################################
    def click_selector(self, selector):
        sleep(random.uniform(0, 1) * 3 + 5)
        element = self.WEBDRIVER.find_element_by_css_selector(selector)
        if element and element.is_displayed():
            print("display")
            element.click()  # 签到
        else:
            print("not display")

    #####################################################
    #               Daily Sign-in                       #
    #####################################################
    def daliy_sign_in(self):

        self.click('//*[@id="js-fans-sign-btn"]') # 签到
        self.click('/html/body/div[35]/div[2]/button')  # 确定
        # / html / body / div[36] / div[2] / button
        self.click('/html/body/div[2]/div[3]/div/div/ul/li[4]/a')  # 代币活动
        self.click('/html/body/div[2]/div[3]/div/div/div[3]/div[1]/div[2]/div[2]/div[2]/a')  # 签到
        self.click('/html/body/div[5]/a[2]')  # 知道了

        self.click('/html/body/div[2]/div[3]/div/div/ul/li[2]/a') # 皮肤兑换
        self.click('//*[@id="js-owl-sign"]')  # 签到 每日签到赠送10欢呼值
        # self.click('//*[@id="js-time-scores"]')  # 领取 每日观赛10分钟可获得10欢呼值

        # sleep(random.uniform(0, 1)*3)
        # self.WEBDRIVER.find_element_by_xpath('//*[@id="js-room-super-panel"]/div/div[2]/div[3]/div[2]/div[2]/ul/li[1]/a/i[2]').click() #我的
        #
        # sleep(random.uniform(0, 1)*3)
        # self.WEBDRIVER.find_element_by_xpath('//*[@id="js-room-super-panel"]/div/div[2]/div[3]/div[1]/div/ul/li[1]/a/p').click() #任务
        #
        # sleep(random.uniform(0, 1) * 3)
        # self.WEBDRIVER.find_element_by_xpath('//*[@id="js-room-task-panel"]/div[2]/div[3]/div[2]/div/ul/li[1]/div[2]/div[2]/a').click()  # 领取
    #####################################################
    #                  Close                            #
    #####################################################
    def close(self):
        self.WEBDRIVER.close()


    #####################################################
    #               Get Text                            #
    #####################################################
    def get_text_xpath(self, xpath):
        sleep(random.uniform(0, 1) * 3 + 5)
        element = self.WEBDRIVER.find_element_by_xpath(xpath)
        if element and element.is_displayed():
            return element.text  # 签到

    #####################################################
    #               Get Text                            #
    #####################################################
    def get_text_selector(self, selector):
        sleep(random.uniform(0, 1) * 3 + 5)
        element = self.WEBDRIVER.find_element_by_css_selector(selector)
        if element and element.is_displayed():
            return element.text  # 签到


    #####################################################
    #                  Get Number                       #
    #####################################################
    def get_number(self):
        number1 = 0
        number2 = 0

        # element1 = self.get_text_xpath('//*[@id="js-flash-panel"]/div[5]/div[1]/div[4]/a[1]/i[2]')  #  #js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix > a.left-team.fl.js-left-area > i.js-score
        # element2 = self.get_text_xpath('//*[@id="js-flash-panel"]/div[5]/div[1]/div[4]/a[2]/i[2]')  #  #js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix > a.right-team.fr.js-right-area > i.js-score

        element1 = self.get_text_selector("#js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix > a.left-team.fl.js-left-area > i.js-score")
        element2 = self.get_text_selector("#js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix > a.right-team.fr.js-right-area > i.js-score")
        # js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix.active > a.right-team.fr.js-right-area > i.js-score
        # print(element1)  #js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix > a.left-team.fl.js-left-area
        # print(element2)
        if element1:
            number1 = re.findall(r'\d+', element1)
            print(number1)

        if element2:
            number2 = re.findall(r'\d+', element2)
            print(number2)
        return number1, number2

    #####################################################
    #              Write In Txt                         #
    #####################################################
    def write_in_txt(self,write_in):
        with open("record.txt" , "a") as f:  # 格式化字符串还能这么用！
            f.write("\n------------------------------------------------------------------------------\n")
            for i in write_in:
                f.write(i)

    #####################################################
    #               Quiz Selection                      #
    #####################################################
    def quiz_selection(self):
        while self.EXECUTION_TIME < 22500:#:
            #self.WEBDRIVER.refresh()
            sleep(random.uniform(0, 1) * 3 + 5)
            self.EXECUTION_TIME = time.time() - self.START_TIME
            #
            # temp = self.WEBDRIVER.find_element_by_css_selector(".right-team.fr.js-right-area") #"right-team fr js-right-area active"
            # temp = self.WEBDRIVER.find_element_by_css_selector("#js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix > a.right-team.fr.js-right-area > i.js-name") #"right-team fr js-right-area active"
            # if temp:
            #     print('find')
            #     print(temp)
            #     print(self.WEBDRIVER.find_element_by_xpath('//*[@id="js-flash-panel"]/div[5]/div[1]/div[4]/a[2]/i[1]'))
            #     if temp.text:
            #         print("temp.text")

            number1, number2 = self.get_number()
            if number1 != 0 and number2 != 0:
                temp_str = strftime("%H:%M:%S", time.localtime()) + '\n' + 'A: ' + str(number1) + '\n' + 'B: ' + str(number2) + '\n'

                js = 'window.open("https://www.zhanqi.tv/topic/owl");'
                self.WEBDRIVER.execute_script(js)
                sleep(random.uniform(0, 1) * 3 + 5)
                now_handle = self.WEBDRIVER.current_window_handle
                for handles in self.WEBDRIVER.window_handles:
                    if handles != now_handle:
                        self.WEBDRIVER.close()
                        self.WEBDRIVER.switch_to.window(handles)


                #self.WEBDRIVER.refresh()
                sleep(random.uniform(0, 1) * 3 + 5)
                if number1 > number2:
                    # self.click_xpath('//*[@id="js-flash-panel"]/div[5]/div[1]/div[4]/a[1]/i[1]')  # left
                    #self.click_selector(
                        # "#js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix > a.left-team.fl.js-left-area > i.js-name")            #owl
                          # js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix.active > a.right-team.fr.js-right-area
                    self.click_selector(
                        "#js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix.active > a.left-team.fl.js-left-area")
                        # js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix.active > a.left-team.fl.js-left-area
                        # js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix.active > a.left-team.fl.js-left-area
                        #"#js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix.active > a.left-team.fl.js-left-area > i.js-name")                  #owwc
                        ##js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix.active > a.right-team.fr.js-right-area
                    temp_str = temp_str + ' click left!' + '\n'
                    # print(' click left!')
                else:
                    # self.click_xpath('//*[@id="js-flash-panel"]/div[5]/div[1]/div[4]/a[2]/i[1]')  # right
                    #self.click_selector(
                        # "#js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix > a.right-team.fr.js-right-area > i.js-name")         #owl
                    self.click_selector(
                        "#js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix.active > a.right-team.fr.js-right-area")  # owwc
                        #"#js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix.active > a.right-team.fr.js-right-area > i.js-name")                #owwc
                    temp_str = temp_str +  ' click right!' + '\n'
                    # print(' click right!')
                # // *[ @ id = "js-flash-panel"] / div[5] / div[1] / div[3] / div / div[2]
                self.write_in_txt(temp_str)
                print(temp_str)
                sleep(random.uniform(0, 1) * 10 + 800)
            sleep(random.uniform(0, 1) * 3 + 140)
            self.EXECUTION_TIME = time.time() - self.START_TIME
            print("{:.3f}s".format(self.EXECUTION_TIME))

        self.COINS = self.check_coins() - self.COINS
        temp_str = 'Get coins: ' + str(self.COINS) + '\n'
        self.write_in_txt(temp_str)
        print(self.COINS)


#####################################################
#                Main Function                      #
#####################################################
if __name__ == "__main__":
    wd = Webdrive()
    wd.start()
    #sleep(1200)
    #wd.daliy_sign_in()
    wd.quiz_selection()
    wd.close()