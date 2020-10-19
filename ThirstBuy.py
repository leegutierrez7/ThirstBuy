import requests
import time
import hashlib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from twilio.rest import Client
#This is for text messages if you want to use this client - Twillo you need to make an account through their website.
client = Client("",
                "")


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
        client.messages.create(to="",
                               from_="",
                               body="RTX 3080 in stock!")
