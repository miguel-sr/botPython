from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

email = ""
senha = ""

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--incognito")

browser = webdriver.Chrome(chrome_options=options)
browser.maximize_window()
browser.get("https://www.linkedin.com/uas/login")
browser.find_element(by=By.XPATH, value='//*[@id="username"]').send_keys(email)
browser.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys(senha)
browser.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button').click()
browser.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
time.sleep(2.5)
browser.find_element(by=By.XPATH, value='//*[@id="mn-connections-search-input"]').send_keys("c")
time.sleep(2.5)

quantidadeDeConexoesParaRemover = 30
i = 1

while i <= quantidadeDeConexoesParaRemover:
  pyautogui.click(x=990, y=367)
  pyautogui.click(x=990, y=373)
  time.sleep(0.5)
  pyautogui.click(x=990, y=483)
  i += 1