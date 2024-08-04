# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from twitter_bot import InternetSpeedTwitterBot

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://tinder.com/")

bot_var = InternetSpeedTwitterBot()
bot_var.get_internet_speed()
bot_var.tweet_at_provider()
