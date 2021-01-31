from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Step1
driver = webdriver.Chrome(executable_path=r'D:\chromedriver_win32\chromedriver.exe')
action = ActionChains(driver)
driver.implicitly_wait(10)
driver.get('https://www.google.com/')
driver.maximize_window()
driver.delete_all_cookies()
flipkart = driver.find_element_by_xpath('//input[@class="gLFyf gsfi"]')

#Step2
flipkart.send_keys("flipkart.com")
opt = driver.find_elements(By.CSS_SELECTOR,'ul.erkvQe li span')

#Step3
print("Printing search options\n")
if opt:
    for ele in opt:
        print(ele.text)
print("\n\n")

#Step4
flipkart.submit()

driver.find_element_by_xpath("//span[contains(text(),'Online Shopping Site for Mobiles, Electronics, Furniture ...')]").click()

#Step5
cancel_button = driver.find_elements_by_xpath("//button[@class='_2KpZ6l _2doB4z']")
if cancel_button:
    cancel_button[0].click()

#Step6
appliences = driver.find_element_by_xpath("//div[contains(text(),'Appliances')]")
action.move_to_element(appliences).perform()
ac = driver.find_element_by_xpath("//a[contains(text(),'Air Conditioners')]")
action.move_to_element(ac).perform()
driver.find_element_by_link_text('Window ACs').click()

#Step7
compare = driver.find_elements_by_xpath("//span[contains(text(),'Add to Compare')]")
compare[1].click()
compare[2].click()
compare[5].click()

#Step8
driver.find_element_by_xpath("//span[contains(text(),'COMPARE')]").click()

ac_names = driver.find_elements_by_xpath("//a[@class='_3L_M2k']")
ac_price = driver.find_elements_by_xpath("//div[@class='_30jeq3']")

#Step9
print(" printing ac names amd respective prices\n")
for ele in range(0,3):
    print("ac name : ",ac_names[ele].text, end=" "*20)
    print("price : ",ac_price[ele].text)

print("\n\n")
count=0

wait = WebDriverWait(driver, 20)

#Step10
for ele in range(0,3):
    count +=1
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Add a product')]")))
    driver.find_elements_by_xpath("//button[@class='_2KpZ6l _2U9uOA _3v1-ww vsi37q']")[ele].click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Place Order')]")))
    if count !=3:
        driver.back()

#Step11
driver.find_element_by_xpath("//input[@class='cfnctZ']").send_keys('533464')
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Check')]"))).click()

stus = []
status1 = driver.find_elements_by_xpath("//div[@class='_1tBBEs']")
if status1:
    for ele in status1:
        stus.append(driver.execute_script("return arguments[0].innerHTML;", ele))
status2 = driver.find_elements_by_xpath("//div[@class='_2pqhhf']")
if status2:
    for ele in status2:
        stus.append(driver.execute_script("return arguments[0].innerHTML;", ele))

#Step12
print( "\n Available status for 533464")
for ele in range(0,len(stus)):
    print(stus[ele])
print("\n\n")  
time.sleep(5)

#Step13
driver.find_element_by_xpath("//div[@class='_3gc7Vf']").click()
driver.find_element_by_xpath("//input[@class='cfnctZ']").send_keys("603103")
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Check')]"))).click()

stus2 = []
status11 = driver.find_elements_by_xpath("//div[@class='_1tBBEs']")
if status11:
    for ele in status11:
        stus2.append(driver.execute_script("return arguments[0].innerHTML;", ele))
status22 = driver.find_elements_by_xpath("//div[@class='_2pqhhf']")
if status22:
    for ele in status22:
        stus2.append(driver.execute_script("return arguments[0].innerHTML;", ele))

#Step14
print("\n Available status for 603103")

for ele in range(0,len(stus2)):
    print(stus2[ele])


#Step15
driver.quit()        

