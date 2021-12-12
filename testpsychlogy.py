from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("https:///www.google.com")
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 20)
btn_1 = wait.until(EC.element_to_be_clickable((By.NAME, 'q'))).send_keys('تست روانشناسی'+ Keys.ENTER)
btn_2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#rso > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)"))).click()
btn_3 = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/section[2]/div[2]/div/div[1]/div[1]/div/div[1]/h3/a"))).click()
btn_4 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/section[2]/div/div[3]/div[2]/a[1]'))).click()
btn_5 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sex"]')))
drop_1 = Select(btn_5).select_by_value("male")
btn_6 = wait.until(EC.element_to_be_clickable((By.ID, "year_birth")))
drop_2 = Select(btn_6).select_by_value('1375')
btn_7 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/section[2]/div/div/div/div/div[1]/div/form/button'))).click()

i = 1
while i <= 10:
    if i % 2 == 0:
        btn_7 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[3]/div/div[1]/label'))).click()
    elif i % 2 !=0:
        btn_8 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[3]/div/div[2]/label'))).click()
    i += 1