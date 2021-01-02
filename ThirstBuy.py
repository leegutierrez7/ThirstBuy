import time
import hashlib
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
from urllib.request import urlopen
# Create account on Twilio via their website (Client that enables text messages).
client = Client("", # account_sid
                "") # auth_token

while True:
    #The website you're looking for any changes on. -> For me its the Microcenter website and I'm looking for a RTX 3080, this link is really interchangable. 
    url = 'https://www.microcenter.com/search/search_results.aspx?N=&cat=&Ntt=rtx+3080&searchButton=search'
    response = urlopen(url).read()
    #I'm parsing the html using a parser tre with lxml format, kinda high level but does not really need to be explained you're just searching for a string
    soup = BeautifulSoup(response, "lxml")
    #You need to look at the HTML code to find exactly where the field is being changed when an item comes into stock for me its here in the stock class. 
    mydivs = soup.findAll("div", {"class": "stock"})
    

    # .find returns -1 if not found, so if not found its not in stock. 
    if (str(mydivs).find("in stock") == -1):
        print("Not in stock")
        #Check the website every 2 minutes just so we don't get suspected of DDOS'ing microcenter lol.
        time.sleep(120)
    #If its found then text your phone to let you know its in stock! 
    else:
        client.messages.create(to="",                       # YOUR phone number
                               from_="",                    # Twilio phone number
                               body="RTX 3080 in stock!")   # Text Message being delivered
