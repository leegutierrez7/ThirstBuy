import time
import emoji
from bs4 import BeautifulSoup
from twilio.rest import Client
from urllib.request import urlopen

# -------------- INSERT INFORMATION HERE --------------- #
# Twilio Credentials
account_sid = ""
auth_token  = ""

# Phone Numbers
my_number = ""
twilio_number = ""
# ------------------------------------------------------ #

client = Client(account_sid, auth_token)                    # Twilio Client

item = 'RTX 3080: '
no  = emoji.emojize(':x:', use_aliases=True)                # Emoji: Red "X"
yes = emoji.emojize(':white_check_mark:', use_aliases=True) # Emoji: Green check

# Website URL : Microcenter
url = 'https://www.microcenter.com/search/search_results.aspx?N=&cat=&Ntt=rtx+3080&searchButton=search'

while True:
    response = urlopen(url).read()
    soup = BeautifulSoup(response, "lxml")                      # A parser tree (lxml format) helps search for a string.

    online = soup.findAll("div", {"class": "stock"})            # Depending on the website, find the field that is changes when the item is in stock.
    clearance = soup.findAll("div", {"class": "clearance"})     # Depending on the website, find the field that is changes when the item is in stock.

    if (str(online).find("in stock") == -1 or str(clearance).find("$") == -1):  # If .find() returns -1, item isn't in stock.
        print(item + no)

    else:                                                                       # Else, item is in stock (send out text message)
        txt = item 
        if str(online).find("in stock") != -1:
            txt = "Online "
            if str(clearance).find("$") != -1:
                txt = txt + "& Clearance "
        elif str(clearance).find("$") != -1:
            txt = txt + "Clearance " 

        client.messages.create(to=my_number,            # YOUR phone number
                               from_=twilio_number,     # Twilio phone number
                               body=txt+yes)            # Text Message being delivered

    time.sleep(120)                                     # Scans website every 2 minutes
