import requests
from selenium import webdriver
from requests.auth import HTTPBasicAuth
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import zipfile, random, string, time

username = "lum-customer-rubelrana-zone-rubel3-country-us-state-NY-city-buffalo-session-"
char_set = string.ascii_lowercase
ext = random.sample(char_set * 8, 8)
ext = ''.join(ext)

PROXY_HOST = "zproxy.lum-superproxy.io"
PROXY_PORT = 22225
PROXY_USER = username + ext
PROXY_PASS = "o1ockrt34qhh"
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

browser.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%(user)s",
            password: "%(pass)s"
        }
    };
}

browser.webRequest.onAuthRequired.addListener(
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

pluginfile = 'proxy_auth_plugin.xpi'

with zipfile.ZipFile(pluginfile, 'w') as zp:
    zp.writestr("manifest.json", manifest_json)
    zp.writestr("background.js", background_js)

# co = Options()
# co.add_argument("--start-maximized")
# # co.add_extension(pluginfile)

# # ----- without image ----- (uncomment this)
# # prefs = {"profile.managed_default_content_settings.images": 2}
# # co.add_experimental_option("prefs", prefs)
profile = webdriver.FirefoxProfile()
profile.add_extension(extension=pluginfile)
driver = webdriver.Firefox(executable_path='geckodriver.exe', firefox_profile=profile)
# driver = webdriver.Chrome(chrome_options=co)


# PROXY_HOST = "zproxy.lum-superproxy.io"
# PROXY_PORT = 22225
# USERNAME = username + ext 
# PASSWORD = "o1ockrt34qhh"

# PROXY = "127.0.0.1:24000"
# webdriver.DesiredCapabilities.FIREFOX['proxy']={
#     "httpProxy":PROXY,
#     "ftpProxy":PROXY,
#     "sslProxy":PROXY,
#     "noProxy":None,
#     "proxyType":"MANUAL",
# }
# driver = webdriver.Firefox(executable_path='geckodriver.exe')
# driver.get('http://www.whatsmyip.org/')

# profile = webdriver.FirefoxProfile()
# profile.set_preference("network.proxy.type", 1)
# profile.set_preference("network.proxy.http", PROXY_HOST)
# profile.set_preference("network.proxy.http_port", PROXY_PORT)
# profile.set_preference("network.proxy.socks_username", USERNAME)
# profile.set_preference("network.proxy.socks_password", PASSWORD)

# profile.update_preferences()

# # executable_path  = define the path if u don't already have in the PATH system variable. 
# driver = webdriver.Firefox(executable_path='geckodriver.exe',firefox_profile=profile)
driver.get("https://whatismyipaddress.com/")
# # driver.maximize_window()
# WebDriverWait(driver, 50).until(EC.alert_is_present(), 'Timed out waiting for alerts to appear')
# alert=driver.switch_to.alert
# print("here")
# time.sleep(2)
# # alert.send_keys(USERNAME+webdriver.common.keys.Keys.TAB+PASSWORD)
# alert.send_keys(USERNAME)
# time.sleep(2)
# time.sleep("here1")
# alert.accept()
time.sleep(10000)

# return driver