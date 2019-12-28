from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import zipfile, time, csv
import string
import random
import threading
import queue
import linkFromEmail
import excel
import var


class craigslist_(threading.Thread):

    def __init__(self, threadID, name, info):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.threadID = threadID
        self.name = name
        self.info = info
        var.threadCount += 1

    def run(self):
        for i in range(1):
            try:
                print("Starting " + self.name)
                if var.browserSelect == "Chrome":
                    self.set_proxy(self.info["State"], self.info["City"])
                else:
                    self.set_proxyFirefox(self.info["State"], self.info["City"])

                self.wait()
                print("main func")
                self.driver.get(self.info["clAccount"])
                self.wait()
                self.inputField("inputEmailHandle", self.info["clEmail"])
                self.wait()
                self.inputField("inputPassword", self.info["clPassword"])
                self.wait()
                self.buttonClickById("login")
                self.wait()
                self.driver.implicitly_wait(1)
                
                
                #email verification here
                try:
                    self.wait()
                    self.buttonClickById("onetime")
                    self.wait()
                    time.sleep(10)
                    link = linkFromEmail.fun(self.info["Email"], self.info["Password"], self.info["Imap"])
                    print(link)
                    self.driver.get(link)
                    self.wait()
                except Exception as e:
                    print(e)

                self.driver.implicitly_wait(2)
                self.driver.get(self.info["Link"])
                self.wait()
                
                try:
                    self.driver.find_elements_by_xpath(".//input[@type='radio' and @name='n']")[0].click()
                    self.wait()
                    self.driver.find_elements_by_xpath(".//input[@type='radio' and @name='n']")[1].click()
                    self.driver.implicitly_wait(2)
                    self.wait()
                    try:
                        self.driver.find_element_by_xpath("./html/body/article/section/form/ul/li[11]/label/span[1]/input").click()
                        self.driver.implicitly_wait(2)
                        self.wait()
                    except Exception as e:
                        print(e)
                        time.sleep(10)
                        self.driver.find_element_by_xpath("./html/body/article/section/form/ul/li[11]/label/span[1]/input").click()
                        self.driver.implicitly_wait(2)
                        self.wait()
                    
                    
                    self.driver.find_element_by_xpath(".//*[@id='new-edit']/div/label/label[1]/input").click()
                    self.driver.implicitly_wait(2)
                    self.wait()

                    self.driver.find_element_by_xpath(".//*[@id='new-edit']/div/div[3]/div/button").click()
                    self.driver.implicitly_wait(2)
                    self.wait()
                except Exception as e:
                    print("sub section")
                    print(e)
                    
                try:
                    self.inputField("PostingTitle", self.info["title"])
                    
                except Exception as e:
                    print(e)
                    time.sleep(10)
                    self.inputField("PostingTitle", self.info["title"])

                try:
                    self.inputField("GeographicArea", self.info["City"])
                except Exception as e:
                    print(e)

                self.inputField("postal_code", self.info["Zip"])
                self.inputField("PostingBody", self.info["message"])
                self.driver.implicitly_wait(1)
                self.wait()
                self.buttonClickByClass(".go.big-button.submit-button")
                self.driver.implicitly_wait(1)
                self.wait()

                #posting 2nd page
                self.buttonClickByClass(".continue.bigbutton")
                self.driver.implicitly_wait(1)
                self.wait()

                #positn 3rd page
                self.buttonClickByClass(".bigbutton")
                self.driver.implicitly_wait(1)
                self.wait()

                text = self.driver.find_element_by_xpath(".//*[@id='new-edit']/div/div/h4").text
                if text == "Thanks for posting! We really appreciate it!":
                    print("success")
                else:
                    print("failed")
                    raise Exception("Asking Mobile Number Error")
                
                #phone number page
                #posting FUNCTION is not complete yet
                
                var.threadCount -= 1
                var.monitorQ.put('''<p><span style="color: #0C5E3E; font-size: 30px;">{} </span><br>'''.format("Success-" + " " + self.info["clEmail"]))

            except Exception as e:
                print(e)
                var.threadCount -= 1
                var.monitorQ.put('''<p><span style="color: #D60000; font-size: 30px;">{} </span><br>'''.format("Failed-" + " " + self.info["clEmail"]))
            finally:
                if var.terminate == False:
                    time.sleep(10)
                self.driver.quit()
    #TODO: add stop to terminate thread
    #TODO: add other browser
    #FIXME:

    def wait(self):
        # print("enter wait")
        if var.terminate == True:
            print("terminate")
            raise Exception("Terminate Thread")
        while var.pause == True:
            time.sleep(1)

    def inputField(self, id, inputText):
        self.driver.find_element_by_id(id).send_keys(inputText)

    def buttonClickByClass(self, className):
        name = className
        self.driver.find_element_by_css_selector(name).click()

    def buttonClickById(self, id):
        self.driver.find_element_by_id(id).click()

    def set_proxy(self, state, city):
        # username = "lum-customer-rubelrana-zone-rubel3-country-us-state-"+state+"-city-"+city+"-session-"
        username = var.proxyUser+"-country-us-state-"+state+"-session-"

        char_set = string.ascii_lowercase
        ext = random.sample(char_set * 8, 8)
        ext = ''.join(ext)

        PROXY_HOST = "zproxy.lum-superproxy.io"
        PROXY_PORT = 22225
        PROXY_USER = username + ext
        PROXY_PASS = var.proxyPassword
        print(PROXY_USER)
        manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "scripts": ["background.js"]
            },
            "minimum_chrome_version":"22.0.0"
        }
        """

        background_js = """
        var config = {
                mode: "fixed_servers",
                rules: {
                singleProxy: {
                    scheme: "http",
                    host: "%(host)s",
                    port: parseInt(%(port)d)
                },
                bypassList: ["foobar.com"]
                }
            };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "%(user)s",
                    password: "%(pass)s"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        );
        """ % {
            "host": PROXY_HOST,
            "port": PROXY_PORT,
            "user": PROXY_USER,
            "pass": PROXY_PASS,
        }

        pluginfile = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)

        co = Options()
        co.add_argument("--start-maximized")
        co.add_extension(pluginfile)

        # ----- without image ----- (uncomment this)
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # co.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=co)
        
        # driver = webdriver.Chrome(chrome_options=co)

        # self.driver.get("https://whatismyipaddress.com/")

        # return driver

    def set_proxyFirefox(self, state, city):
        # username = "lum-customer-rubelrana-zone-rubel3-country-us-state-"+state+"-city-"+city+"-session-"
        username = var.proxyUser+"-country-us-state-"+state+"-session-"
        # lum-customer-rubelrana-zone-rubel3-country-us-state-ca-city-al-session-gsdfgsdf
        char_set = string.ascii_lowercase
        ext = random.sample(char_set * 8, 8)
        ext = ''.join(ext)

        PROXY_HOST = "zproxy.lum-superproxy.io"
        PROXY_PORT = 22225
        PROXY_USER = username + ext
        PROXY_PASS = var.proxyPassword
        # temp = PROXY_USER+":"+PROXY_PASS
        # proxy = {'host': PROXY_HOST, 'port': PROXY_PORT, 'usr': PROXY_USER, 'pwd': PROXY_PASS}

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

        self.driver = webdriver.Firefox(executable_path='geckodriver.exe', firefox_profile=fp)
        wait(self.driver, 20).until(EC.alert_is_present())
        alert = self.driver.switch_to_alert()
        alert.send_keys(PROXY_USER + Keys.TAB + PROXY_PASS)
        time.sleep(2)
        alert.accept()
        time.sleep(10)


def main(GUI):
    try:
        excel.main()
        
        for i in range(var.infoLen):
            name = 'Thread-' + str(i)
            if not var.infoQ.empty():
                info = var.infoQ.get()
                craigslist_(i, name, info).start()
                time.sleep(1)
            
            while var.threadCount > 0:
                time.sleep(1)
            if var.terminate == True:
                break
        while var.threadCount > 0:
            time.sleep(1)
        
        print("Finished")
        var.monitorQ.put('''<p><span style="color: #0C5E3E; font-size: 30px;">{} </span><br>'''.format("Finished"))
    except Exception as e:
        print(e)
        var.monitorQ.put('''<p><span style="color: #D60000; font-size: 30px;">{} </span><br>'''.format("ERROR - " + str(e)))
    finally:
        var.terminate = False
        GUI.start.setEnabled(True)


if __name__ == '__main__':
    Number_of_threads = 5
    info = {
        "clAccount": "https://accounts.craigslist.org/",
        "clEmail": "janetzachery3206@yahoo.com",
        "clPassword": "Usabd12345%%",
        "State": "Al",
        "City": "dothan",
        "Zip": "36345",
        "Email": "janetzachery3206@yahoo.com",
        "Password": "NOGHghwx22",
        "Port": "993",
        "Imap": "imap.mail.yahoo.com",
        "Link": "https://post.craigslist.org/c/aub/C/act",
        "title": " ef dsgdf  fdg sfgs df",
        "message": " fdsg sdfg sdf gfdg sdfg sdf"
    }
    craigslist_(0, "Thread-0", info).start()
    # for i in range(Number_of_threads):
    # 	name = 'Thread-' + str(i)
    # 	craigslist_(i, name, info).start()
    # 	time.sleep(1)