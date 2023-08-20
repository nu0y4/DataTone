#
import time

from selenium import webdriver


def freebuf(url):
    # Setup WebDriver
    driver = webdriver.Chrome()

    # Open the URL
    driver.get(url)

    # Extract the header
    time.sleep(1)
    header = driver.find_element_by_xpath('/html/body/div[1]/div/div/section/main/div/div[3]/div[2]/div[1]/div[1]/div[1]/span').text
    title = header

    # Extract the content
    content = driver.find_element_by_class_name('content-detail').text

    con = content
    driver.quit()
    return title, con

# tit,con = freebuf('https://www.freebuf.com/articles/web/374665.html')
# print(tit)
# print(con)