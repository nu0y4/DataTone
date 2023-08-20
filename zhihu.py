# https://zhuanlan.zhihu.com/p/133449879
import time

from selenium import webdriver


def zhihu(url):
    # Setup WebDriver
    driver = webdriver.Chrome()

    # Open the URL
    driver.get(url)

    a = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/button')
    a.click()
    # Extract the header
    time.sleep(1)
    header = driver.find_element_by_xpath('//html//body//div[1]//div//main//div//article//header//h1').text
    title = header

    # Extract the content
    content = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/article/div[1]/div/div/div').text
    con = content
    driver.quit()
    return title, con



