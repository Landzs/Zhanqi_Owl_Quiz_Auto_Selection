
import pyautogui
import time
import random
import re
import os
from time import sleep
from time import strftime
from selenium import webdriver
#####################################################
#                 Webdirve Class                    #
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
        self.START_TIME = 0
        self.EXECUTION_TIME = 0
        self.COINS = 0

    #####################################################
    #               Start                               #
    #####################################################
    def start(self):
        self.WEBDRIVER.get(self.URL)
        self.START_TIME = time.time()
        sleep(random.uniform(0, 1) * 1 + 3)

        #self.WEBDRIVER.refresh()
        self.write_in_txt(strftime("%d %b %Y", time.localtime()))
        #self.COINS = self.check_coins()
        #print(self.COINS)

    #####################################################
    #               Save Cookies                        #
    #####################################################
    def save_cookies(self):
        sleep(60)
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
        self.click_selector("#bg2 > div > div > ul > li.tab.token-tab.pr.first-nav")
        #self.click_xpath('/html/body/div[2]/div[3]/div/div/ul/li[4]/a')  # 代币活动
        sleep(random.uniform(0, 1) * 3 + 5)

        temp_str = self.WEBDRIVER.find_element_by_css_selector(
            '# bg2 > div > div > div.tabc.token.first-nav-con.js-active-area.active > div.center > div.hd-1.clearfix > div > div.msg.pr > span.count.js-have-daibi').text
        #temp_str = self.WEBDRIVER.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[3]/div[2]/div[1]/div/div[2]/span[2]').text
        temp_num = int(temp_str)
        temp_str = 'coins: ' + temp_str + '\n'
        self.write_in_txt(temp_str)
        return temp_num

    #####################################################
    #              Mouse Refresh                        #
    #####################################################
    def mouse_refresh(self):
        sleep(random.uniform(0, 1) * 3 + 5)
        pyautogui.click(155, 76)

    #####################################################
    #             Mouse Click Left                      #
    #####################################################
    def mouse_click_left(self):
        sleep(random.uniform(0, 1) * 3 + 5)
        pyautogui.click(806,1004)

    #####################################################
    #             Mouse Click Right                     #
    #####################################################
    def mouse_click_right(self):
        sleep(random.uniform(0, 1) * 3 + 5)
        pyautogui.click(944, 1004)


    #####################################################
    #               Click Xpath                         #
    #####################################################
    def click_xpath(self, xpath):
        sleep(random.uniform(0, 1) * 3 + 5)
        element = self.WEBDRIVER.find_element_by_xpath(xpath)
        if element and element.is_displayed():
            element.click()


    #####################################################
    #             Click Selector                        #
    #####################################################
    def click_selector(self, selector):
        sleep(random.uniform(0, 1) * 3 + 3)
        element = self.WEBDRIVER.find_element_by_css_selector(selector)
        if element and element.is_displayed():
            print("display")
            element.click()
            return True
        else:
            print("not display")
            return False

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
            return element.text

    #####################################################
    #               Get Text                            #
    #####################################################
    def get_text_selector(self, selector):
        sleep(random.uniform(0, 1) * 3 + 5)
        element = self.WEBDRIVER.find_element_by_css_selector(selector)
        if element and element.is_displayed():
            return element.text


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

        # print(element1)
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
        with open("record.txt" , "a") as f:
            f.write("\n------------------------------------------------------------------------------\n")
            for i in write_in:
                f.write(i)

    #####################################################
    #              Open New Tab                         #
    #####################################################
    def open_new_tab(self,write_in):

        js = 'window.open("https://www.zhanqi.tv/topic/owl");'
        self.WEBDRIVER.execute_script(js)
        sleep(random.uniform(0, 1) * 1 + 5)
        self.WEBDRIVER.close()
        for handles in self.WEBDRIVER.window_handles:
                 self.WEBDRIVER.switch_to.window(handles)
        sleep(random.uniform(0, 1) * 1 + 5)


    #####################################################
    #               Quiz Selection                      #
    #####################################################
    def quiz_selection(self):
        while self.EXECUTION_TIME < 22500:#:
            #self.WEBDRIVER.refresh()
            sleep(random.uniform(0, 1) * 1 + 3)
            self.EXECUTION_TIME = time.time() - self.START_TIME

            #self.WEBDRIVER.refresh()
            #self.open_new_tab()
            self.mouse_refresh()
            sleep(random.uniform(0, 1) * 1 + 7)

            temp_str = strftime("%H:%M:%S", time.localtime()) + '\n' + 'checking' + '\n'
            print(temp_str)
            number1, number2 = self.get_number()
            if number1 != 0 and number2 != 0:
                temp_str = strftime("%H:%M:%S", time.localtime()) + '\n' + 'A: ' + str(number1) + '\n' + 'B: ' + str(number2) + '\n'

                #self.open_new_tab()

                pyautogui.hotkey('ctrl', 't')
                sleep(random.uniform(0, 1) * 1 + 2)
                pyautogui.typewrite('https://www.zhanqi.tv/topic/owl', interval=0.25)
                pyautogui.press('enter')
                sleep(random.uniform(0, 1) * 1 + 5)


                display = True
                while display:

                    #self.open_new_tab()

                    if number1 > number2:
                        self.mouse_click_left()

                        #self.click_xpath('//*[@id="js-flash-panel"]/div[3]/div[1]/div[4]/a[1]')  # left
                        #self.click_selector("#js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix > a.left-team.fl.js-left-area > i.js-score")            #owl
                               # js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix.active > a.left-team.fl.js-left-area > i.js-name

                        # display = self.click_selector(
                        #     "#js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix > a.left-team.fl.js-left-area > i.js-score")


                        display = False
                        if not display:
                            temp_str = temp_str + ' click left!' + '\n'
                    else:
                        self.mouse_click_right()
                        # self.click_xpath('//*[@id="js-flash-panel"]/div[3]/div[1]/div[4]/a[2]')  # right
                        #self.click_selector("#js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix > a.right-team.fr.js-right-area > i.js-score")         #owl
                        #display = self.click_selector(
                            # "#js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix > a.right-team.fr.js-right-area > i.js-score")  # owwc

                        # js-flash-panel > div.active-guess-ibox > div.js-main > div.guess-content.clearfix.active > a.right-team.fr.js-right-area

                        display = False
                        if not display:
                            temp_str = temp_str +  ' click right!' + '\n'
                pyautogui.click(300, 44)
                for handles in self.WEBDRIVER.window_handles:
                    self.WEBDRIVER.switch_to.window(handles)

                self.write_in_txt(temp_str)
                print(temp_str)
                sleep(random.uniform(0, 1) * 10 + 600)
            sleep(random.uniform(0, 1) * 3 + 140)
            self.EXECUTION_TIME = time.time() - self.START_TIME


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
    #sleep(1000)
    #wd.daliy_sign_in()
    wd.quiz_selection()
    wd.close()
    os.system('shutdown -h now')


