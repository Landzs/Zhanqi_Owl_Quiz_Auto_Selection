from selenium import webdriver
from time import sleep
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
        self.URL = 'https://www.zhanqi.tv/topic/owl'
        self.START_TIME = 0
        self.EXECUTION_TIME = 0


    #####################################################
    #               Start                               #
    #####################################################
    def start(self):
        self.WEBDRIVER.get(self.URL)
        self.START_TIME = time.time()
        sleep(random.uniform(0, 1) * 3 + 5)
        self.WEBDRIVER.refresh()


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
    #               Click                               #
    #####################################################
    def click(self, xpath):
        sleep(random.uniform(0, 1) * 3 + 5)
        element = self.WEBDRIVER.find_element_by_xpath(xpath)
        if element and element.is_displayed():
            element.click()  # 签到

    #####################################################
    #               Daily Sign-in                       #
    #####################################################
    def daliy_sign_in(self):
        #
        # self.click('//*[@id="js-fans-sign-btn"]') # 签到
        # self.click('/html/body/div[35]/div[2]/button')  # 确定
        #
        # self.click('/html/body/div[2]/div[3]/div/div/ul/li[4]/a')  # 代币活动
        # self.click('/html/body/div[2]/div[3]/div/div/div[3]/div[1]/div[2]/div[2]/div[2]/a')  # 签到
        # self.click('/html/body/div[5]/a[2]')  # 知道了

        # self.click('/html/body/div[2]/div[3]/div/div/ul/li[2]/a') # 皮肤兑换
        self.click('//*[@id="js-owl-sign"]')  # 签到 每日签到赠送10欢呼值
        self.click('//*[@id="js-time-scores"]')  # 领取
        # self.click('//*[@id="js-owl-sign"]') # 领取 每日观赛10分钟可获得10欢呼值

        # sleep(random.uniform(0, 1) * 3)
        # print(self.WEBDRIVER.find_element_by_xpath('//*[@id="js-owl-sign"]').text) #test

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

    def get_number(self):
        number1 = 0
        number2 = 0
        element1 = self.WEBDRIVER.find_element_by_xpath('//*[@id="js-flash-panel"]/div[3]/div[1]/div[4]/a[1]/i[2]').text
        element2 = self.WEBDRIVER.find_element_by_xpath('//*[@id="js-flash-panel"]/div[3]/div[1]/div[4]/a[2]/i[2]').text
        # print(element1)
        # print(element2)
        if element1:
            number1 = re.findall(r'\d+', element1)
            print(number1)

        if element2:
            number2 = re.findall(r'\d+', element2)
            print(number2)
        return number1, number2

    def write_in_txt(self,write_in):
        with open("record.txt" % title, "a") as f:  # 格式化字符串还能这么用！
            f.write("\n------------------------------------------------------------------------------\n")
            for i in write_in:
                f.write(i)

    #####################################################
    #               Quiz Selection                      #
    #####################################################
    def quiz_selection(self):
        while True:
            self.WEBDRIVER.refresh()
            sleep(random.uniform(0, 1) * 3 + 10)
            self.EXECUTION_TIME = time.time() - self.START_TIME
            number1, number2 = self.get_number()
            if number1 != 0 and number2 != 0:
                temp_str = "At {:.3f}s".format(self.EXECUTION_TIME) + '\n' + 'A: ' + str(number1) + '\n' + 'B: ' + str(number2) + '\n'
                print("At {:.3f}s".format(self.EXECUTION_TIME))
                if number1 > number2:
                    self.click('//*[@id="js-flash-panel"]/div[3]/div[1]/div[4]/a[1]/i[1]')  # left
                    temp_str = temp_str + ' click left!' + '\n'
                    print(' click left!')
                else:
                    self.click('//*[@id="js-flash-panel"]/div[3]/div[1]/div[4]/a[2]/i[1]')  # right
                    temp_str = temp_str +  ' click right!' + '\n'
                    print(' click right!')

                self.write_in_txt(temp_str)
                sleep(random.uniform(0, 1) * 10 + 900)
            sleep(random.uniform(0, 1) * 3 + 100)
            self.EXECUTION_TIME = time.time() - self.START_TIME
            # print('next!')



#####################################################
#                Main Function                      #
#####################################################
if __name__ == "__main__":
    wd = Webdrive()
    wd.start()
    # wd.daliy_sign_in()
    wd.quiz_selection()
    # wd.close()