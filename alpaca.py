import os
import sys
import selenium

from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time 

# os.environ['MOZ_HEADLESS'] = '1'

profile_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
options = Options()
options.set_preference('profile', profile_path)
driver = Firefox(options=options)

######

def testA():
    try:
        driver.get("https://www.google.pl/")    
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[2]/div"))).click()
        element = driver.find_element(By.CSS_SELECTOR, '[name="q"]')
        element.send_keys("CyberAlpaca")
        element.send_keys(Keys.ENTER)
        element2 = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "rso")))
        result = element2.text.find(r"www.cyberalpaca.com")
        if result > 0:
            print('----PASS1----')
        else:
            print('----FAIL1----')
        driver.quit()
        
    except Exception as e:
        print(e)

        
# Poniżej, ze względu na brak jasności co oznacza stwierdzenie 'displayed at the top' podjąłem pewne założenia że obiekt znajduje się w górnej cześci strony zdefiniowanej 
# jako ~25% strony w pierwszym widoku. Oczywiście moje zakładanie czegokolwiek wynika z małej ilości wolnego czasu i jak już usiadłem i pisałem kod to zrobiłem wszystko od razu.
# W normalnym pryzypadku zapytałbym przełożonego bądź klienta o zdefiniowanie pojęcia. 

def testB():
    try:
        driver.set_window_size(1024, 768)   
        driver.get("https://www.cyberalpaca.com/")  
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div/div/div[1]/a[3]'))).click()  
        location = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div/main/section[1]/div[1]/div/div[1]/h1'))).location
        if location["y"] <200:
            print('----PASS2a----')
        else:
            print('----FAIL2a----')
        i = 0
        count = 0
        while True:
            try:
                i+=1
                driver.find_element(By.XPATH, '/html/body/div/main/section[1]/div[1]/div/div[2]/div[1]/div['+str(i)+']').click()
                bufor = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div/main/section[1]/div[1]/div/div[2]/div[2]/div/div')))
                squish = bufor.find_elements(By.CSS_SELECTOR, '[title="Squish"]')
                if bufor.text.find(r'Automated GUI testing') == 0 and len(squish) > 0:    # na stronie 'testing' jest z małej a w zadaniu z dużej 'Testing', użyłem to co jest na stronie. 
                    count+=1
                elif bufor.text.find(r'Embedded testing') == 0 and len(squish) > 0:       
                    count+=1
                elif bufor.text.find(r'API testing') == 0 and len(squish) == 0:            
                    count+=1
            except:
                if count == 3:
                    print('----PASS2b----')
                else:
                    print('----FAIL2b----')
                break
        driver.quit()

    except Exception as e:
        print(e)
        driver.quit()

        
testA()
time.sleep(10)
testB()    
