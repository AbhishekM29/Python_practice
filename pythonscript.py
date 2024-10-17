
from curses import keyname
from tkinter import S
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver=webdriver.Chrome("D:/python_study/drivers/chromedriver.exe")

driver.maximize_window()

driver.get("https://www.youtube.com")

searchinput = driver.find_element(By.XPATH,"//input[@id='search']")

searchinput.send_keys("nature videos")

searchbtn= driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button/yt-icon")
searchbtn.click()








