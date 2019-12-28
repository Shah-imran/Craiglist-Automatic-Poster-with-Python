import imaplib
import email
from bs4 import BeautifulSoup
import requests

def fun(email, password, imap):
    mail = imaplib.IMAP4_SSL(imap)
    print(email, password, imap)
    mail.login(email, password)
    mail.list()
    # Out: list of "folders" aka labels in gmail.
    mail.select("inbox") # connect to inbox.

    result, data = mail.search(None, "ALL")
    
    ids = data[0] # data is a list.
    id_list = ids.split() # ids is a space separated string
    latest_email_id = id_list[-1] # get the latest
    
    result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
    
    raw_email = data[0][1] # here's the body, which is raw text of the whole email

    soup = BeautifulSoup(raw_email, features="html.parser")
    #print(soup.prettify())
    for link in soup.find_all("a"):
        '''
        print("Inner Text: {}".format(link.text))
        print("Title: {}".format(link.get("title")))'''
        # print("href: {}".format(link.get("href")))
        

        l = format(link.get("href"))

    mail.logout

    return l