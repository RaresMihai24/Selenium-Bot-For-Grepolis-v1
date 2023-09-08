import os
import sys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string
from colorama import init, Fore

init()
color = Fore.RED
color2 = Fore.LIGHTGREEN_EX
color3 = Fore.YELLOW
style = ["bold", "underline"]
error_file = open("error_log.txt", "w")
sys.stderr = error_file
AZOG = "[{}]".format(
    color + "Script Started" + Fore.RESET)
acc_conf = "[{}]".format(color3 + "Account created and vacantion mode activated." + Fore.RESET)
print(AZOG)


def generate_random_text(length):
    characters = string.ascii_letters + string.digits

    user = ''.join(random.choice(characters) for _ in range(length))
    return user


tor_browser_path = r"location\Tor Browser\Browser\firefox.exe"
geckodriver_path = r"location\gecko\geckodriver.exe"
text_length = 12
text_length2 = 15
os.startfile(tor_browser_path)
file_path = "accounts.txt"
file_path2 = "accounts_fail.txt"
os.environ["PATH"] += os.pathsep + os.path.dirname(geckodriver_path)
tor_proxy = "socks5://127.0.0.1:9150"
firefox_options = webdriver.FirefoxOptions()
firefox_options.binary_location = tor_browser_path
firefox_options.add_argument(f"--proxy-server={tor_proxy}")

counter = 0

while True:
    try:
        driver = webdriver.Firefox(options=firefox_options)
        driver.get("https://ro.grepolis.com/")
        user = generate_random_text(text_length)
        passw = generate_random_text(text_length2)
        print("[{}]Account_name: {}".format(color2 + "Script" + Fore.RESET, user) +", "+ "{}password: {}".format(color2 + Fore.RESET, passw))

        with open(file_path, "a") as file:
            file.write("User: " + user + ", " + "Password: " + passw + "\n")

        login_nume = driver.find_element(By.ID, "registration_nickname")
        login_nume.send_keys(user)
        login_nume.clear()

        login_parola = driver.find_element(By.ID, "registration_password")
        login_parola.send_keys(passw)
        login_parola.clear()

        login_email = driver.find_element(By.ID, "registration_email")
        login_email.send_keys(user + "@yahoo.com")
        login_email.clear()

        login_checkbox = driver.find_element(By.XPATH,"/html/body/div[3]/div/header/div[3]/div[1]/div/div[1]/div/div[1]/form/div[4]/label[1]")
        login_checkbox.click()

        time.sleep(2)

        register_DO = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/header/div[3]/div[1]/div/div[1]/div/div[1]/form/div[5]/button")))
        register_DO.click()

        cookie_ok = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "cookie-notification-button-text")))
        cookie_ok.click()

        time.sleep(2)

        intemeiation_do = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[14]/div/div[10]/div/div[2]/div[9]/div/div[2]/div[1]/div[3]")))
        intemeiation_do.click()
        time.sleep(2)
        cladire_do = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[25]/div/div[2]/div")))
        cladire_do.click()
        time.sleep(2)
        senat_do = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[23]/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]")))
        senat_do.click()

        setari_do = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[12]/div[5]/div[1]/div")))
        setari_do.click()

        vacanta_do = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, "player-vacation")))
        vacanta_do.click()

        button_vac = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[15]/div[2]/div[5]/div[2]/div/div[3]/form/a/span[1]/span/span")))
        button_vac.click()
        time.sleep(2)

        button_conf_vac = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[16]/div[2]/div[5]/div/div/a[1]/span[1]/span/span")))

        button_conf_vac.click()

        print(acc_conf)
        counter += 1
        driver.quit()
        if counter == 10:
            os.system('taskkill /im firefox.exe /f')
            time.sleep(2)
            os.startfile(tor_browser_path)
            driver.quit()
    except:
        with open(file_path2, "a") as file:
            file.write("User: " + user + ", " + "Password: " + passw + "\n")
            counter += 1
            if counter == 10:
                os.system('taskkill /im firefox.exe /f')
                time.sleep(2)
                os.startfile(tor_browser_path)
        driver.quit()
        continue

sys.stderr = sys.__stderr__
error_file.close()
