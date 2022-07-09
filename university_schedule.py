from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from datetime import *

s = Service("C:/Users/Szczepan/Downloads/edgedriver_win64 (3)/msedgedriver.exe")
op = webdriver.EdgeOptions()
driver = webdriver.Edge(service=s, options=op)

driver.get("https://plan.polsl.pl/?fbclid=IwAR14dgMJ1yIpwzRa6rdvYleTpCHBPQjRKyiiG3vJaXqfKg14CPYfkCunm04")

driver.switch_to.frame("left_menu")

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/table/tbody/tr[2]/td/ul/li[2]/a/img")))
element.click()

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/table/tbody/tr[2]/td/ul/li[2]/div/ul/li[5]/img")))
element.click()

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/table/tbody/tr[2]/td/ul/li[2]/div/ul/li[5]/div/ul/li[2]/img")))
element.click()

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/table/tbody/tr[2]/td/ul/li[2]/div/ul/li[5]/div/ul/li[2]/div/ul/li[2]/img")))
element.click()

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/table/tbody/tr[2]/td/ul/li[2]/div/ul/li[5]/div/ul/li[2]/div/ul/li[2]/div/ul/li[2]/a")))
element.click()

driver.switch_to.default_content()
driver.switch_to.frame("page_content")

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div[4]/select")))
element = Select(element)

current_day = date.today().day
current_month = date.today().month

for x in range(1, 52):
    element.select_by_index(x)
    text = element.first_selected_option.text

    if(int(text[3:5]) == current_month and int(text[0:2]) <= current_day and int(text[6:8]) >= current_day):
        break

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/input")))
element.click()

