#
import time

from selenium import webdriver


def weixin(url):
    # Setup WebDriver
    driver = webdriver.Chrome()

    # Open the URL
    driver.get(url)

    # Extract the header
    time.sleep(1)
    header = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/h1').text
    title = header

    # Extract the content
    content = driver.find_element_by_class_name('rich_media_content').text

    con = content
    driver.quit()
    return title, con

# tit,con = weixin('https://mp.weixin.qq.com/s/d8tO-ae68Ny3C6Ae3L8zIA')
# print(tit)
# print(con)