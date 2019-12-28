from selenium import webdriver
from selenium.webdriver.common.proxy import *
import string, random, time

username = "lum-customer-rubelrana-zone-rubel3-country-us-state-NY-city-buffalo-session-"
char_set = string.ascii_lowercase
ext = random.sample(char_set * 8, 8)
ext = ''.join(ext)

PROXY_HOST = "zproxy.lum-superproxy.io"
PROXY_PORT = 22225
# proxy_url = PROXY_HOST +":"+PROXY_PORT
PROXY_USER = username + ext
PROXY_PASS = "o1ockrt34qhh"
print(PROXY_USER)

prof = webdriver.FirefoxProfile()
prof.set_preference('signon.autologin.proxy', 'true')
prof.set_preference('network.proxy.share_proxy_settings', 'false')
prof.set_preference('network.automatic-ntlm-auth.allow-proxies', 'false')
prof.set_preference('network.auth.use-sspi', 'false')

proxy_data = {'address': "zproxy.lum-superproxy.io:22225",
              'username': PROXY_USER,
              'password': PROXY_PASS}

proxy_dict = {'proxyType': ProxyType.MANUAL,
              'httpProxy': proxy_data['address'],
              'ftpProxy': proxy_data['address'],
              'sslProxy': proxy_data['address'],
              'noProxy': '',
              'socksUsername': proxy_data['username'],
              'socksPassword': proxy_data['password']}

proxy_config = Proxy(proxy_dict)

driver = webdriver.Firefox(executable_path='geckodriver.exe', proxy=proxy_config, firefox_profile=prof)

driver.get('http://www.whatsmyip.org/')

time.sleep(10000)