import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_UP = 30
PROMISED_DOWN = 10
TWITTER_EMAIL = "agarwal.sakshi.100doc@gmail.com"
TWITTER_PASSWORD = "Sa@12345"
TWITTER_USERNAME = "@SakshiA100doc"


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        # speed_but = self.driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/div[1]/div/button')
        time.sleep(3)

        privacy_but = self.driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        privacy_but.click()
        time.sleep(3)

        go_but = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_but.click()
        time.sleep(60)

        down_val = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        up_val = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(up_val)
        print(down_val)
        time.sleep(2)

    def tweet_at_provider(self):
        self.driver.get("https://x.com/?lang=en")
        time.sleep(3)
        wel_x = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div[2]/div/div/div/button')
        wel_x.click()
        time.sleep(3)
        sign_x = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div/span/span')
        sign_x.click()
        time.sleep(3)
        # self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[4]/label/div/div[2]/div/input').send_keys(TWITTER_EMAIL, Keys.ENTER)
        self.driver.find_element(by=By.NAME,
                                 value="text").send_keys(
            TWITTER_EMAIL, Keys.ENTER)
        time.sleep(3)
        # self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div/input').send_keys(TWITTER_USERNAME, Keys.ENTER)
        self.driver.find_element(by=By.NAME,
                                 value="text").send_keys(
            TWITTER_USERNAME, Keys.ENTER)
        time.sleep(3)
        # self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(TWITTER_PASSWORD, Keys.ENTER)
        self.driver.find_element(by=By.NAME,
                                 value="password").send_keys(
            TWITTER_PASSWORD, Keys.ENTER)
        time.sleep(3)

        try:
            close = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/button')
            close.click()
            time.sleep(5)
        except:
            pass
        else:
            pass

        try:
            close1 = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div[1]/div/div/div/button')
            close1.click()
            time.sleep(5)
        except:
            pass
        else:
            pass

        # new_post = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/svg/g/path')
        # new_post.click()

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div').send_keys(tweet)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span').click()

        # time.sleep(5)
        # tweet_compose = self.driver.find_element(By.XPATH,
        #                                         value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        # tweet_compose.send_keys(tweet)

        # tweet_button = self.driver.find_element(By.XPATH,
        #                                         value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        # tweet_button.click()

        time.sleep(2)
        self.driver.quit()
