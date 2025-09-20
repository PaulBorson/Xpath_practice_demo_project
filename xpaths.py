from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def setup():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver


def xpaths(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(2)

    username_input = driver.find_element(By.XPATH, '//input[@name="username"]')
    username_input.send_keys("Admin")
    time.sleep(2)

    password_input = driver.find_element(By.XPATH,"//input[contains(@placeholder,'Password')]")
    password_input.send_keys("admin123")
    time.sleep(2)

    submit_button = driver.find_element(By.XPATH, '//button')
    submit_button.click()
    time.sleep(2)


def xpath2(driver):
    driver.get("https://demoqa.com/text-box")
    time.sleep(2)
    full_name_input = driver.find_element(By.XPATH, "//input[starts-with(@id,'userN')]")
    full_name_input.send_keys("Prattoy Paul")
    time.sleep(2)

    email_input = driver.find_element(By.XPATH, '//input[@id="userEmail" and @type="email"]')
    email_input.send_keys("abcd@aaa.com")
    time.sleep(2)

    cur_address=driver.find_element(By.XPATH, '//textarea[@id="permanentAddress"]/preceding :: textarea')
    cur_address.send_keys("Dhaka")
    time.sleep(2)


    per_address=driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]/following :: textarea')
    per_address.send_keys("Netrakona")
    time.sleep(2)


    button_submit = driver.find_element(By.XPATH, '//div[@class="text-right col-md-2 col-sm-12"]/descendant :: button')
    button_submit.click()


    output= driver.find_element(By.XPATH, '//div[@class="border col-md-12 col-sm-12"]/ child :: p').text

    assert 'Prattoy Paul' in output ,'Not found'
    print('Prattoy Paul successfully added')
    time.sleep(2)



driver = setup()

xpaths(driver)
xpath2(driver)