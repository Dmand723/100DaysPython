from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chromeOptions)
driver.get('https://orteil.dashnet.org/experiments/cookie/')

upgrades = {}

cookie = driver.find_element(by=By.ID, value="cookie")

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes

while True:
    cookie.click()
    
    #after 5 secconds 
    if time.time() > timeout:
        curMoney = int(driver.find_element(By.ID, 'money').text.replace(',',''))

        allUpgradeBtns = driver.find_elements(By.CSS_SELECTOR, '#store div')
        for upgrade in allUpgradeBtns:
            try:
                upgradeHeader = upgrade.find_element(By.CSS_SELECTOR, 'b').text.replace(' ','')
        
                title, price = upgradeHeader.split('-')

                upgrades[title] = {'price':int(price.replace(',','')),"ID":upgrade.get_attribute('id')}
            except:
                pass

        canBuy = []
        for e in upgrades:
            if curMoney >= upgrades[e]['price']:
                canBuy.append(upgrades[e])
        if len(canBuy) != 0:
            hightestCanBuy = canBuy[-1]['ID']
            driver.find_element(By.ID,hightestCanBuy).click()
            
        timeout = time.time() +5

    # #after 5 min stop the program and tell how many cps we were making 
    # if time.time() > five_min:
    #     cookie_per_s = driver.find_element(by=By.ID, value="cps").text
    #     print(cookie_per_s)
    #     break