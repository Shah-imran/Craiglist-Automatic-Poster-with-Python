from selenium import webdriver
import random, string
import time
import win32com.client
import pythoncom
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

def set_proxy(state, city):
    
    username = "lum-customer-rubelrana-zone-rubel3-country-us-state-"+state+"-city-"+city+"-session-"
    # username = "lum-customer-rubelrana-zone-rubel3-country-us-state-NY-city-buffalo-session-"
    char_set = string.ascii_lowercase
    ext = random.sample(char_set * 8, 8)
    ext = ''.join(ext)

    PROXY_HOST = "zproxy.lum-superproxy.io"
    PROXY_PORT = 22225
    PROXY_USER = username + ext
    PROXY_PASS = "o1ockrt34qhh"
    temp = PROXY_USER+":"+PROXY_PASS
    proxy = {'host': PROXY_HOST, 'port': PROXY_PORT, 'usr': PROXY_USER, 'pwd': PROXY_PASS}

    fp = webdriver.FirefoxProfile()
    fp.set_preference("network.proxy.type", 1)
    fp.set_preference("network.proxy.http",PROXY_HOST)
    fp.set_preference("network.proxy.http_port",int(PROXY_PORT))
    fp.set_preference("network.proxy.https",PROXY_HOST)
    fp.set_preference("network.proxy.https_port",int(PROXY_PORT))
    fp.set_preference("network.proxy.ssl",PROXY_HOST)
    fp.set_preference("network.proxy.ssl_port",int(PROXY_PORT))  
    fp.set_preference("network.proxy.ftp",PROXY_HOST)
    fp.set_preference("network.proxy.ftp_port",int(PROXY_PORT))   
    fp.set_preference("network.proxy.socks",PROXY_HOST)
    fp.set_preference("network.proxy.socks_port",int(PROXY_PORT))  

    fp.set_preference("general.useragent.override","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A")
    fp.update_preferences()

    driver = webdriver.Firefox(executable_path='geckodriver.exe', firefox_profile=fp)
    # driver.get("https://www.google.com")
    wait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to_alert()
    alert.send_keys(PROXY_USER + Keys.TAB + PROXY_PASS)
    # alert.send_keys(PROXY_USER)
    # time.sleep(2)
    # alert.send_keys(Keys.TAB)
    # time.sleep(2)
    # alert.send_keys(PROXY_PASS)
    time.sleep(2)
    alert.accept()
    # shell = win32com.client.Dispatch("WScript.Shell")   
    # shell.Sendkeys(PROXY_USER)  
    # time.sleep(2)
    # shell.Sendkeys("{TAB}")
    # time.sleep(2)
    # shell.Sendkeys(PROXY_PASS) 
    # time.sleep(2)
    # shell.Sendkeys("{ENTER}")
    # time.sleep(2)
    # driver.close()
    print("here")
    time.sleep(10)
    driver.get("https://www.google.com")
    # driver.quit()
    time.sleep(10000)
    return driver
# time.sleep(10000)

if __name__ == '__main__':
    set_proxy("NY","buffalo")