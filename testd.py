from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def add_credentials_moz(driver, target, username, password):
    driver.execute("SET_CONTEXT", {"context": "chrome"})        
    driver.execute_script("""
        let [target, username, password] = [...arguments];
        let WebRequest = Cu.import('resource://gre/modules/WebRequest.jsm', {});
        WebRequest.onAuthRequired.addListener(function listener(){
          WebRequest.onAuthRequired.removeListener(listener);
          return Promise.resolve({authCredentials: {username: username, password: password}});
        }, {urls: new MatchPatternSet([target])}, ['blocking']);
        """, target, username, password)        
    driver.execute("SET_CONTEXT", {"context": "content"})

WebDriver.add_credentials_moz = add_credentials_moz



driver = webdriver.Firefox()
driver.add_credentials_moz("https://httpbin.org/*", username="user", password="passwd")

driver.get("https://httpbin.org/")

driver.find_element_by_css_selector("[href='/basic-auth/user/passwd']")\
      .click()