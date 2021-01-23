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
yes = emoji.emojize(':white_check_mark: ', use_aliases=True) # Emoji: Green check

# Website URL : Microcenter
# url = 'https://www.microcenter.com/search/search_results.aspx?N=&cat=&Ntt=rtx+3080&searchButton=search'
url = 'https://www.microcenter.com/search/search_results.aspx?Ntt=rtx+3080&Ntk=all&sortby=match&N=44&myStore=true'

n = 1

while True:
    response = urlopen(url).read()
    soup = BeautifulSoup(response, "lxml")                      # A parser tree (lxml format) helps search for a string.

    online = soup.findAll("div", {"class": "stock"})            # Depending on the website, find the field that is changes when the item is in stock.
    clearance = soup.findAll("div", {"class": "clearance"})     # Depending on the website, find the field that is changes when the item is in stock.

    if (str(online).find("in stock") == -1 or str(clearance).find("$") == -1):  # If .find() returns -1, item isn't in stock.
        e = emoji.emojize(time.strftime("%-I:%M%p") + ' :satellite: ', use_aliases=True)
        print(e + str(n) + '\t\t\t' + item + no)
        n += 1

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
                               body=txt+yes+url)            # Text Message being delivered

    time.sleep(120)                                     # Scans website every 2 minutes
