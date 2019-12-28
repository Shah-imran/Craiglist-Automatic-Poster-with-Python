#read instructions at the end
from selenium import webdriver
import time

#driver object
driver = webdriver.Chrome('chromedriver.exe')

#use this function to click a button with id
def buttonClickById(id):
    id = id
    driver.find_element_by_id(id).click()

def buttonClickByClass(className):
    name = className
    driver.find_element_by_css_selector(name).click()

#use this function to input in a text field
def inputField(id, inputText):
    id = id
    inputText = inputText
    driver.find_element_by_id(id).send_keys(inputText)

class craigslist_:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self, emailPass):
        driver.get("https://accounts.craigslist.org/login")
        time.sleep(2)
        inputField("inputEmailHandle", self.email)
        time.sleep(1)
        inputField("inputPassword", self.password)
        time.sleep(1)
        buttonClickById("login")
        time.sleep(1)
        buttonClickById("onetime")

        #email verification here
        time.sleep(10)
        import linkFromGmail

        link = linkFromGmail.fun(self.email, emailPass)
        driver.get(link)

    def posting(self, title, city, postal, description, contact_no):
        driver.get("https://post.craigslist.org/c/dhn/C/act")
        time.sleep(1)

        inputField("PostingTitle", title)
        time.sleep(1)
        inputField("GeographicArea", city)
        time.sleep(1)
        inputField("postal_code", postal)
        time.sleep(1)
        inputField("PostingBody", description)
        time.sleep(1)

        buttonClickByClass(".go.big-button.submit-button")
        time.sleep(1)

        #posting 2nd page
        buttonClickByClass(".continue.bigbutton")
        time.sleep(1)

        #positn 3rd page
        buttonClickByClass(".bigbutton")
        time.sleep(1)

        #phone number page
        

        #posting FUNCTION is not complete yet


ob1 = craigslist_("EMAIL", "CRAIGSLIST_PASSWORD")
ob1.login("PASSWORD_OF_EMAIL_ACCOUNT")
ob1.posting("Posting title", "Dothan", "36345", "Description about the post will go here", "XXXXXXXXXX")

'''
First create an object with EMAIL and PASSWORD
ob1 = craigslist_("EMAIL", "CRAIGSLIST_PASSWORD")

then, to login, call the login FUNCTION. It'll do the email verification automatically
ob1.login("PASSWORD_OF_EMAIL_ACCOUNT")

to post, call the post FUNCTION with TITLE, CITY, POSTAL CODE, DESCRIPTION and CONTACT_NO
ob1.posting("Posting title", "Dothan", "36345", "Description about the post will go here", "XXXXXXXXXX")

'''